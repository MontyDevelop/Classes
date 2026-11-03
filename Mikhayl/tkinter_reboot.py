import tkinter as mikhayl

# Create the main window
root = mikhayl.Tk()

# Set title and size
root.title("My First Tkinter App")
root.geometry("300x200")


entry1 = mikhayl.Entry(root)
entry1.pack()

label = mikhayl.Label(root, text="Hello, Tkinter!")
label.pack()  # Add it to the window




# Start the GUI loop
root.mainloop()