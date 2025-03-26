from kivy.app import app

class PixelShiftApp(App):
    def build(self):
        Builder.load_file("GUI.kv")
        return PixelShift()


if __name__ == "__main__":
    PixelShiftApp().run()