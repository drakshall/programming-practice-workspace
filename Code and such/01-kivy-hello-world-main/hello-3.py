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

class SimpleLayout(FloatLayout):
    pass

class SimpleApp(App):
    def build(self):
        return SimpleLayout()

if __name__ == "__main__":
    SimpleApp().run()

    