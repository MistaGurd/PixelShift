import os
import subprocess
from tkinter import filedialog
import tkinter as tk
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from PIL import Image
from docx import Document

class FormatKonverter(Screen):
    file_list_container = ObjectProperty()
    status_label = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_tk = tk.Tk()
        self.root_tk.withdraw()
        self.selected_files = []
        self.default_output_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        self.output_folder = None
        Window.bind(on_dropfile=self.on_drop)

    def on_drop(self, window, file_path):
        formater = (".pdf", ".jpg", ".jpeg", ".png", ".webp", ".avif", ".pptx", ".docx", ".txt")
        path = file_path.decode("utf-8")
        if os.path.isdir(path):
            files_in_dir = [
                os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(formater)
            ]
            self.selected_files.extend(files_in_dir)
        elif path.lower().endswith(formater):
            self.selected_files.append(path)
        self.update_file_list()

    def file_select(self):
        filepaths = filedialog.askopenfilenames(
            title="Vælg filer",
            filetypes=[("Formater", "*.pdf;*.jpg;*.jpeg;*.png;*.webp;*.avif;*.pptx;*.docx;*.txt")]
        )
        if filepaths:
            self.selected_files.extend(filepaths)
            self.update_file_list()

    def folder_select(self):
        formater = (".pdf", ".jpg", ".jpeg", ".png", ".webp", ".avif", ".pptx", ".docx", ".txt")
        filepaths = filedialog.askdirectory()
        if os.path.isdir(filepaths):
            files_in_dir = [
                os.path.join(filepaths, f) for f in os.listdir(filepaths) if f.lower().endswith(formater)
            ]
            self.selected_files.extend(files_in_dir)
        self.update_file_list()

    def update_file_list(self):
        # Update the file list display
        pass

    def ask_output_folder(self):
        folder = filedialog.askdirectory(title="Vælg mappesti")
        return folder if folder else self.create_unique_output_folder(self.default_output_folder)

    def create_unique_output_folder(self, base_folder):
        output_folder = os.path.join(base_folder, "KonverteredeFiler")
        counter = 1
        while os.path.exists(output_folder):
            output_folder = os.path.join(base_folder, f"KonverteredeFiler_{counter}")
            counter += 1
        os.makedirs(output_folder)
        return output_folder

    def convert_files(self):
        output_folder = self.ask_output_folder()
        for file in self.selected_files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif')):
                self.convert_image_to_png(file, output_folder)
            elif file.lower().endswith('.txt'):
                self.convert_txt_to_docx(file, output_folder)
            elif file.lower().endswith('.docx'):
                self.convert_docx_to_pdf(file, output_folder)
            elif file.lower().endswith('.pptx'):
                self.convert_pptx_to_pdf(file, output_folder)
            elif file.lower().endswith('.pdf'):
                self.convert_pdf_to_docx(file, output_folder)

    def convert_image_to_png(self, image_path, output_folder):
        img = Image.open(image_path)
        png_path = os.path.join(output_folder, os.path.basename(image_path).replace(img.format.lower(), "png"))
        img.save(png_path, "PNG")
        self.status_label.text = f"Billede konverteret til PNG: {png_path}"

    def convert_txt_to_docx(self, txt_path, output_folder):
        doc = Document()
        with open(txt_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
        for line in content:
            doc.add_paragraph(line)
        docx_path = os.path.join(output_folder, os.path.basename(txt_path).replace(".txt", ".docx"))
        doc.save(docx_path)
        self.status_label.text = f"TXT konverteret til DOCX: {docx_path}"

    def convert_docx_to_pdf(self, docx_path, output_folder):
        pdf_path = os.path.join(output_folder, os.path.basename(docx_path).replace(".docx", ".pdf"))
        subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", output_folder, docx_path])
        self.status_label.text = f"DOCX konverteret til PDF: {pdf_path}"

    def convert_pptx_to_pdf(self, pptx_path, output_folder):
        pdf_path = os.path.join(output_folder, os.path.basename(pptx_path).replace(".pptx", ".pdf"))
        subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", output_folder, pptx_path])
        self.status_label.text = f"PPTX konverteret til PDF: {pdf_path}"

    def convert_pdf_to_docx(self, pdf_path, output_folder):
        docx_path = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".docx"))
        subprocess.run(["libreoffice", "--headless", "--convert-to", "docx", "--outdir", output_folder, pdf_path])
        self.status_label.text = f"PDF konverteret til DOCX: {docx_path}"




def clear_list(self):
    self.selected_files = []
    self.update_file_list()
    # Rydder listen
