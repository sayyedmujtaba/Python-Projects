from tkinter import Label, Tk
import time

app = Tk() # create main window
app.title("🕒 Digital Clock")  # Displays app name
app.geometry("300x100")  #set window size
# app.resizable(False, False)  # disable resizing
app.configure(bg="black") 

clock_label = Label(app, bg="black", fg="cyan", font=("Helvetica", 40), relief="flat")
clock_label.place(x=20, y=20)

def update_time():
    current_time = time.strftime("%H:%M:%S") # get current time as HH:MM:SS 
    clock_label.config(text=current_time) # update label text
    clock_label.after(1000, update_time) # Schedules Tkinter to call update_time again after 1000 ms (1 second).
    # This creates a loop without blocking the GUI.
    # Without after(), the label would only update once and then freeze.

update_time()  # initial call to start the time updates
app.mainloop() # start the Tkinter event loop (run the app)