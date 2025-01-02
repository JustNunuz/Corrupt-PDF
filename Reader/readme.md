# About

This folder contains two Python scripts that work together to create a PDF viewer application. The main script, `PDFViewer.py`, provides a graphical user interface (GUI) using Tkinter, allowing users to open, navigate, and view PDF documents. It includes features such as navigation buttons, scrollbars, and theme switching (light/dark mode). The second script, `PDFMiner.py`, handles the backend operations for loading and manipulating PDF files using the PyMuPDF library. It retrieves metadata, extracts text, and manages zoom levels. Additionally, the application includes icons for the file and navigation buttons, enhancing the user experience. A demo PDF file is provided for testing the functionality of the viewer.

# How to Run the Application

1. **Navigate to the Directory**:
   Ensure you are inside the `reader` directory where the scripts and demo file are located.

2. **Run the Code**:
   You can run the application using the following command in your terminal:
   ```python
   python3 pdfviewer.py
   ```
   Alternatively, you can open the `pdfviewer.py` file in a code editor and press the run button.

3. **Open a PDF File**:
   Once the application is running, use the file menu to open the PDF file you want to view. You can try using the provided `test_pdf.pdf` file for testing.

# Detailed Code Execution

### 1. **PDFViewer (Main Application)**

The `PDFViewer` class is the main application that provides a graphical user interface (GUI) for viewing PDF files. It uses the Tkinter library to create the GUI components.

#### Key Components:

- **Initialization**: Sets up the main window, menus, and frames.
- **Menu Bar**: Includes options for opening files, exiting the application, switching themes (light/dark mode), and zooming in/out.
- **Canvas**: Displays the PDF pages.
- **Scrollbars**: Allow vertical and horizontal scrolling of the PDF content.
- **Navigation Buttons**: Buttons for navigating to the previous and next pages.
- **Page Label**: Displays the current page number and the total number of pages.

#### Key Methods:

- **`open_file`**: Opens a file dialog to select a PDF file and initializes the `PDFMiner` instance to load the PDF.
- **`display_page`**: Displays the current page of the PDF on the canvas.
- **`previous_page` and `next_page`**: Navigate to the previous and next pages, respectively.
- **`set_light_mode` and `set_dark_mode`**: Switch between light and dark modes.
- **`zoom_in` and `zoom_out`**: Zoom in and out of the PDF content.

### 2. **PDFMiner Class (PDF Handling)**

The `PDFMiner` class handles the loading and manipulation of PDF files using the `fitz` (PyMuPDF) library.

#### Key Components:

- **Initialization**: Opens the PDF file and loads the first page.
- **Zoom Dictionary**: Defines zoom levels based on the width of the PDF page.

#### Key Methods:

- **`get_metadata`**: Retrieves metadata from the PDF, such as the author, document name, and number of pages.
- **`get_page`**: Loads a specific page of the PDF and returns it as an image.
- **`get_text`**: Extracts text from a specific page of the PDF.
- **`zoom_in` and `zoom_out`**: Adjust the zoom level of the PDF content.

### Workflow:

1. **Initialization**:

   - The `PDFViewer` class initializes the main window and sets up the GUI components.
   - The `PDFMiner` class is initialized when a PDF file is opened.

2. **Opening a PDF File**:

   - The user selects a PDF file through the file dialog.
   - The `PDFMiner` instance is created with the selected file path.
   - Metadata and the number of pages are retrieved and stored.

3. **Displaying Pages**:

   - The `display_page` method of `PDFViewer` calls the `get_page` method of `PDFMiner` to load and display the current page on the canvas.
   - The user can navigate through the pages using the navigation buttons or scrollbars.

4. **Zooming**:

   - The user can zoom in and out using the zoom menu options.
   - The `zoom_in` and `zoom_out` methods of `PDFMiner` adjust the zoom level, and the `display_page` method updates the canvas with the zoomed content.

5. **Themes**:
   - The user can switch between light and dark modes using the theme menu options.
   - The `set_light_mode` and `set_dark_mode` methods of `PDFViewer` update the background colors of the main window and canvas.

### Summary:

The `PDFViewer` class provides the GUI for the PDF viewer application, while the `PDFMiner` class handles the backend operations related to PDF loading and manipulation. Together, they create a functional PDF viewer that allows users to open, navigate, zoom, and view PDF files with different themes.
