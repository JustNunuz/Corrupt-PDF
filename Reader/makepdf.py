from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf_with_lorem(file_name):
    # Create a canvas object
    c = canvas.Canvas(file_name, pagesize=letter)

    # Page 1: Title Page
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, 750, "Hello, ReportLab!")
    c.setFont("Helvetica", 14)
    c.drawString(100, 720, "This is a simple PDF created using Python and ReportLab.")
    c.drawString(100, 700, "You can customize the content, layout, and style.")
    c.setFillColorRGB(0.8, 0.9, 0.8)
    c.rect(80, 680, 400, 50, fill=1)
    c.line(80, 675, 480, 675)
    c.showPage()  # End of page 1

    # Page 2: Lorem Ipsum Page
    lorem_text = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, "
        "vitae scelerisque enim ligula venenatis dolor. Maecenas nisl est, "
        "ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. "
        "Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac."
    )
    c.setFont("Times-Roman", 12)
    c.drawString(100, 750, "Page 2: Lorem Ipsum")
    text_object = c.beginText(100, 730)
    text_object.setFont("Times-Roman", 12)
    text_object.setTextOrigin(100, 730)  # Start writing text
    for _ in range(5):  # Repeat text to fill some space
        text_object.textLines(lorem_text)
    c.drawText(text_object)
    c.showPage()  # End of page 2

    # Page 3: More Lorem Ipsum
    c.setFont("Times-Italic", 12)
    c.drawString(100, 750, "Page 3: More Lorem Ipsum")
    text_object = c.beginText(100, 730)
    for _ in range(7):  # Add more Lorem Ipsum
        text_object.textLines(lorem_text)
    c.drawText(text_object)
    c.showPage()  # End of page 3

    # Save the PDF
    c.save()

# Create the PDF
create_pdf_with_lorem("test_pdf.pdf")
