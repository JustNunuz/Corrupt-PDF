from reportlab.pdfgen import canvas
import os
import random

def create_pdf(output_path):
    """Create a simple PDF file."""
    c = canvas.Canvas(output_path)
    c.drawString(100, 750, "This is a test PDF file.")
    c.drawString(100, 730, "We will corrupt this file intentionally.")
    c.save()
    print(f"PDF created and saved at: {output_path}")

def corrupt_pdf(input_path, output_path):
    """Corrupt a PDF by overwriting critical sections and appending malformed data."""
    try:
        # Read the original PDF
        with open(input_path, 'rb') as original_pdf:
            pdf_data = original_pdf.read()

        # Generate corruption payloads
        random_data = os.urandom(random.randint(100, 200))  # Larger random binary data for more disruption
        corrupt_metadata = b"\n%MalformedMetadata: Malicious Injection Here\n"
        fake_cross_reference = b"xref\n0 1\n0000000000 65535 f \ntrailer<<>>startxref\n999999\n%%EOF"
        
        # Construct corrupted PDF
        corrupted_data = (
            b"%PDF-1.5\n"  # Overwrite header with an invalid one
            + pdf_data[:len(pdf_data) // 2]  # Keep half of the original content
            + corrupt_metadata  # Insert malformed metadata
            + random_data  # Append random binary data
            + fake_cross_reference  # Overwrite xref and trailer sections
        )

        # Write the corrupted PDF to a new file
        with open(output_path, 'wb') as corrupted_pdf:
            corrupted_pdf.write(corrupted_data)
        
        print(f"Corrupted PDF saved at: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
original_pdf_path = "original.pdf"
corrupted_pdf_path = "corrupted.pdf"

# Create and corrupt the PDF
create_pdf(original_pdf_path)
corrupt_pdf(original_pdf_path, corrupted_pdf_path)
