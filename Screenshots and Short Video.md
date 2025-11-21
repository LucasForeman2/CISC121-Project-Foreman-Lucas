## **Final Gradio Code Testing:**
All zoomed out to see the full screen 

**Opening Screen**

**First thing you see:**

It should have:
* The title
* The steps/instructions you should take to use the program
* Sliders for list size and speed
* Text box to enter the target number
* Generate new list and run linear search buttons
* No list yet
* empty status/result
* next/previous step buttons, pause/resume button and stop button

<img width="2601" height="1430" alt="image" src="https://github.com/user-attachments/assets/847de5a5-2106-41b2-9671-747f5befd7c2" />

### **List Generation**

**Creating a normal sized list**
<img width="2425" height="1444" alt="image" src="https://github.com/user-attachments/assets/bac512a8-aa17-4083-a60e-2410da6067ca" />

The interface displays ten randomly generated values formatted as boxes with index labels. The status box confirms that a new list has been created and instructs the user to enter a target before running the search.

**Creating an Edge Case List**

List of 5:

<img width="2460" height="1418" alt="image" src="https://github.com/user-attachments/assets/21538537-81cc-4980-a4bb-e365849115e0" />

The visualization shows exactly five elements, and the box size automatically scales up for visibility. 

List of 100:

<img width="2401" height="1403" alt="image" src="https://github.com/user-attachments/assets/41c90f4f-28eb-4059-8950-56edca3de654" />

The list correctly generates 100 elements, wrapping across multiple rows with smaller boxes to fit on screen. The visualization remains readable.

### **Running the Search**

**Search where target is found**

<img width="2410" height="1329" alt="image" src="https://github.com/user-attachments/assets/602d11ea-b8bb-4dae-bf1b-45edde5de3d1" />

The found element is highlighted in green and the arrow is positioned on the correct index. The search log clearly documents each step and ends with a confirmation message indicating the index where the target was located.

**Search where target is not found**

<img width="2403" height="1423" alt="image" src="https://github.com/user-attachments/assets/ee232cd5-c911-4207-981c-f613e087176c" />

All elements up to the final index are marked as visited with dashed borders, and no cell is highlighted as found. The final log includes a “not found” notification.

### **Error / Invalid Input Handling**

**Entering an Invalid Integer/No Input**

<img width="2381" height="1206" alt="image" src="https://github.com/user-attachments/assets/a9ac5435-7204-4262-89ff-9fcc5f769d05" />

The user enters an invalid target value or doesn't enter an input at all. The application rejects the input and displays a message requesting a valid integer.

**No List Generated Yet**

<img width="2383" height="1395" alt="image" src="https://github.com/user-attachments/assets/66f350a6-554c-4090-abba-47831032beaa" />

The user attempts to run the search before generating a list. The system responds with a message instructing the user to create a list first.

### **Pause/Resume & Stop Controls**

**After Pressing Pause/Resume**

<img width="2428" height="1312" alt="image" src="https://github.com/user-attachments/assets/74996d51-885c-4014-bd2d-f39359474a30" />

*Pressing the button again will resume until completion*

The arrow is stopped on a specific index, and the search log shows partial progress. The animation remains frozen until the user resumes it.

**After Pressing Stop**

<img width="2383" height="1204" alt="image" src="https://github.com/user-attachments/assets/87e63bad-961f-4be3-818a-2b834e6ae580" />

The animation halts immediately, the visualization resets to its initial state (no arrows or highlights), and the log displays a message indicating that the search was stopped.

### **Step Navigation**

https://github.com/user-attachments/assets/202b9ec8-e20e-40ab-9fc4-efcc06916b07

After a completed search, the user can review recorded steps using the Previous and Next buttons.

## **Full Walkthrough (No Errors)**

https://github.com/user-attachments/assets/69e205f4-391b-43f0-84e6-5e12c7871e47
