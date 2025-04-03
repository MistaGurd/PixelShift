# Diverse imports
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.core.window import Window

from BGfjernelse import BGFjern
from PDF_Merge import PDF_Merge

# Overstående er import af de klasser, som hver Python fil har. Hver klasse,
# er hver sin del (her en screen) af koden
class MainMenu(Screen):
    pass

class PixelShiftApp(App):
    def build(self):
        Window.maximize()
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="hovedmenu"))
        sm.add_widget(BGFjern(name="bgfjern"))
        sm.add_widget(PDF_Merge(name="pdf_merger"))
        sm.transition = SwapTransition()
        return sm

if __name__ == "__main__": # Opstart af programmet
    PixelShiftApp().run()
