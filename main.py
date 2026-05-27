from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty

# Верстка нашої гри
KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: [0.08, 0.09, 0.12, 1]  # Темний ігровий фон
        Rectangle:
            pos: self.pos
            size: self.size

    # Змінна рахунку: Вгорі по центру
    Label:
        text: "PINS: " + str(app.score)
        font_size: '40sp'
        bold: True
        color: [1, 0.8, 0, 1]  # Золотий колір
        pos_hint: {'center_x': 0.5, 'top': 0.92}
        size_hint: (None, None)
        size: self.texture_size

    # Клікер-кнопка з твоїм PNG по центру
    Button:
        size_hint: (None, None)
        # Якщо кнопку натиснуто — вона автоматично трохи стискається
        size: (280, 280) if self.state == 'normal' else (240, 240)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        # Використовуємо твою прозору PNG-шку
        background_normal: 'images/sigmapin.png'
        background_down: 'images/sigmapin.png'
        border: (0, 0, 0, 0)
        
        on_press: app.increment_score()
'''

class SigmaClickerApp(App):
    score = NumericProperty(0)

    def build(self):
        return Builder.load_string(KV)

    def increment_score(self):
        self.score += 1

if __name__ == '__main__':
    SigmaClickerApp().run()
