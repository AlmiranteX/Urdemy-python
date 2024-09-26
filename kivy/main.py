from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.clock import Clock
import random, os


# Define o tamanho da janela antes de carregar o App
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '480')

# Funçao logica alfabeto
def alphabet(L, click, i=0):
    
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', \
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    speak_letters = ['ei', 'bi', 'ci', 'di', 'i', 'éf', 'dji', 'êicht', 'ai', 'djêi', 'key', 'él', 'ém', 'én', 'ou', \
        'pi', 'quiu', 'ar', 'és', 'ti', 'iu', 'vi', 'dãbliu', 'équis', 'uai', 'zi']
    
    for letter in letters:
        
        if letter == L:
            if click == speak_letters[i]:
                return True, i, letters, speak_letters
            else:
                return False, i, letters, speak_letters 
            
        i+=1
        
    
       


# Define the main app class
class SimpleApp(App):
    
    def build(self):
        return SimpleLayout()
    
        
    
def color(self, bt, L, click):
    
    self.ids.btns.disabled = True
    i=2
    i += alphabet(L, click)[1]
    
    self.ids.alphabet_English.text = f'English alphabet {i}/26' 
    
    
def colo_gray(self):
    os.system('cls')
    click_letter = self.ids.btn_1.text
    letter = self.ids.letter.text
        
    test = alphabet(L=letter, click=click_letter)
    win, indice, letra, fala = test[0], test[1], test[2], test[3]
        
    print(indice, len(fala))

    if letra == 'z':
        os.system('cls')
        print('Fim do programa...')
    else:
        self.ids.letter.text = letra[indice+1]
    
        
    self.ids.btns.disabled = False
        
    #sortear fala nos btns
    n = random.randint(0, 3)
    if n == 0:
        self.ids.btn_1.text = fala[indice+1]
        self.ids.btn_2.text =  fala[random.randint(0, 25)]
        self.ids.btn_3.text =  fala[random.randint(0, 25)]
        self.ids.btn_4.text = fala[ random.randint(0, 25)]   
    elif n == 1:
        self.ids.btn_2.text = fala[indice+1]
        self.ids.btn_1.text =  fala[random.randint(0, 25)]
        self.ids.btn_3.text =  fala[random.randint(0, 25)]
        self.ids.btn_4.text =  fala[random.randint(0, 25)]
    elif n == 2:
        self.ids.btn_3.text =  fala[indice+1]
        self.ids.btn_2.text =  fala[random.randint(0, 25)]
        self.ids.btn_1.text =  fala[random.randint(0, 25)]
        self.ids.btn_4.text =  fala[random.randint(0, 25)]
    elif n == 3:
        self.ids.btn_4.text = fala[indice+1]
        self.ids.btn_2.text = fala[random.randint(0, 25)]
        self.ids.btn_3.text =  fala[random.randint(0, 25)]
        self.ids.btn_1.text =  fala[random.randint(0, 25)]
            
          
# Define the layout class
class SimpleLayout(BoxLayout):
  
    def on_BTN_1(self):
        """Sumary:
            1-salva txt do btn_1 na var clcik_letter
            2-salva txt do label que mostra a letra atual na var letter
            3-chama a funçao alphabet que fas os teste de acerto e erro
            4-salva o valor retornado da funcao alphabet em variaveis individuais
        """
        
        click_letter = self.ids.btn_1.text
        letter = self.ids.letter.text
        
        test = alphabet(L=letter, click=click_letter)
        win, indice, letra, fala = test[0], test[1], test[2], test[3]
    
        if win == True:
            
            color(self, bt='btn_1', L=letter, click=click_letter)
            if letter == 'z':
                print('ganhor')
            else:
                colo_gray(self)
            
    def on_BTN_2(self):
        print('ok')
        click_letter = self.ids.btn_2.text
        letter = self.ids.letter.text
        
        test = alphabet(L=letter, click=click_letter)
        win, indice, letra, fala = test[0], test[1], test[2], test[3]
        
        if win == True:
            color(self, bt='btn_2', L=letter, click=click_letter)
            colo_gray(self)
            
    def on_BTN_3(self):
        print('ok')
        click_letter = self.ids.btn_3.text
        letter = self.ids.letter.text
        
        test = alphabet(L=letter, click=click_letter)
        win, indice, letra, fala = test[0], test[1], test[2], test[3]
        
        if win == True:
        
            color(self, bt='btn_3', L=letter, click=click_letter)
            colo_gray(self)
            
    def on_BTN_4(self):
        print('ok')
        click_letter = self.ids.btn_4.text
        letter = self.ids.letter.text
        
        test = alphabet(L=letter, click=click_letter)
        win, indice, letra, fala = test[0], test[1], test[2], test[3]
        
        if win == True:
           
            color(self, bt='btn_4', L=letter, click=click_letter)
            colo_gray(self)
    
            
      
        
    
# Run the application
if __name__ == "__main__":
    SimpleApp().run()
    
