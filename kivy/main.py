from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

now_letter = 0

# Define o tamanho da janela antes de carregar o App
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '480')

# Funçao logica alfabeto
def alphabet(L):
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', \
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    speak_letters = ['ei', 'bi', 'ci', 'di', 'i', 'éf', 'dji', 'êicht', 'ai', 'djêi', 'key', 'él', 'ém', 'én', 'ou', \
        'pi', 'quiu', 'ar', 'és', 'ti', 'iu', 'vi', 'dãbliu', 'équis', 'uai', 'zi']
    print(L)
    
        


# Define the main app class
class SimpleApp(App):
    
    def build(self):
        return SimpleLayout()
    
    
# Define the layout class
class SimpleLayout(BoxLayout):

    def on_BTN_1(self):
        click_letter = self.ids.btn_1.text
        return alphabet(L=click_letter)

# Run the application
if __name__ == "__main__":
    SimpleApp().run()
