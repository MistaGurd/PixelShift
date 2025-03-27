# Diverse imports
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.core.window import Window
from kivy.lang.builder import Builder
#Builder.load_file('GUI.kv')

from BGfjernelse import BGFjern

class MainMenu(Screen):
    pass

class PixelShiftApp(App):
    def build(self):
        Window.maximize()
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="hovedmenu"))
        sm.add_widget(BGFjern(name="bgfjern"))
        sm.transition = SwapTransition()
        return sm

if __name__ == "__main__":
    PixelShiftApp().run()
