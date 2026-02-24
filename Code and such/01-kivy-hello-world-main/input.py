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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.instructions_label = Label(text='Enter your name')
        self.name_input = TextInput(text='', multiline=False)
        self.greet_button = Button(text='Greet')
        self.greet_button.bind(on_press=self.greet)
        self.greeting_label = Label(text='')
        
        layout.add_widget(self.instructions_label)
        layout.add_widget(self.name_input)
        layout.add_widget(self.greet_button)
        layout.add_widget(self.greeting_label)
        
        return layout
    
    def greet(self, instance):
        name = self.name_input.text
        self.greeting_label.text = f'Hello, {name}!'

if __name__ == '__main__':
    SimpleApp().run()

    