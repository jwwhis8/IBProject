# Course Recomendations

## Introduction

This application allows for Student Recomendation sheets to be generated quickly, importing data from an Excel Sheet.

## Required Libraries

The application requires the following libraries:

- `pdfkit`: For creating PDFs from HTML.
- `PyPDF2`: Manipulates PDF files, including merging and splitting.
- `pandas`: Handles data, particularly useful for Excel files.
- `customtkinter`: Enhances UI with custom widgets for Tkinter.

Additionally, manual installation of `wkhtmltopdf` is required for `pdfkit`. Instructions are available [here](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf).

## Installation Guide

1.  Ensure Python (3.6 or later) is installed.
2.  Install the required libraries using the command:

        pip install pdfkit PyPDF2 pandas customtkinter reportlab

3.  Manually install `wkhtmltopdf` as described in the provided link. Once installed, add it as an enviroment variable, and restart your computer.

        https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf

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
