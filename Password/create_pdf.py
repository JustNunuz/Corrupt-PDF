import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Define the folder name
folder_name = "Password"

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define the PDF file path
pdf_filename = os.path.join(folder_name, "Pycon_Namibia_Presentation.pdf")

# Create a canvas object
c = canvas.Canvas(pdf_filename, pagesize=A4)

# Set the font and size
c.setFont("Helvetica", 24)

# Define the text to be written
text = "Pycon Namibia Presentation"

# Draw the text on the PDF at position (x, y)
c.drawString(100, 750, text)

# Save the PDF
c.save()

print(f"PDF created successfully: {pdf_filename}")