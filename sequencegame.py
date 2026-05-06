from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

from kivy.app import App

class SequenceApp(App):
    pass

if __name__ == '__main__':
    SequenceApp().run()
