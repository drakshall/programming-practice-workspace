from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class InputNameForm(BoxLayout):
    def nameInputHandler(self):
        print("hi :)")

class SequenceApp(App):
    pass

if __name__ == '__main__':
    SequenceApp().run()
