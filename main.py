import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import subprocess
import glob

def select_directory():
    # Open a directory selection dialog and return the selected directory
    return filedialog.askdirectory()

def get_html_files(directory):
    # Get a list of all HTML files in the selected directory and return it
    return glob.glob(os.path.join(directory, '*.html'))

def delete_file_if_exists(file):
    # If the file exists, delete it
    if os.path.exists(file):
        os.remove(file)

def convert_html_to_pdf(html_file, pdf_file):
    # Define the path to the wkhtmltopdf executable
    path_wkhtmltopdf = 'wkhtmltopdf/bin/wkhtmltopdf.exe'  # Replace with your actual path

    # Convert the HTML file to a PDF
    subprocess.run([path_wkhtmltopdf]  + [html_file, pdf_file])

def convert_all_html_to_pdf(progress):
    directory = select_directory()
    html_files = get_html_files(directory)

    for i, html_file in enumerate(html_files):
        pdf_file = os.path.splitext(html_file)[0] + '.pdf'
        delete_file_if_exists(pdf_file)
        convert_html_to_pdf(html_file, pdf_file)
        print(f'Conversion completed. The PDF file is available at: {pdf_file}')

        # Update the progress bar
        progress['value'] = (i + 1) / len(html_files) * 100
        root.update_idletasks()

    # Notify the user when all conversions are finished
    messagebox.showinfo("Information", "All conversions completed.")

def create_gui():
    global root
    # Create a Tkinter root widget
    root = tk.Tk()

    # Set the title of the window
    root.title("HTML to PDF Converter")

    # Create a button that starts the conversion process when clicked
    convert_button = tk.Button(root, text="Convert HTML to PDF", command=lambda: convert_all_html_to_pdf(progress))
    convert_button.pack(pady=10)

    # Create a progress bar
    progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
    progress.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

# Run the GUI
create_gui()