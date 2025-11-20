# CISC121-Project-Foreman-Lucas

Why I chose Linear Search:
I chose Linear search because it works with any data type and doesn't require the list to be sorted or prepared beforehand. 

## **Problem Breakdown & Computational Thinking**

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

Chosen data types:
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
 
# **Flowchart**
<img width="480" height="928.5" alt="image" src="https://github.com/user-attachments/assets/8b23d455-c7cd-4f2e-9170-3f76a2e92170" />


# Linear Search in Python:

<img width="664" height="457.5" alt="image" src="https://github.com/user-attachments/assets/a9c8fc16-5904-4a63-aaae-1bbe8f746eb7" />

# **Different Input Cases in Python**

**First thing you see:**

<img width="449" height="62" alt="image" src="https://github.com/user-attachments/assets/6959610b-3367-4056-b261-7df34f686d3e" />

**Handling valid cases:**

<img width="468" height="262" alt="image" src="https://github.com/user-attachments/assets/45e24049-7ddd-40f4-a758-ce291c40c18d" />

**Handling invalid cases:**

<img width="405" height="121" alt="image" src="https://github.com/user-attachments/assets/00483c79-b88e-429a-8ab1-dcc7041038b7" />



## **Final Gradio Code Testing:**
All zoomed out to see the full screen 

**Opening Screen**

<img width="2601" height="1430" alt="image" src="https://github.com/user-attachments/assets/847de5a5-2106-41b2-9671-747f5befd7c2" />

### **List Generation**

**Creating a normal sized list**
<img width="2425" height="1444" alt="image" src="https://github.com/user-attachments/assets/bac512a8-aa17-4083-a60e-2410da6067ca" />

**Creating an Edge Case List**

List of 5:

<img width="2460" height="1418" alt="image" src="https://github.com/user-attachments/assets/21538537-81cc-4980-a4bb-e365849115e0" />

List of 100:

<img width="2401" height="1403" alt="image" src="https://github.com/user-attachments/assets/41c90f4f-28eb-4059-8950-56edca3de654" />

### **Running the Search**

**Search where target is found**

<img width="2410" height="1329" alt="image" src="https://github.com/user-attachments/assets/602d11ea-b8bb-4dae-bf1b-45edde5de3d1" />

**Search where target is not found**

<img width="2403" height="1423" alt="image" src="https://github.com/user-attachments/assets/ee232cd5-c911-4207-981c-f613e087176c" />

### **Error / Invalid Input Handling**

**Entering an Invalid Integer**

<img width="2381" height="1206" alt="image" src="https://github.com/user-attachments/assets/a9ac5435-7204-4262-89ff-9fcc5f769d05" />

**No input Entered**

<img width="2375" height="1199" alt="image" src="https://github.com/user-attachments/assets/a70a96a7-64e7-4dde-9a48-69338f07ab43" />

**No List Generated Yet**

<img width="2383" height="1395" alt="image" src="https://github.com/user-attachments/assets/66f350a6-554c-4090-abba-47831032beaa" />

### **Pause/Resunt & Stop Controls**

**After Pressing Pause/Resume**

<img width="2428" height="1312" alt="image" src="https://github.com/user-attachments/assets/74996d51-885c-4014-bd2d-f39359474a30" />

*Pressing the button again will resume until completion*

**After Pressing Stop**

<img width="2383" height="1204" alt="image" src="https://github.com/user-attachments/assets/87e63bad-961f-4be3-818a-2b834e6ae580" />

### **Step Navigation**

https://github.com/user-attachments/assets/202b9ec8-e20e-40ab-9fc4-efcc06916b07

## **Full Walkthrough (No Errors)**

https://github.com/user-attachments/assets/69e205f4-391b-43f0-84e6-5e12c7871e47







**Hugging Face app link:**

https://huggingface.co/spaces/Lucas4man/CISC121-Project-Foreman-Lucas-LinSearch/blob/main/app.py

**AI disclaimers:**
All ChatGPT 5.1
* Helped with the addition of boxes and to resize the boxes as more are added
* Created templates for the css part

