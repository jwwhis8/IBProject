# Course Recomendations

## Introduction

This application allows for Student Recomendation sheets to be generated quickly, importing data from an Excel Sheet.

## Quick-Start Guide

1.  Clone or Download the repository, and extract the data.
2.  Navigate to the folder and run the "Application" shortcut
3.  Select the Excel file and the back-page PDF.
4.  Enter the year and the number of students to generate for.
5.  Click Generate
6.  The PDF should be located in the folder, and can then be printed.

## Required Libraries

These are only required if the application is being run through Python directly, rather than through the compiled EXE file.

The application requires the following libraries:

- `pdfkit`: For creating PDFs from HTML.
- `PyPDF2`: Manipulates PDF files, including merging and splitting.
- `pandas`: Handles data, particularly useful for Excel files.
- `customtkinter`: Enhances UI with custom widgets for Tkinter.

Additionally, manual installation of `wkhtmltopdf` is required for `pdfkit`. Instructions are available [here](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf).

## File by File

- `CreatePDF.py`: Generates a PDF from HTML content. Modify the HTML within the script as needed.
- `IntersplicePDF.py`: Merges multiple PDF files into one. Specify the PDF files to be merged in the script.
- `PageText.py`: Extracts text from a specified page in a PDF file. Set the PDF file and page number in the script.
- `GetSheet.py`: Reads and processes data from an Excel file, useful for generating reports or data summaries.
- `CreateWindow.py`: Offers a GUI for interacting with the application's functionalities, powered by `customtkinter`.

## How It Works

- **PDF Creation and Manipulation**: `pdfkit` uses `wkhtmltopdf` for converting HTML to PDF, while `PyPDF2` is utilized for merging PDF documents, offering straightforward document combination.
- **Data Handling**: `pandas` is key for reading and manipulating data from Excel files, enabling efficient data processing for reporting or analysis.
- **User Interface**: `customtkinter` provides an enhanced UI experience, particularly seen in `CreateWindow.py`, through modern and custom Tkinter widgets.
