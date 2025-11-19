import random
import time
import gradio as gr

# Global flags for pause/stop
pause_flag = False
stop_flag = False


def build_visual(arr, current_index, is_found=False, visited_limit=None):
    """
    HTML visualization:
    - Each element is a box with the number inside.
    - Arrow trail moves left → right:
        - Bright arrow ⤏ over the current element
        - Faint arrows over already visited elements
    - Found box is green.
    - Boxes resize based on list length so everything stays readable on screen.
    """

    # Case handling if user has not generated a list yet
    if not arr:
        return "<div style='font-family: monospace;'>No list generated yet.</div>"

    n = len(arr)

    # Decide box size based on list length
    if n <= 12:
        box_size = 70
        font_size = 18
    elif n <= 25:
        box_size = 55
        font_size = 16
    elif n <= 40:
        box_size = 45
        font_size = 14
    else:
        box_size = 38
        font_size = 13

    # visited_limit controls how many boxes shows the faded arrows
    if visited_limit is None:
        visited_limit = current_index if current_index >= 0 else -1

    # CSS container style
    container_style = (
        "display:flex; flex-wrap:wrap; "
        "gap:10px; justify-content:center; "
        "align-items:flex-start; font-family: monospace;"
    )

    # CSS for the grid and different box states
    css = """
    <style>
    .ls-container { %s }
    .ls-box-wrapper {
        display:flex;
        flex-direction:column;
        align-items:center;
    }
    .ls-cell {
        border-radius:10px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-weight:bold;
        color:#000000 !important;
        box-sizing:border-box;
    }
    .ls-cell-normal {
        border:2px solid #cccccc;
        background:#ffffff;
    }
    .ls-cell-visited {
        border:2px dashed #888888;
        background:#f5f5f5;
    }
    .ls-cell-current {
        border:2px solid #1f77b4;
        background:#e8f4ff;
    }
    .ls-cell-found {
        border:2px solid #2ca02c;
        background:#a8f5a2;
    }
    </style>
    """ % container_style

    html = css
    html += "<div class='ls-container'>"

    # Loop through each element and build its box
    for i, value in enumerate(arr):
        # Determine arrow for this position
        if i == current_index:
            arrow_html = "⤏"  # bright arrow on current item
        elif 0 <= visited_limit and i <= visited_limit:
            arrow_html = "<span style='opacity:0.25'>⤏</span>"  # Faded arrow trail
        else:
            arrow_html = "&nbsp;"

        # Determine box style
        if i == current_index and is_found:
            cell_class = "ls-cell ls-cell-found"
        elif i == current_index:
            cell_class = "ls-cell ls-cell-current"
        elif 0 <= visited_limit and i <= visited_limit:
            cell_class = "ls-cell ls-cell-visited"
        else:
            cell_class = "ls-cell ls-cell-normal"

        # Generate HTML per box
        html += f"""
        <div class="ls-box-wrapper">
            <div style="height:20px; font-size:18px; line-height:20px;">
                {arrow_html}
            </div>
            <div class="{cell_class}"
                style="
                    width:{box_size}px;
                    height:{box_size}px;
                    font-size:{font_size}px;
                    font-weight:bold;
                    color:#000000 !important; 
                ">
                {value}
            </div>
            <div style="font-size:11px; color:#444; margin-top:3px;">
                [{i}]
            </div>
        </div>
        """

    html += "</div>"
    return html


# List generation
def generate_list(list_size):
    """
    Generate a new random list and show it before searching.
    Reset stored steps and current step index.
    """
    global pause_flag, stop_flag
    pause_flag = False
    stop_flag = False

    arr = [random.randint(0, 99) for _ in range(list_size)]
    visual = build_visual(arr, -1, is_found=False, visited_limit=-1)  # no arrow yet
    msg = (
        f"New list generated with size {list_size}:\n"
        f"{arr}\n\n"
        "Now enter a target number and click 'Run Linear Search'."
    )
    steps = []       # clear any previous steps
    current_step = -1
    return arr, visual, msg, steps, current_step


