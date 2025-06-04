📌 Project Overview
I created this simple terminal-based ordering system for a restaurant using Python. The purpose of the program is to simulate a basic interaction where a user can view the menu, place orders, and receive a running bill until they finish ordering. It helps users understand how loops, conditionals, dictionaries, and user input work together in a real-world example.
The idea is to allow users to select items from a pre-defined menu and calculate the total bill based on their orders.

💻 Coding Method & Purpose
Dictionary (dict): Used to store the menu items and their prices in key-value pairs.
Functions: display_menu() is used to print the menu in a reusable and clean way.
Loops (while True): To keep asking the user for more orders until they choose to stop.
Conditionals (if-else): To check if the ordered item exists in the menu and respond appropriately.
String Methods (.title(), .strip(), .lower()): For input normalization to avoid mismatch issues.
termcolor Library: Used to add colored text to improve the interface and make the experience more engaging.

🌈 Termcolor Styling
To improve user experience in the terminal, I used the termcolor module to display prompts and messages in color

✨ All Available Options in termcolor:
🎨 Text Colors:
'grey'
'red'
'green'
'yellow'
'blue'
'magenta'
'cyan'
'white'
🎨 Background Colors (prefix with on_):
'on_grey'
'on_red'
'on_green'
'on_yellow'
'on_blue'
'on_magenta'
'on_cyan'
'on_white'
✏️ Text Attributes:
'bold'
'dark'
'underline'
'blink'
'reverse'
'concealed'

✅ Key Learnings
Practical use of loops and conditionals
Basic user interaction and input validation
Formatting and styling terminal output with termcolor
Managing simple state (like total_bill) during a loop