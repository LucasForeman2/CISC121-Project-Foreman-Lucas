# CISC121-Project-Foreman-Lucas

Why I chose Linear Search:
I chose Linear search because it works with any data type and doesn't require the list to be sorted or prepared beforehand. 

**PROBLEM BREAKDOWN & COMPUTATIONAL THINKING**

**Decomposition**:
* Get the user's input for:
  * A list of number (e.g. "5, 2, 9, 1, 7")
  * A target value to search for (e.g., "9")
* Convert the list input (string) into a python list of integers
* Set an index variable i = 0
* Repeat until we reach the end of the list:
  * Compare the current element array[i] with the target
  * Visually highlight this element in the UI
  * If it matches the target, stop and show the position
  * If not, move to the next index (i = i + 1)
* If we finish the loop without finding the target, show a "not found" message
* Handle invalid input (e.g., non-numeric values, empty list) by showing a clear error message

**Pattern Recognition**
* The algorithm always
  * Starts at the first element and moves forward one step at a time.
  * Repeats the same action: compare current elemnt and then move to the next element
* Each step uses the same pattern:
  * Look at array[i], compared to target, then either stop or increase i.
* This pattern is independent of the exact numbers in the list; it always scans from left to right

**Abstraction**

Shown to the user:
* The list of number they entered
* The target value they are searching for
* The current "step" of the algorithm
  * Which element is being checked
  * A short message like "checking index 2: value 9"
* The final result:
  * "Target found at index X" or "target not found in the list"

Hidden from the user:
* The exact python variables used (i, array, etc.)
* How the string is split and converted into integers
* Internal error handling logic (try/except) - the user only sees an appropriate error message

Chosen daya types:
* Raw user input for the list: string (e.g., "1, 4, 7")
* Converted list: list[int]
* Target value: int
* Return to the UI: a combination of string emssages and a list representation for visualization

**Algorithm Design**
* Input
  * Text box for the list of integers
  * Text box for the target integer
  * A button like "Run Linear Search"
* Processing
  * Parse the list input into list[int]
  * Parse the target input into int
  * Run a linear search loop:
    * For each index i, compare array[i] with the target
    * Record each step in a list of "states" to visialize
  * Decide the final result: found (with index) or not found
* Output
  * Display the list with the current element highlighted step by step
  * Show a text description for each step (e.g., "step 3: checking value 9 at index 2").
  * Show a final message like:
    * "Target 9 found at index 2 after 3 steps."
    * or "Target 10 not found after checking 5 elements
  * Show an error message if the input is invalid
 

<img width="480" height="928.5" alt="image" src="https://github.com/user-attachments/assets/8b23d455-c7cd-4f2e-9170-3f76a2e92170" />


Linear Search in Python:

<img width="664" height="457.5" alt="image" src="https://github.com/user-attachments/assets/a9c8fc16-5904-4a63-aaae-1bbe8f746eb7" />

**Different input Cases**

First thing you see:

<img width="449" height="62" alt="image" src="https://github.com/user-attachments/assets/6959610b-3367-4056-b261-7df34f686d3e" />

Handling valid cases:

<img width="468" height="262" alt="image" src="https://github.com/user-attachments/assets/45e24049-7ddd-40f4-a758-ce291c40c18d" />

Handling invalid cases:

<img width="405" height="121" alt="image" src="https://github.com/user-attachments/assets/00483c79-b88e-429a-8ab1-dcc7041038b7" />



**Final Gradio Code:**

All zoomed out to see the full screen 

<img width="2601" height="1430" alt="image" src="https://github.com/user-attachments/assets/847de5a5-2106-41b2-9671-747f5befd7c2" />






**Hugging Face app link:**

https://huggingface.co/spaces/Lucas4man/CISC121-Project-Foreman-Lucas-LinSearch/blob/main/app.py

AI disclaimers:
All ChatGPT 5.1
* Helped with the addition of boxes and to resize the boxes as more are added
* Created templates for the css part

