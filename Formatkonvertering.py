import os
import locale

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.window import Window

import tkinter as tk
from tkinter import filedialog

from PIL import Image

class FormatKonvertering(Screen):
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
        formater = (".pdf",".jpg",".jpeg",".png",".webp",".avif",'.pptx','.docx','.txt')
        path = file_path.decode("utf-8")  # Når man drag and dropper vil Kivy gerne have
        # et input i bytes, derfor decoder vi med utf-8 fra str til bytes

        if os.path.isdir(path):  # Hvis det er en mappe (dir for directory/mappe)
            files_in_dir = [
                os.path.join(path, f)
                for f in os.listdir(path)
                if f.lower().endswith(formater)
            ]
            self.selected_files.extend(files_in_dir)

        elif path.lower().endswith(formater):  # Hvis det er en enkel fil i følgende format
            self.selected_files.append(path)

        self.update_file_list()

    def file_select(self):
        filepaths = filedialog.askopenfilenames(
            title="Vælg filer",
            filetypes=[("Formater", "*.png;*.jpg;*.jpeg;*.webp;*.avif;*.pdf*.pptx;*.docx;*.txt")]
        )
        if filepaths:
            self.selected_files.extend(filepaths)
            self.update_file_list()

    def folder_select(self):
        formater = (".pdf",".jpg",".jpeg",".png",".webp",".avif",'.pptx','.docx','.txt')
        filepaths = filedialog.askdirectory()

        if os.path.isdir(filepaths):  # Hvis det er en mappe (dir for directory/mappe)
            files_in_dir = [
                os.path.join(filepaths, f)
                for f in os.listdir(filepaths)
                if f.lower().endswith(formater)
            ]
            self.selected_files.extend(files_in_dir)
        elif filepaths.lower().endswith(formater):  # Hvis det er en enkel fil i følgende format
            self.selected_files.append(filepaths)

        self.update_file_list()

    def update_pdf_list(self):
        self.pdf_list_container.clear_widgets()
        for i, path in enumerate(self.selected_pdfs):
            entry = FormatKonvertering() #???????????????????????????????????????????
            entry.entry_index = i
            entry.ids.file_label.text = os.path.basename(path)
            self.pdf_list_container.add_widget(entry)

    def ask_output_folder(self):
        folder = filedialog.askdirectory(title="Vælg mappesti")
        return folder if folder else self.create_unique_output_folder(self.default_output_folder)

    def create_unique_output_folder(self, base_folder):
        output_folder = os.path.join(base_folder, "KonverteredeFiler") # Laver en mappe, hvis brugeren ikke vælger en
        counter = 1  # Programmet navngiver filer, og starter med billede 1
        while os.path.exists(output_folder):
            output_folder = os.path.join(base_folder, f"KonverteredeFiler_{counter}") # her navngives de
            counter += 1 # og tæller op for hvert billede
        os.makedirs(output_folder) # Opretter mappen
        return output_folder
    def Single_konvertering(self):
        pass

    def Mapppe_konvertering(self):
        pass

    def clear_list(self):
        self.selected_files = []
        self.update_file_list()
        # Rydder listen