# Main linear search animation and step recording
def linear_search_visual(arr, speed, target_str):
    """
    Perform a linear search on the existing list, step by step.
    Uses 'yield' to animate and records steps so that the user can
    navigate them later with Previous/Next buttons.
    """
    global pause_flag, stop_flag
    pause_flag = False
    stop_flag = False

    # No list yet
    if not arr:
        yield (
            "<div style='font-family: monospace;'>No list yet. Please click 'Generate New List' first.</div>",
            "Please generate a list first.",
            [],
            -1
        )
        return

    # Validate the user's input
    try:
        target = int(str(target_str))
    except ValueError:
        visual = build_visual(arr, -1, is_found=False, visited_limit=-1)
        yield visual, "Please enter a valid integer for the target.", [], -1
        return

    steps = []  # full history of steps
    results = ""

    # Initial message
    intro = (
        f"Searching for {target} in list of size {len(arr)}...\n"
        f"{arr}\n"
    )
    results += intro

    # Before checking anything (step 0)
    steps.append({
        "index": -1,
        "results": results,
        "found": False,
        "visited_limit": -1
    })
    visual = build_visual(arr, -1, is_found=False, visited_limit=-1)
    yield visual, results, steps, 0
    time.sleep(0.3)

    # Helper: what happens when STOP is pressed
    def handle_stop():
        """
        Resets the visualization as if starting over.
        """
        reset_results = "⏹ Search stopped.\n"
        reset_steps = [{
            "index": -1,
            "results": reset_results,
            "found": False,
            "visited_limit": -1
        }]
        reset_visual = build_visual(arr, -1, is_found=False, visited_limit=-1)
        reset_current_step = 0
        return reset_visual, reset_results, reset_steps, reset_current_step

    # Linear search animation
    for i, value in enumerate(arr):
        # Check stop BEFORE doing the step
        if stop_flag:
            visual, results, steps, current_step = handle_stop()
            yield visual, results, steps, current_step
            return

        # Pause loop: stay here until pause_flag is False or stop_flag is set
        while pause_flag and not stop_flag:
            time.sleep(0.1)
        if stop_flag:
            visual, results, steps, current_step = handle_stop()
            yield visual, results, steps, current_step
            return

        # Log the step
        step_msg = f"Step {i + 1}: Checking index {i}, value = {value}\n"
        results += step_msg

        visited_limit = i - 1  # previous ones are "visited"
        is_found = False

        # Update visualization for this step
        visual = build_visual(arr, i, is_found=is_found, visited_limit=visited_limit)
        
        # Save step to history
        steps.append({
            "index": i,
            "results": results,
            "found": is_found,
            "visited_limit": visited_limit
        })
        current_step = len(steps) - 1

        # Yield new animation frame
        yield visual, results, steps, current_step
        time.sleep(max(0.01, float(speed)))

        # If the element is found, stop early
        if value == target:
            found_msg = f"\n✅ Found {target} at index {i} after {i + 1} steps.\n"
            results += found_msg
            is_found = True

            # Update last step as found
            steps[-1] = {
                "index": i,
                "results": results,
                "found": True,
                "visited_limit": visited_limit
            }
            visual = build_visual(arr, i, is_found=True, visited_limit=visited_limit)
            current_step = len(steps) - 1

            yield visual, results, steps, current_step
            return

    # If not found (and not stopped)
    not_found_msg = (
        f"\n❌ {target} was not found in the list.\n"
        f"Checked {len(arr)} elements."
    )
    results += not_found_msg

    # Final step after finishing search: everything visited, no current
    steps.append({
        "index": -1,
        "results": results,
        "found": False,
        "visited_limit": len(arr) - 1
    })
    visual = build_visual(arr, -1, is_found=False, visited_limit=len(arr) - 1)
    current_step = len(steps) - 1

    yield visual, results, steps, current_step


