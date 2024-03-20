import pdfkit
import os
from PyPDF2 import PdfWriter, PdfReader
import GetSheet
from PageText import getPageText

def create_individual_pdf(name, courses, year, filename):
    # Use your getPageText function to generate HTML content for each student
    html_content = getPageText(name, courses, year)
    # Generate a PDF from this HTML content
    pdfkit.from_string(html_content, filename)

def create_and_combine_pdfs(output_pdf, sheet_path, year):
    GetSheet.getSheet(sheet_path)  
    pdf_writer = PdfWriter()

    for x in range(GetSheet.NumberOfStudents):
        filename = f"{GetSheet.getName(x)}.pdf"
        create_individual_pdf(GetSheet.getName(x), GetSheet.getCourses(x), year, filename)

        with open(filename, 'rb') as fileobj:
            pdf_reader = PdfReader(fileobj)
            for page in pdf_reader.pages:
               pdf_writer.add_page(page)
                
        os.remove(filename)

    # Write out the combined PDF
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

