from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1

# Define the path to the PDF file
pdf_path = "Password/Locked_file.pdf"  # Locked file will cause and error
#pdf_path = "Password/Pycon_namibia.pdf"  # Not locked file will not cause problems

# Open the PDF file in binary read mode
with open(pdf_path, "rb") as pdf_file:
    # Create a PDF parser object
    parser = PDFParser(pdf_file)
    # Create a PDF document object
    document = PDFDocument(parser)

    # Print the PDF header
    print("--- PDF Header ---")
    print(pdf_file.read(8).decode("utf-8"))  # PDF files start with "%PDF-1.x"

    # Print the PDF trailer
    print("\n--- PDF Trailer ---")
    trailer = resolve1(document.catalog)
    print(trailer)

    # Print all objects in the PDF
    print("\n--- PDF Objects ---")
    for xref in document.xrefs:
        for obj_id in xref.get_objids():
            obj = resolve1(document.getobj(obj_id))
            print(f"Object ID: {obj_id}, Object: {obj}")