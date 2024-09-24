from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.label = Label(text="Esperando 3 segundos...")
        self.add_widget(self.label)
        # Agendar a função `change_text` para ser chamada em 3 segundos
        Clock.schedule_once(self.change_text, 3)

    def change_text(self, dt):
        self.label.text = "Pronto! Texto atualizado após 3 segundos."

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
