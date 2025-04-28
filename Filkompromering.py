from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty
import tkinter as tk

class FileCompressHandle(Screen):
    Start_nummer = NumericProperty()

class FilKomprimering(Screen):
    pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tk_root = tk.Tk()
        self.tk_root.withdraw()

    def file_select(self):
        pass

    def folder_select(self):
        pass

    def drag_and_drop(self):
        pass

    def file_selection(self):
        pass

    def clear_list(self):
        pass