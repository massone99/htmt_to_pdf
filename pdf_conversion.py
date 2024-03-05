import os
import subprocess
import shlex
from file_operations import delete_file_if_exists

def convert_html_to_pdf(html_file, pdf_file, options):
    # Define the path to the wkhtmltopdf executable
    path_wkhtmltopdf = 'wkhtmltopdf/bin/wkhtmltopdf.exe'  # Replace with your actual path

    # Convert the HTML file to a PDF
    subprocess.run([path_wkhtmltopdf] + options + [html_file, pdf_file])

from tkinter import messagebox

def convert_all_html_to_pdf(progress, options_entry, select_html_files, root):
    html_files = select_html_files()

    # Parse the options from the entry field
    options = shlex.split(options_entry.get())

    for i, html_file in enumerate(html_files):
        pdf_file = os.path.splitext(html_file)[0] + '.pdf'
        delete_file_if_exists(pdf_file)
        convert_html_to_pdf(html_file, pdf_file, options)
        print(f'Conversion completed. The PDF file is available at: {pdf_file}')

        # Update the progress bar
        progress['value'] = (i + 1) / len(html_files) * 100
        root.update_idletasks()

    # Show a notification when all conversions are completed
    messagebox.showinfo("Conversion Completed", "All HTML files have been converted to PDF.")