# Step navigation
def go_to_step(delta, arr, steps, current_step):
    """
    Move backward or forward through the recorded steps.
    delta = -1 for previous, +1 for next.
    """

    # Nothing to navigate
    if not steps:
        visual = build_visual(arr, -1, is_found=False, visited_limit=-1)
        msg = "No steps to navigate yet. Run a search first."
        return visual, msg, current_step

    # If current_step is invalid, reset to last step
    if current_step is None or current_step < 0:
        current_step = len(steps) - 1

    # Clamp to valid range
    new_step_index = current_step + delta
    new_step_index = max(0, min(new_step_index, len(steps) - 1))

    step = steps[new_step_index]

    # Regenerate visualization for that step
    visual = build_visual(
        arr,
        step["index"],
        is_found=step["found"],
        visited_limit=step["visited_limit"]
    )
    msg = step["results"]

    return visual, msg, new_step_index


def prev_step(arr, steps, current_step):
    return go_to_step(-1, arr, steps, current_step)


def next_step(arr, steps, current_step):
    return go_to_step(1, arr, steps, current_step)


# Pause/Stop handlers
def toggle_pause(paused):
    """
    Toggle pause_flag and return the new paused state.
    """
    global pause_flag
    new_state = not paused
    pause_flag = new_state
    return new_state


def trigger_stop(stopped):
    """
    Set stop_flag to True so the search halts immediately
    """
    global stop_flag
    stop_flag = True
    return True


# Gradio UI layout 
with gr.Blocks() as demo:

    # Title and instructions
    gr.Markdown("# Linear Search Visualizer")
    gr.Markdown(
        "1. Choose the **list size**.\n"
        "2. Click **Generate New List** to see the numbers as boxes.\n"
        "3. Enter a **target number** and click **Run Linear Search**.\n"
        "4. Watch the arrow and trail move through the boxes from left to right.\n"
        "5. After the search, use **◀ Previous step** and **Next step ▶** to move through the steps manually.\n"
        "6. Use **⏸ Pause/Resume** and **⏹ Stop** to control the animation."
    )

    # States to hold: current list, recorded steps, and current step index
    list_state = gr.State([])
    steps_state = gr.State([])
    current_step_state = gr.State(-1)
    pause_state = gr.State(False)
    stop_state = gr.State(False)

    # Controls (slider and inputs)
    with gr.Row():
        list_size = gr.Slider(
            minimum=5,
            maximum=100,
            step=1,
            value=10,
            label="List size"
        )
        speed = gr.Slider(
            minimum=0.1,
            maximum=2.0,
            step=0.1,
            value=1.0,
            label="Speed (seconds per element)"
        )

    # Target number input
    target_input = gr.Textbox(
        label="Number to search for",
        placeholder="e.g. 7"
    )

    # Main buttons
    with gr.Row():
        generate_button = gr.Button("Generate New List")
        start_button = gr.Button("Run Linear Search")

    # Outputs
    visual_output = gr.HTML(label="Visualization")
    result_output = gr.Textbox(label="Status / Result", lines=8)

    # Step navigation buttons
    with gr.Row():
        prev_button = gr.Button("◀ Previous step")
        next_button_btn = gr.Button("Next step ▶")

    # Pause and Stop buttons 
    with gr.Row():
        pause_button = gr.Button("⏸ Pause/ Resume")
        stop_button = gr.Button("⏹ Stop")

    # Generate a new list
    generate_button.click(
        fn=generate_list,
        inputs=[list_size],
        outputs=[list_state, visual_output, result_output, steps_state, current_step_state]
    )

    # Run linear search on the current list
    start_button.click(
        fn=linear_search_visual,
        inputs=[list_state, speed, target_input],
        outputs=[visual_output, result_output, steps_state, current_step_state]
    )

    # Go to previous recorded step
    prev_button.click(
        fn=prev_step,
        inputs=[list_state, steps_state, current_step_state],
        outputs=[visual_output, result_output, current_step_state]
    )

    # Go to next recorded step
    next_button_btn.click(
        fn=next_step,
        inputs=[list_state, steps_state, current_step_state],
        outputs=[visual_output, result_output, current_step_state]
    )

    # Wire up pause/resume
    pause_button.click(
        fn=toggle_pause,
        inputs=[pause_state],
        outputs=[pause_state],
    )

    # Wire up stop
    stop_button.click(
        fn=trigger_stop,
        inputs=[stop_state],
        outputs=[stop_state],
    )

if __name__ == "__main__":
    demo.launch()
