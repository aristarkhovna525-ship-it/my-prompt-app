from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window

# Настраиваем приятный темный фитнес-дизайн
Window.clearcolor = (0.1, 0.11, 0.13, 1)

class KBZUApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 15

        # Заголовок
        self.add_widget(Label(text="🍏 КБЖУ ПОМОЩНИК", font_size='24sp', bold=True, color=(0.4, 0.8, 0.4, 1)))

        # Поля ввода данных
        self.add_widget(Label(text="Введите ваш вес (кг):", font_size='16sp', halign='left'))
        self.weight = TextInput(text="70", multiline=False, input_filter='int', font_size='18sp')
        self.add_widget(self.weight)

        self.add_widget(Label(text="Введите ваш рост (см):", font_size='16sp'))
        self.height = TextInput(text="170", multiline=False, input_filter='int', font_size='18sp')
        self.add_widget(self.height)

        self.add_widget(Label(text="Введите ваш возраст:", font_size='16sp'))
        self.age = TextInput(text="30", multiline=False, input_filter='int', font_size='18sp')
        self.add_widget(self.age)

        # Выбор цели
        self.add_widget(Label(text="Выберите вашу цель:", font_size='16sp'))
        self.goal = Spinner(text='Поддержание веса', values=('Похудение', 'Поддержание веса', 'Набор массы'), font_size='16sp')
        self.add_widget(self.goal)

        # Кнопка расчета
        self.btn = Button(text="РАССЧИТАТЬ НОРМУ", font_size='18sp', bold=True, background_color=(0.2, 0.7, 0.2, 1))
        self.btn.bind(on_press=self.calculate)
        self.add_widget(self.btn)

        # Поле вывода результата
        self.result = Label(text="Результат появится здесь", font_size='16sp', bold=True, color=(0.9, 0.9, 0.9, 1))
        self.add_widget(self.result)

        # Имитация нижнего рекламного баннера Яндекса (ID: R-M-20149375-1)
        self.add_widget(Label(text="Рекламный блок Яндекс ID: 20149375", font_size='11sp', color=(0.5, 0.5, 0.5, 1)))

    def calculate(self, instance):
        try:
            w = int(self.weight.text)
            h = int(self.height.text)
            a = int(self.age.text)
            
            # Базовый расчет по формуле Миффлина - Сан Жеора
            calories = int(10 * w + 6.25 * h - 5 * a + 5)
            
            if self.goal.text == 'Похудение':
                calories = int(calories * 0.85)
                status = "🔥 Цель: Похудение (Дефицит 15%)"
            elif self.goal.text == 'Набор массы':
                calories = int(calories * 1.15)
                status = "💪 Цель: Набор массы (Профицит 15%)"
            else:
                status = "🍏 Цель: Поддержание баланса"

            # Рассчитываем БЖУ
            b = int((calories * 0.3) / 4)
            j = int((calories * 0.3) / 9)
            u = int((calories * 0.4) / 4)

            self.result.text = f"{status}\n\n🔥 Калории: {calories} ккал\n🍞 Белки: {b}г  |  🥑 Жиры: {j}г  |  🌾 Углеводы: {u}г"
        except:
            self.result.text = "❌ Ошибка! Проверьте введенные данные."

class MainApp(App):
    def build(self):
        return KBZUApp()

if __name__ == '__main__':
    MainApp().run()
