# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from GridWidget import GridWidget   



class CARoot(BoxLayout):
    pass

class CAApp(App):
    def build(self):
        return CARoot()

if __name__ == '__main__':
    CAApp().run()