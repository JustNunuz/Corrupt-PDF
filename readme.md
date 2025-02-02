```

 ██████╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗██████╗ ████████╗    ██████╗ ██████╗ ███████╗
██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║   ██║██╔══██╗╚══██╔══╝    ██╔══██╗██╔══██╗██╔════╝
██║     ██║   ██║██████╔╝██████╔╝██║   ██║██████╔╝   ██║       ██████╔╝██║  ██║█████╗  
██║     ██║   ██║██╔══██╗██╔══██╗██║   ██║██╔═══╝    ██║       ██╔═══╝ ██║  ██║██╔══╝  
╚██████╗╚██████╔╝██║  ██║██║  ██║╚██████╔╝██║        ██║       ██║     ██████╔╝██║     
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝        ╚═╝       ╚═╝     ╚═════╝ ╚═╝     
                                                                                       

```

![Corrupt PDF Example](/assets/pdf.jpeg)
This repo provides a Python-based demonstration of techniques to intentionally corrupt PDF files, highlighting the security vulnerabilities and risks associated with handling and manipulating PDF documents. It emphasizes the critical issues of data integrity and document security, shedding light on how easily PDFs can be exploited.

## Presentation for PyCon Zim 2024

In the session, I dive into how PDFs can be manipulated, the hidden threats they present, and how they can be weaponized to deliver malware or exploit vulnerabilities within PDF readers. I also demonstrate forensic techniques to detect and analyze these attacks, with a focus on identifying tampered documents, extracting malicious payloads, and understanding the structural complexities that make PDFs both powerful and prone to abuse.

Wanna check out my slides: [[Click here](https://docs.google.com/presentation/d/1KyZD8nERr0gxEnAmliuy8Oh4MUje14a6vduAhqwfCMA/edit?usp=sharing)]

## Presentation for PyCon Namibia 2025
Building up upon the content from the last time I gave this talk, I added a Python-based PDF reader to open PDFs. I will also add a feature to test for removing a password from a protected PDF in two ways: Brute force and remvoing the portion of code.

## Disclaimer

This repository is intended for educational and research purposes only. It explores techniques for manipulating PDFs, identifying potential vulnerabilities, and demonstrating how these can be achieved using Python. The goal is to reveal and understand how PDF files can be altered or corrupted, with a particular focus on testing PDF viewers' handling of embedded JavaScript and other manipulations.

This is not an endorsement or encouragement for malicious use. The techniques demonstrated here should never be used on files intended for distribution or in any way that could harm or disrupt systems, users, or data. Unauthorized use of these methods outside of a controlled, research-focused environment is strictly discouraged and may be illegal.

By using this repository, you agree to take full responsibility for any actions you take based on this information. Always use these techniques responsibly and within the bounds of applicable laws and ethical guidelines.
