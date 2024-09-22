from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

# Define o tamanho da janela antes de carregar o App
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '480')

# Define the main app class
class SimpleApp(App):
    def build(self):
        return SimpleLayout()

# Define the layout class
class SimpleLayout(BoxLayout):
    def on_BTN_1(self):
        # Change the label's text when the button is pressed
        self.ids.my_label.text = "Button clicked!"

# Run the application
if __name__ == "__main__":
    SimpleApp().run()
