# Defines the app root and orchestrates the running of the program

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from GridWidget import GridWidget   


class UIRoot(FloatLayout):
    pass

class UIApp(App):
    def build(self):
        return UIRoot()

if __name__ == '__main__':
    UIApp().run()