from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        #button = CustomButton(text="Test Button", pos_hint={"center_x": 0.5, "center_y": 0.5})
        #button.bind(on_press=self.pressed)
        #return button

        txt = TextInput()
        txt.bind(text=self.pressed)
        return txt

    def pressed(self, instance, value):
        print(value)

if __name__ == '__main__':
    app = MainApp()
    app.run()
