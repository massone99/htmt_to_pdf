import os
import glob
from tkinter import filedialog

def select_html_files():
    # Open a file selection dialog and return the selected files
    return filedialog.askopenfilenames(filetypes=[('HTML Files', '*.html')])

def get_html_files(directory):
    # Get a list of all HTML files in the selected directory and return it
    return glob.glob(os.path.join(directory, '*.html'))

def delete_file_if_exists(file):
    # If the file exists, delete it
    if os.path.exists(file):
        os.remove(file)