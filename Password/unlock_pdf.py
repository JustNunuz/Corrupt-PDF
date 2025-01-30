import PyPDF2

# Define paths
input_pdf_path = "Password/locked_file.pdf"  # Path to the encrypted PDF
output_txt_path = "Password/pdf_analysis.txt"  # Path to save the analysis
password = "open"  # Replace with the actual password

# Function to write PDF metadata, header, trailer, and body to a file
def analyze_pdf(reader, output_file):
    # Write metadata
    output_file.write("--- PDF Metadata ---\n")
    metadata = reader.metadata
    if metadata:
        for key, value in metadata.items():
            output_file.write(f"{key}: {value}\n")
    else:
        output_file.write("No metadata found.\n")

    # Write header
    output_file.write("\n--- PDF Header ---\n")
    output_file.write(f"PDF Version: {reader.pdf_header}\n")

    # Write trailer
    output_file.write("\n--- PDF Trailer ---\n")
    trailer = reader.trailer
    if trailer:
        for key, value in trailer.items():
            output_file.write(f"{key}: {value}\n")
    else:
        output_file.write("No trailer found.\n")

    # Write body (pages)
    output_file.write("\n--- PDF Body (Pages) ---\n")
    for page_num, page in enumerate(reader.pages, start=1):
        output_file.write(f"\nPage {page_num}:\n")
        output_file.write(page.extract_text() + "\n")

# Main script
try:
    # Open the PDF file
    with open(input_pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        # Check if the PDF is encrypted
        if reader.is_encrypted:
            print("PDF is encrypted. Attempting to decrypt...")
            if reader.decrypt(password):
                print("PDF decrypted successfully.")
            else:
                print("Incorrect password. Unable to decrypt the PDF.")
                exit()

        # Analyze the PDF and write results to a file
        with open(output_txt_path, "w", encoding="utf-8") as output_file:
            analyze_pdf(reader, output_file)
        
        print(f"PDF analysis saved to: {output_txt_path}")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Script execution finished.")