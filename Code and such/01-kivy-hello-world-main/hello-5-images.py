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
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout


class ImageButton(ButtonBehavior, Image):
    pass

class BoxLayoutApp(App): 
    def build(self):
        superBox = BoxLayout(orientation ='vertical')
        HB = BoxLayout(orientation ='horizontal')

        # windsurf
        ws_btn = ImageButton(source='1.png', size_hint=(1, 0.9))
        ws_btn.bind(on_press=self.on_windsurf_press)

        # surf
        s_btn = ImageButton(source='2.png', size_hint=(1, 0.9))
        s_btn.bind(on_press=self.on_surf_press)

        # kayak
        k_btn = ImageButton(source='3.png', size_hint=(1, 0.9))
        k_btn.bind(on_press=self.on_kayak_press)

        HB.add_widget(ws_btn)
        HB.add_widget(s_btn)
        HB.add_widget(k_btn)

        VB = BoxLayout(orientation ='vertical')

        btn3 = Button(text ="Three")
        btn4 = Button(text ="Four")

        VB.add_widget(btn3)
        VB.add_widget(btn4)

        superBox.add_widget(HB)
        superBox.add_widget(VB)

        return superBox

    
    
    def on_windsurf_press(self, instance):
        print("Windsurf!")

    def on_surf_press(self, instance):
        print("Surf!")

    def on_kayak_press(self, instance):
        print("Kayak!")


root = BoxLayoutApp() 
root.run() 
