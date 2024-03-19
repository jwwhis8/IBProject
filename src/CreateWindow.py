import customtkinter as tk
from tkinter.filedialog import askopenfilename
import CreatePDF

class App(tk.CTk):
    
    def browse(self):
        global f_path
        f_path = askopenfilename(initialdir="~",
            title="Select File", filetypes=(("Excel files","*.xlsx*"),("All Files","*.*")))
        self.file_explorer.configure(text="File Opened: " + f_path)

    def generate(self):
        CreatePDF.createPDF(f_path, self.yearEntry.get())

    def __init__(self):
        super().__init__()
        tk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        tk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
        
        self.title("Create Recomendations")
        self.geometry("500x500")

        self.grid_columnconfigure(0, weight=1)  # configure grid system
        self.grid_rowconfigure(0, weight=5)  # configure grid system
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure(2, weight=3)
        self.grid_rowconfigure(3, weight=3)

        xpad = 25
        ypad = 10

        # Title
        self.titleLabel = tk.CTkLabel(master=self, text="Create Course Recomendations!", font=("helvetica", 26))
        self.titleLabel.grid(row=0, column=0, padx=xpad, pady=ypad, sticky="nswe")

        # File Explorer Frame
        self.fileExplorerFrame = tk.CTkFrame(master=self)
        self.fileExplorerFrame.grid(row=1, column=0, padx=50, pady=ypad, sticky="nswe")

        self.file_explorer = tk.CTkLabel(master=self.fileExplorerFrame, text="First Select your Spreadsheet",
            font=("helvetica", 20))
        self.file_explorer.pack(padx=xpad, pady=ypad, anchor="center")

        self.browseButton = tk.CTkButton(master=self.fileExplorerFrame, text="Browse Folder", font=("helvetica", 14), command=self.browse)
        self.browseButton.pack(padx=xpad, pady=ypad, anchor="center")
        
        # Year Frame
        self.yearFrame = tk.CTkFrame(master=self)
        self.yearFrame.grid(row=2, column=0, padx=50, pady=ypad, sticky="nswe")

        self.yearFormatLabel = tk.CTkLabel(master=self.yearFrame, text="Year: (Format: \"20XX-20XX\"):", font=("helvetica", 20))
        self.yearFormatLabel.pack(padx=xpad, pady=ypad, anchor="center")

        self.yearEntry = tk.CTkEntry(master=self.yearFrame, width=20, font=("helvetica", 14))
        self.yearEntry.pack(padx=xpad, pady=ypad, anchor="center", fill="x")

        # Generate Button
        self.generateButton = tk.CTkButton(master=self, text="Generate PDF", font=("helvetica", 14), command=self.generate)
        self.generateButton.grid(row=3, column=0, padx=120, pady=(10, 30), sticky="nswe")

if __name__ == "__main__":
    app = App()
    app.mainloop()
    