import tkinter as tk
from tkinter.filedialog import askopenfilename
import createPDF

def browse():
    global f_path
    f_path = askopenfilename(initialdir="/",
        title="Select File", filetypes=(("Excel files","*.xlsx*"),("All Files","*.*")))
    file_explorer.configure(text="File Opened: " + f_path)

def generate():
    input_value = entry.get()  # Get the current text in entry
    createPDF.createPDF(f_path, input_value)

def runWindow():
    root = tk.Tk()
    root.title("File Explorer")
    root.geometry("950x1000")
    root.config(background="white")

    # Create an File Explorer widget
    global file_explorer
    file_explorer = tk.Label(root, text="First Select your Spreadsheet",
        font=("Verdana", 13, "bold"),
        width=100,
        height=4, fg="white", bg="gray")

    # Create an Browse widget
    browseButton = tk.Button(root, text="Browse Folder", font=("Roboto", 14),
        command=browse)
    
    # Create a Label widget
    label = tk.Label(root, text="Year: (Format: \"20XX-20XX\"):")

    # Create an Entry widget
    global entry
    entry = tk.Entry(root, width=20)

    # Create an Generate widget
    generateButton = tk.Button(root, text="Generate PDF", font=("Roboto", 14),
        command=generate)

    file_explorer.pack()
    browseButton.pack(pady=10)
    label.pack(pady=5)
    entry.pack(pady=10)
    generateButton.pack(pady=10)

    root.mainloop()