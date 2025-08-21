# 📝 To-Do List (CLI)

A simple **Command-Line To-Do List Application** built with Python.  
It allows you to **add, view, and delete tasks** directly from the terminal with colored outputs for better readability.  

---

## 🚀 Features
- Show tasks with numbering  
- Add tasks  
- Delete tasks by number  
- Colored outputs using `termcolor`  
- Lightweight and beginner-friendly  

---

## 📦 Requirements
- Python 3.x  
- `termcolor` library  

Install the dependency with:
```bash
pip install termcolor
```

---

## ▶️ Usage
Run the script in your terminal:
```bash
python todo.py
```

You’ll see:
```
=== To-Do List ===
1. Show tasks
2. Add task
3. Delete task
4. Quit
```

### Example Workflow:
- Choose **2** → Add a new task  
- Choose **1** → Show current tasks  
- Choose **3** → Delete a task by entering its number  
- Choose **4** → Exit the program  

---

## 📸 Demo
```bash
=== To-Do List ===
1. Show tasks
2. Add task
3. Delete task
4. Quit
Choose an option (1-4): 2
Enter a task: Learn Python
Task "Learn Python" added to to_do list

Choose an option (1-4): 1
1. Learn Python
```

---

## 🛠 Future Improvements
- Mark tasks as **completed** ✅  
- Save tasks to a **file/database** for persistence  
- Add **due dates / priorities**  
- Search and filter tasks  
