import os
import kivy

# Avoid using OpenGL 3.0 on windows VM
# Angle will convert OpenGL to DirectX11
if kivy.platform == 'win':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
else:
    # On Android / Linux use OpenGL by default:
    pass

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class SimpleApp(App):
    def build(self):
        # Create the root widget
        root = FloatLayout()

        # Add a label with "Hello World"
        label = Label(
            text="Hello World",
            font_size='30sp',
            color=(100, 250, 100, 1)  # Purple color for text
        )
        root.add_widget(label)

        return root

if __name__ == "__main__":
    SimpleApp().run()
