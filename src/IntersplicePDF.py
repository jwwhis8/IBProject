import PyPDF2

def insert_between_pages(base_pdf_path, insert_pdf_path, output_pdf_path):
    # Open the base PDF with PdfReader
    base_pdf = PyPDF2.PdfReader(open(base_pdf_path, 'rb'))
    # Open the PDF to insert the single page from with PdfReader
    insert_pdf = PyPDF2.PdfReader(open(insert_pdf_path, 'rb'))
    # Make sure the insert PDF has at least one page
    if len(insert_pdf.pages) == 0:
        print("The insert PDF does not contain any pages.")
        return
    # Get the single page to be inserted
    insert_page = insert_pdf.pages[0]
    # Create a PDF writer for the output PDF using PdfWriter
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through the base PDF and insert the single page after each page
    for page_num in range(len(base_pdf.pages)):
        # Add the current page from the base PDF
        pdf_writer.add_page(base_pdf.pages[page_num])
        # Add the single insert page after the current page
        pdf_writer.add_page(insert_page)

    # Save the output PDF
    with open(output_pdf_path, 'wb') as out:
        pdf_writer.write(out)

    print(f"PDF created successfully: {output_pdf_path}")
