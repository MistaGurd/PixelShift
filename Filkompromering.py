import os
import locale

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.window import Window

import tkinter as tk
from tkinter import filedialog

import PIL as pil
import ghostscript

class FileCompressHandle(Screen):
    Start_nummer = NumericProperty()  # Lader Kivy automatisk opdaterer,
                                      # hvis der bliver fortaget ændringer til filerne


class FilKomprimering(Screen):
    file_list_container = ObjectProperty()
    status_label = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.root_tk = tk.Tk()
        self.root_tk.withdraw()

        self.selected_files = []

        Window.bind(on_dropfile=self.on_drop)

    def on_drop(self, window, file_path):
        formater = (".pdf",".jpg",".jpeg",".png",".webp",".avif")
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
            title="Vælg billeder og PDF filer",
            filetypes=[("Formater", "*.png;*.jpg;*.jpeg;*.webp;*.avif;*.pdf*")]
        )
        if filepaths:
            self.selected_files.extend(filepaths)
            self.update_file_list()

    def folder_select(self):
        formater = (".pdf",".jpg",".jpeg",".png",".webp",".avif")
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


    def update_file_list(self):
        self.file_list_container.clear_widgets()
        for i, path in enumerate(self.selected_files):
            entry = FileCompressHandle()
            entry.entry_index = i
            entry.ids.file_label.text = f"{os.path.basename(path)} - fil str. {os.path.getsize(path)/1000000:.2f} MB"
            self.file_list_container.add_widget(entry)

    def compress(self):
        if len(self.selected_files) < 1:  # Sørger for, at der mindst er valgt to PDF filer
            self.ids.status_label.text = "Fejl: Vælg mindst én fil!"  # Hvis ikke, gives denne meddelelse
            return

        output_path = filedialog.asksaveasfilename(
            title="Vælg destinationssti",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        # Vha. tkinter kan destinationsstien vælges, inklusiv navn.
        # Sørger selv for, at formattet bliver PDF
        if not output_path:
            return

        try:
            if self.selected_files.lower().endswith((".pdf")):
                pass

            elif self.selected_files.lower().endswith((".png", ".jpg", ".jpeg",".webp",".avif")):
                pass


        except Exception as e:
            self.status_label.text = f"Fejl: {str(e)}"  # Hvis fejl skulle opstå, kan brugeren her se, hvad der gik galt

    def clear_list(self):
        self.selected_files = []
        self.update_file_list()
        # Rydder listen