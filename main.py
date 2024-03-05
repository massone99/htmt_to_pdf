import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from file_operations import select_html_files
from pdf_conversion import convert_all_html_to_pdf

def create_gui():
    global root
    # Create a Tkinter root widget
    root = tk.Tk()

    # Set the title of the window
    root.title("HTML to PDF Converter")

    # Create a button that starts the conversion process when clicked
    convert_button = tk.Button(root, text="Convert HTML to PDF", command=lambda: convert_all_html_to_pdf(progress, options_entry, select_html_files, root))
    convert_button.pack(pady=10)

    # Create a progress bar
    progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
    progress.pack(pady=10)

    # Create an entry field for the wkhtmltopdf options
    options_entry = tk.Entry(root, width=50)
    options_entry.pack(pady=10)
    options_entry.insert(0, '--page-size A4 --orientation Portrait')  # Default options

    # Start the Tkinter event loop
    root.mainloop()

# Run the GUI
create_gui()