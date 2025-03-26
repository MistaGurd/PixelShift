# Diverse imports
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.core.window import Window
from kivy.lang.builder import Builder
Builder.load_file('GUI.kv')

# Importering af klasser fra de andre Python filer
from BGfjernelse import RemBG
# from Filkompromering import...
# from Formatkonvertering import
# from PDF_Merge import



class MainMenu(Screen):
    pass
class PixelShiftApp(App):
    def build(self):
        Window.maximize()  # Får programmet til at åbne i Windowded borderless
        sm = ScreenManager()  # Variabel for håndtering af start-skærm, og resultatskærm
        sm.add_widget(MainMenu(name="hovedmenu"))
        sm.add_widget(RemBG(name="bgfjern"))
        sm.transition = SwapTransition()
        return sm


if __name__ == "__main__":
    PixelShiftApp().run()