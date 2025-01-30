## Create_pdf.py

This file, create_pdf.py, creates a PDF in the password directory. The PDF file can have options for font, size, and other metadata such as the author, title, and subject.

1. **Creating a PDF Manually:**

   - When you create a PDF using software like Adobe Acrobat, Microsoft Word, or any other PDF creator, the software often includes metadata such as the author's name, the software used, and the creation date.
   - For example, if you create a PDF using Microsoft Word, the metadata might include your username (as configured in Word) and the software name (Microsoft Word).
2. **Creating a PDF Programmatically (e.g., using Python ReportLab):**

   - When you create a PDF using a library like ReportLab in Python, you have control over the metadata that is included. ReportLab allows you to set metadata fields such as the author, title, and subject.
   - Here’s an example of how you might set metadata in ReportLab:
     ```python
     from reportlab.lib.pagesizes import letter
     from reportlab.pdfgen import canvas

     def create_pdf(file_path):
         c = canvas.Canvas(file_path, pagesize=letter)
         c.setAuthor("Your Name")
         c.setTitle("Your Title")
         c.setSubject("Your Subject")
         c.drawString(100, 750, "Hello, World!")
         c.save()

     create_pdf("example.pdf")
     ```
   - In this example, the metadata fields for author, title, and subject are explicitly set.
3. **PDFs Created by Websites or Online Tools:**

   - When a website or online tool generates a PDF, the metadata might include information about the website or tool itself. For example, if a website converts a webpage to a PDF, the metadata might include the website's name or the tool used for the conversion.
   - If the website or tool does not explicitly set the metadata, it might default to the server's hostname or other identifiable information.
4. **Corrupted PDFs:**

   - If a PDF is corrupted, the metadata might still be present but could be incomplete or incorrect. The ability to read the metadata depends on the extent of the corruption.
   - Tools and libraries used to repair or analyze corrupted PDFs might capture and display whatever metadata is still readable.

In summary, the metadata in a PDF is determined by the software or tool used to create it. When creating PDFs programmatically, you have control over what metadata is included. If a PDF is corrupted, the metadata might still be captured, depending on the extent of the corruption.

## Password Protected PDF

Next, I used the `pdftk` [application](pdflabs.com/tools/pdftk-the-pdf-toolkit/](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/)) to password protect the PDF using the password 'open'.

After password protecting the PDF, we analyzed the file using the `analysis.py` script.

However, when we tried to open the password-protected PDF, it did not work. Why not?

### What Happens if You Try to Analyze an Encrypted PDF Without a Password?

1. **No Raw Data Access:** You won't be able to access the raw PDF structure (header, body, or trailer) because the file is encrypted.
2. **No Objects or Metadata:** The encryption prevents access to any objects, metadata, or content until the file is decrypted.

To successfully analyze or open the PDF, you need to provide the correct password to decrypt the file.

**To read or analyze a PDF file, it must first be opened** (i.e., loaded into memory). This is true for both `PyPDF2` and `pdfminer.six`. Let me break it down for you:

### 1. **Opening a PDF File**

When you open a PDF file in Python, you typically use a `with open(...)` statement to read the file in binary mode (`"rb"`). This loads the file into memory so that the library (`PyPDF2` or `pdfminer.six`) can process it.

#### Example:

```python
with open("example.pdf", "rb") as pdf_file:
    # Now the file is opened and can be processed
```

---

### 2. **What Happens When You Open a PDF?**

When you open a PDF file:

- The file is read from disk into memory.
- The library (e.g., `PyPDF2` or `pdfminer.six`) parses the file's structure (header, objects, trailer, etc.).
- If the file is **encrypted**, the library will detect this and raise an error unless you provide the correct password.

---

### 3. **Why Opening is Necessary**

PDF files are binary files with a complex structure. To analyze them, the library needs to:

- Parse the **header** (which contains the PDF version, e.g., `%PDF-1.7`).
- Read the **cross-reference table** (which maps object locations in the file).
- Extract **objects** (which contain the actual content, like text, images, and metadata).
- Read the **trailer** (which contains metadata and pointers to the root object).

All of this requires the file to be opened and loaded into memory.

### 4. **What Happens if the PDF is Encrypted?**

If the PDF is encrypted:

- The file can still be **opened** (i.e., loaded into memory).
- However, the library cannot **decrypt** or **parse** the content without the correct password.
- Attempting to analyze the file will result in an error (e.g., `PdfReadError` in `PyPDF2` or `PDFEncryptionError` in `pdfminer.six`).

### 5. **Example Code: Opening and Checking for Encryption**

Here’s an example of opening a PDF and checking if it’s encrypted:

```python
import PyPDF2

pdf_path = "Password/encrypted.pdf"  # Replace with the path to your PDF

try:
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
      
        # Check if the PDF is encrypted
        if reader.is_encrypted:
            print("The PDF is encrypted. Please provide the password.")
        else:
            print("The PDF is not encrypted. Analyzing...")
            # Proceed with analysis
except Exception as e:
    print(f"An error occurred: {e}")
```

---

### 6. **Decrypting and Analyzing an Encrypted PDF**

If the PDF is encrypted, you need to provide the password to decrypt it before analyzing it. Here’s how you can do it with `PyPDF2`:

```python
import PyPDF2

pdf_path = "Password/encrypted.pdf"  # Replace with the path to your PDF
password = "your_password"  # Replace with the actual password

try:
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
      
        # Check if the PDF is encrypted
        if reader.is_encrypted:
            # Attempt to decrypt the PDF
            if reader.decrypt(password):
                print("PDF decrypted successfully. Analyzing...")
                # Proceed with analysis
            else:
                print("Incorrect password. Unable to decrypt the PDF.")
        else:
            print("The PDF is not encrypted. Analyzing...")
            # Proceed with analysis
except Exception as e:
    print(f"An error occurred: {e}")
```

### 7. **Key Takeaways**

- **Opening the file is mandatory**: You must open the PDF file to analyze it.
- **Encryption prevents analysis**: If the PDF is encrypted, you cannot analyze it without the correct password.
- **Decryption is required**: Use the `decrypt()` method in `PyPDF2` to decrypt the file before analysis.
