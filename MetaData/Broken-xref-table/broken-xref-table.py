from reportlab.pdfgen import canvas
import os

def create_pdf(output_path):
    """Create a simple PDF file."""
    c = canvas.Canvas(output_path)
    c.drawString(100, 750, "This is a test PDF file.")
    c.drawString(100, 730, "This file will have a broken cross-reference table.")
    c.save()
    print(f"PDF created and saved at: {output_path}")

def break_xref_table(input_path, output_path):
    """Corrupt the PDF by creating a broken cross-reference table."""
    try:
        # Read the original PDF
        with open(input_path, 'rb') as original_pdf:
            pdf_data = original_pdf.read()

        # Add corrupted xref table
        corrupted_xref = (
            b"xref\n"
            b"0 5\n"  # Declares 5 objects, but only provides invalid entries
            b"0000000000 65535 f \n"  # Free object entry (valid)
            b"0000000017 00000 n \n"  # Points to a valid byte offset
            b"9999999999 00000 n \n"  # Invalid byte offset
            b"0000000034 00000 n \n"  # Points to a non-existent object
            b"0000000048 00000 n \n"  # Random invalid offset
            b"trailer\n"
            b"<< /Size 5 /Root 1 0 R >>\n"  # Points to a non-existent root object
            b"startxref\n"
            b"999999\n"  # Invalid startxref
            b"%%EOF"
        )

        # Combine original PDF with the broken xref table
        corrupted_pdf_data = pdf_data + corrupted_xref

        # Write the corrupted PDF to a new file
        with open(output_path, 'wb') as corrupted_pdf:
            corrupted_pdf.write(corrupted_pdf_data)
        
        print(f"Corrupted PDF with broken xref table saved at: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
original_pdf_path = "original.pdf"
corrupted_pdf_path = "broken_xref.pdf"

# Create and corrupt the PDF
create_pdf(original_pdf_path)
break_xref_table(original_pdf_path, corrupted_pdf_path)