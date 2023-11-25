import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *

def show_help():
    help_text = """
    Welcome to the File Organizer!

    To Organize Files:
    1. Click 'Organize Files'.
    2. Select the folder you want to organize.
    3. Files will be sorted by their types.

    To Reorganize Files:
    1. Click 'Reorganize Files'.
    2. Select the folder to revert the organization.
    """
    # Create a new window for displaying help
    help_window = tk.Toplevel()
    help_window.title("Instruction Manual")

    # Display the help text in a label
    help_label = tk.Label(help_window, text=help_text, padx=20, pady=20)
    help_label.pack()

    img = tk.PhotoImage(file=r"C:\Users\aribz\OneDrive\Desktop\file_organizer\File-Organizer\5726775.png")
    help_window.iconphoto(False, img)


def update_history_label(folder_path, operation):
    history_text = history_label.cget("text")
    history_text += f"\n{operation.capitalize()} folder: {folder_path}"
    history_label.config(text=history_text)


def organize_files():
    source_folder = filedialog.askdirectory(title="Select Folder to Organize")
    if source_folder:
        for filename in os.listdir(source_folder):
            file_path = os.path.join(source_folder, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1][1:]
                if not os.path.exists(os.path.join(source_folder, file_extension)):
                    os.makedirs(os.path.join(source_folder, file_extension))
                shutil.move(file_path, os.path.join(source_folder, file_extension, filename))
        messagebox.showinfo("Success", "Files organized successfully!")
        update_history_label(source_folder, "organized")


def reorganize_files():
    source_folder = filedialog.askdirectory(title="Select Folder to Reorganize")
    if source_folder:
        for root_folder, _, files in os.walk(source_folder):
            for filename in files:
                file_path = os.path.join(root_folder, filename)
                shutil.move(file_path, os.path.join(source_folder, filename))
        messagebox.showinfo("Success", "Files reorganized successfully!")
        update_history_label(source_folder, "reorganized")


def create_icon_labels(files, frame):
    for file in files:
        icon = tk.PhotoImage(file="icon_path_here") 
        label = tk.Label(frame, image=icon)
        label.image = icon  # Keep a reference to the image to avoid garbage collection
        label.pack()


root = tk.Tk()
root.title("File Organizer")
root.geometry("800x600")
root.resizable(False, False)

# HEADER
header_label = tk.Label(root, text="Welcome to File Organizer", font=("Segoe UI Black", 20), pady=10)
header_label.pack()

# ICON
img = tk.PhotoImage(file=r'C:\Users\aribz\OneDrive\Desktop\file_organizer\File-Organizer\3767084.png')
root.iconphoto(False, img)

# FRAME FOR BUTTONS
button_frame = tk.Frame(root, bg="white")
button_frame.pack(side="left", fill="y")

# BUTTONS
organize_button = tk.Button(button_frame, text="Organize Files", command=organize_files)
organize_button.pack(padx=10, pady=5, fill="x")

reorganize_button = tk.Button(button_frame, text="Reorganize Files", command=reorganize_files)
reorganize_button.pack(padx=10, pady=5, fill="x")

help_button = tk.Button(button_frame, text="Help", command=show_help)
help_button.pack(padx=10, pady=5, fill="x")

# FRAME FOR HISTORY AND COPYRIGHT
history_and_copyright_frame = tk.Frame(root)
history_and_copyright_frame.pack(side="right", fill="both", expand=True)

# HISTORY 
history_frame = tk.Frame(history_and_copyright_frame, bg="light gray")
history_frame.pack(fill="both", expand=True)

history_label = tk.Label(history_frame, text="History of Organized/Reorganized Files", font=("Arial", 12), bg="light gray")
history_label.pack(padx=20, pady=5)

# COPYRIGHT
bottom_frame = tk.Frame(history_and_copyright_frame, bg="white")
bottom_frame.pack(side="bottom", fill="x")

copyright_label = tk.Label(bottom_frame, text="© 2023 Atabek Aribzhanov", font=("Century Gothic", 12), bg="white")
copyright_label.pack(side="left", padx=190)

# -
root.mainloop()
