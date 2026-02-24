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

        # Add a pale blue background
        with root.canvas.before:
            Color(0.8, 0.9, 1, 1)  # Pale blue color (RGB + alpha)
            self.rect = Rectangle(size=root.size, pos=root.pos)

        # Update the background size when the window size changes
        root.bind(size=self._update_rect, pos=self._update_rect)

        # Add a label with "Hello World"
        label = Label(
            text="Hello World",
            font_size='30sp',
            color=(0, 0, 0, 1)  # Black color for text
        )
        root.add_widget(label)

        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == "__main__":
    SimpleApp().run()