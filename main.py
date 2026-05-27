from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty

# Оновлена верстка гри
KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: [0.08, 0.09, 0.12, 1]  # Темний фон
        Rectangle:
            pos: self.pos
            size: self.size

    # Контейнер для рахунку: Монетка + Цифри (Вгорі по центру)
    BoxLayout:
        orientation: 'horizontal'
        size_hint: (None, None)
        size: self.minimum_size  # Автоматично стискається під вміст для точного центрування
        pos_hint: {'center_x': 0.5, 'top': 0.92}
        spacing: '12dp'  # Відступ між монеткою і цифрами
        align_items: 'center'

        Image:
            source: 'images/gold_coin.png'
            size_hint: (None, None)
            size: ('50dp', '50dp')  # Розмір твоєї монетки
            allow_stretch: True

        Label:
            text: str(app.score)
            font_size: '45sp'
            bold: True
            color: [1, 0.8, 0, 1]  # Золотий колір цифр
            size_hint: (None, None)
            size: self.texture_size

    # Клікер-кнопка з Sigma Pin по центру
    Button:
        size_hint: (None, None)
        size: (280, 280) if self.state == 'normal' else (240, 240)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
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
