from kivy.uix.screenmanager import Screen # Til screen manager i Main
from kivy.properties import ObjectProperty, NumericProperty
import PyPDF4
import tkinter as tk
from tkinter import filedialog # Windows dialog vindue
import os

from kivy.lang import Builder
Builder.load_file('GUI.kv')

class PDFNummer(Screen):
    Start_nummer = NumericProperty(0)

class PDF_Merge(Screen):

class PDF_Merge(Screen):
    pdf_list_container = ObjectProperty(None)
    status_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_tk = tk.Tk()
        self.root_tk.withdraw()
        self.selected_pdfs = []

    def add_pdfs(self):
        filepaths = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if filepaths:
            self.selected_pdfs.extend(filepaths)
            self.update_pdf_list()

    def update_pdf_list(self):
        self.pdf_list_container.clear_widgets()
        for i, path in enumerate(self.selected_pdfs):
            entry = PDFEntry()
            entry.entry_index = i
            entry.ids.file_label.text = os.path.basename(path)
            self.pdf_list_container.add_widget(entry)

    def move_up(self, index):
        if index > 0:
            self.selected_pdfs[index], self.selected_pdfs[index-1] = self.selected_pdfs[index-1], self.selected_pdfs[index]
            self.update_pdf_list()

    def move_down(self, index):
        if index < len(self.selected_pdfs) - 1:
            self.selected_pdfs[index], self.selected_pdfs[index+1] = self.selected_pdfs[index+1], self.selected_pdfs[index]
            self.update_pdf_list()

    def merge_pdfs(self):
        if len(self.selected_pdfs) < 2:
            self.status_label.text = "Error: Select at least 2 PDFs!"
            return

        output_path = filedialog.asksaveasfilename(
            title="Save Merged PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if not output_path:
            return

        try:
            merger = PyPDF4.PdfFileMerger()
            for pdf in self.selected_pdfs:
                merger.append(pdf)
            merger.write(output_path)
            merger.close()
            self.status_label.text = f"Success: Merged to {os.path.basename(output_path)}"
            self.selected_pdfs = []
            self.update_pdf_list()
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

    def clear_list(self):
        self.selected_pdfs = []
        self.update_pdf_list()