from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.core.window import Window
from kivy.lang import Builder
# Diverse imports

from BGfjernelse import BGFjern
from PDF_Merge import PDF_Merging
from Filkompromering import FilKomprimering
from Formatkonvertering import FormatKonverter

# Overstående er import af de klasser, som hver Python fil har.
# Hver klasse, er hver sin del (her en screen) af koden

class MainMenu(Screen):
    pass

class PixelShiftApp(App):
    def build(self):
        Builder.load_file('GUI.kv')
        Window.maximize()
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="hovedmenu"))
        sm.add_widget(BGFjern(name="bgfjern"))
        sm.add_widget(PDF_Merging(name="pdf_merger"))
        sm.add_widget(FilKomprimering(name="filecompress"))
        sm.add_widget(FormatKonverter(name="formatkonvert"))
        sm.transition = SwapTransition()
        return sm

if __name__ == "__main__": # Opstart af programmet
    PixelShiftApp().run()
