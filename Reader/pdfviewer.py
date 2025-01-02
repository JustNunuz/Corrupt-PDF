import os
from tkinter import *
from tkinter import ttk
# importing the PDFMiner class from the miner file
from miner import PDFMiner
from tkinter import filedialog as fd


class PDFViewer:
    
    def __init__(self, master):
        self.master = master
        # creating the window
        self.master = master
        # gives title to the main window
        self.master.title('PDF Viewer')
        # gives dimensions to main window
        self.master.geometry('580x520+440+180')
        # this disables the minimize/maximize button on the main window
        self.master.resizable(width = 0, height = 0)
        # loads the icon and adds it to the main window
        icon_path = os.path.join(os.path.dirname(__file__), 'pdf_file_icon.ico')
        self.master.iconbitmap(icon_path)
        # Initialize the PDF viewer here
        # For example, you can add a canvas or frame to display the PDF content

        # path for the pdf doc
        self.path = None
        # state of the pdf doc, open or closed
        self.fileisopen = None
        # author of the pdf doc
        self.author = None
        # name for the pdf doc
        self.name = None
        # the current page for the pdf
        self.current_page = 0
        # total number of pages for the pdf doc
        self.numPages = None

        # creating the menu
        self.menu = Menu(self.master)
        # adding it to the main window
        self.master.config(menu=self.menu)
        # creating a sub menu
        self.filemenu = Menu(self.menu)
        # giving the sub menu a label
        self.menu.add_cascade(label="File", menu=self.filemenu)
        # adding two buttons to the sub menus
        self.filemenu.add_command(label="Open File", command=self.open_file)
        self.filemenu.add_command(label="Exit", command=self.master.destroy)
                # creating the top frame
        self.top_frame = ttk.Frame(self.master, width=580, height=460)
        # placing the frame using inside main window using grid()
        self.top_frame.grid(row=0, column=0)
        # the frame will not propagate
        self.top_frame.grid_propagate(False)
        # creating the bottom frame
        self.bottom_frame = ttk.Frame(self.master, width=580, height=50)
        # placing the frame using inside main window using grid()
        self.bottom_frame.grid(row=1, column=0)
        # the frame will not propagate
        self.bottom_frame.grid_propagate(False)

                # creating a vertical scrollbar
        self.scrolly = Scrollbar(self.top_frame, orient=VERTICAL)
        # adding the scrollbar
        self.scrolly.grid(row=0, column=1, sticky=(N,S))
        # creating a horizontal scrollbar
        self.scrollx = Scrollbar(self.top_frame, orient=HORIZONTAL)
        # adding the scrollbar
        self.scrollx.grid(row=1, column=0, sticky=(W, E))

                # creating the canvas for display the PDF pages
        self.output = Canvas(self.top_frame, bg='#ECE8F3', width=560, height=435)
        # inserting both vertical and horizontal scrollbars to the canvas
        self.output.configure(yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        # adding the canvas
        self.output.grid(row=0, column=0)
        # configuring the horizontal scrollbar to the canvas
        self.scrolly.configure(command=self.output.yview)
        # configuring the vertical scrollbar to the canvas
        self.scrollx.configure(command=self.output.xview)

        # Bind mouse scroll events to the canvas
        self.output.bind("<MouseWheel>", self._on_mousewheel)
        self.output.bind("<Shift-MouseWheel>", self._on_shift_mousewheel)
        self.output.bind("<Button-4>", self._on_mousewheel)
        self.output.bind("<Button-5>", self._on_mousewheel)

                 # loading the button icons
        # loading the button icons
        self.uparrow_icon = PhotoImage(file='uparrow.png')
        self.downarrow_icon = PhotoImage(file='downarrow.png')
        # resizing the icons to fit on buttons
        # You can adjust the subsample values to change the size of the icons
        # Higher values will make the icons smaller
        self.uparrow = self.uparrow_icon.subsample(20, 20)
        self.downarrow = self.downarrow_icon.subsample(20, 20)
        # resizing the icons to fit on buttons
        # creating an up button with an icon
        self.upbutton = ttk.Button(self.bottom_frame, image=self.uparrow, command=self.previous_page)
        # adding the button
        self.upbutton.grid(row=0, column=1, padx=(270, 5), pady=8)
        # creating a down button with an icon
        self.downbutton = ttk.Button(self.bottom_frame, image=self.downarrow, command=self.next_page)
        # adding the button
        self.downbutton.grid(row=0, column=3, pady=8)
        # label for displaying page numbers
        self.page_label = ttk.Label(self.bottom_frame, text='page')
        # adding the label
        self.page_label.grid(row=0, column=4, padx=5)

        # creating a theme menu
        self.thememenu = Menu(self.menu)
        self.menu.add_cascade(label="Themes", menu=self.thememenu)
        self.thememenu.add_command(label="Light Mode", command=self.set_light_mode)
        self.thememenu.add_command(label="Dark Mode", command=self.set_dark_mode)

        # creating a zoom menu
        self.zoommnu = Menu(self.menu)
        self.menu.add_cascade(label="Zoom", menu=self.zoommnu)
        self.zoommnu.add_command(label="Zoom In", command=self.zoom_in)
        self.zoommnu.add_command(label="Zoom Out", command=self.zoom_out)

        # Initialize PDFMiner instance
        self.miner = None

    def _on_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:
            self.output.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.output.yview_scroll(1, "units")

    def _on_shift_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:
            self.output.xview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.output.xview_scroll(1, "units")

    def open_file(self):
        # Implement the logic to open a PDF file
        file_path = fd.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.path = file_path
            self.fileisopen = True
            # Load the PDF file using PDFMiner or any other PDF library
            self.miner = PDFMiner(file_path)
            metadata, self.numPages = self.miner.get_metadata()
            self.display_page()

    def display_page(self):
        # checking if numPages is less than current_page and if current_page is less than
        # or equal to 0
        if 0 <= self.current_page < self.numPages:
            # getting the page using get_page() function from miner
            self.img = self.miner.get_page(self.current_page)
            # inserting the page image inside the Canvas
            self.output.create_image(0, 0, anchor='nw', image=self.img)
            # the variable to be stringified
            self.stringified_current_page = self.current_page + 1
            # updating the page label with number of pages 
            self.page_label['text'] = str(self.stringified_current_page) + ' of ' + str(self.numPages)
            # creating a region for inserting the page inside the Canvas
            region = self.output.bbox(ALL)
            # making the region to be scrollable
            self.output.configure(scrollregion=region)

    # function for displaying the previous page        
    def previous_page(self):
        # checking if fileisopen
        if self.fileisopen:
            # checking if current_page is greater than 0
            if self.current_page > 0:
                # decrementing the current_page by 1
                self.current_page -= 1
                # displaying the previous page
                self.display_page()

    def next_page(self):
        # checking if file is open
        if self.fileisopen:
            # checking if current_page is less than or equal to numPages-1
            if self.current_page < self.numPages - 1:
                # updating the page with value 1
                self.current_page += 1
                # displaying the new page
                self.display_page()   
    #dark mode
    def set_light_mode(self):
        self.master.config(bg='white')
        self.output.config(bg='white')
        if self.fileisopen:
            self.display_page()
    #light mode
    def set_dark_mode(self):
        self.master.config(bg='black')
        self.output.config(bg='black')
        if self.fileisopen:
            self.display_page()

    def zoom_in(self):
        if self.fileisopen:
            self.miner.zoom_in()
            self.display_page()

    def zoom_out(self):
        if self.fileisopen:
            self.miner.zoom_out()
            self.display_page()

if __name__ == "__main__":
    root = Tk()
    app = PDFViewer(root)
    root.mainloop()


