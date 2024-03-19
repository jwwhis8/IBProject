import pdfkit
import GetSheet
import PyPDF2
import os
import PageText

def getFilename(x):
   return "Students/" + GetSheet.getName(x) + ".pdf"

def combine_pdfs_in_folder(folder_path, output_pdf):
    pdf_writer = PyPDF2.PdfWriter()

    # List all files in the folder, sort them, and filter out non-PDF files
    pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf')])

    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        
        # Using context manager for opening files
        with open(pdf_path, 'rb') as fileobj:
            try:
                pdf_reader = PyPDF2.PdfReader(fileobj)
                
                # Add each page of the PDF to the writer
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
            except PyPDF2.utils.PdfReadError as e:
                print(f"Error reading {pdf_path}: {e}")

    # Write out the combined PDF
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

def createPDF(path, year_value):
  # Initialize the thing
  GetSheet.getSheet(path)  

  year = year_value

  if not os.path.exists("Students"):
    # If it does not exist, create it
    os.makedirs("Students")

  for x in range(GetSheet.df.shape[1]):
    pdfkit.from_string(PageText.getPageText(GetSheet.getName(x), GetSheet.getCourses(x), year), getFilename(x))

  folder = '/'  # Replace with the path to your folder containing PDFs
  output_file = 'Recommendations.pdf'  # Output file name
  combine_pdfs_in_folder(folder, output_file)
