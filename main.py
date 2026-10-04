from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

# Настраиваем стильный темный фон приложения
Window.clearcolor = (0.08, 0.08, 0.12, 1)


class PromptBuilderApp(App):

    def build(self):
        # Хранилище выбранных элементов промта
        self.selected_tags = {
            "shot": "Cinematic shot",
            "subject": "a mysterious cybernetic warrior",
            "action": "standing still",
            "lighting": "dramatic neon lighting",
            "quality": "photorealistic, 8k resolution, highly detailed",
        }

        # Главный контейнер
        main_layout = BoxLayout(
            orientation="vertical", padding=15, spacing=10
        )

        # 1. Шапка приложения
        header = Label(
            text="AI Video Prompt Builder 🤖",
            font_size="24sp",
            bold=True,
            size_hint_y=None,
            height=50,
            color=(0.0, 0.8, 1.0, 1),
        )
        main_layout.add_widget(header)

        # 2. Поле вывода готового промта
        self.output_box = TextInput(
            text=self.generate_prompt_text(),
            font_size="16sp",
            readonly=True,
            size_hint_y=None,
            height=120,
            background_color=(0.15, 0.15, 0.22, 1),
            foreground_color=(1, 1, 1, 1),
        )
        main_layout.add_widget(self.output_box)

        # Кнопка быстрой скопировать в буфер обмена
        btn_copy = Button(
            text="СКОПИРОВАТЬ ПРОМТ 📋",
            background_color=(0.0, 0.7, 0.9, 1),
            size_hint_y=None,
            height=50,
            bold=True,
        )
        btn_copy.bind(on_press=self.copy_to_clipboard)
        main_layout.add_widget(btn_copy)

        # Разделитель
        main_layout.add_widget(
            Label(text="Конструктор сцены:", size_hint_y=None, height=20)
        )

        # 3. Скролл-зона с кнопками выбора тегов
        scroll = ScrollView()
        scroll_layout = BoxLayout(
            orientation="vertical", spacing=15, size_hint_y=None
        )
        scroll_layout.bind(minimum_height=scroll_layout.setter("height"))

        # Добавляем категории выбора
        self.add_category_block(
            scroll_layout,
            "РАКУРС И ПЛАН (Shot Type):",
            "shot",
            {
                "Крупный план": "Close-up cinematic shot",
                "Общий план": "Wide cinematic shot",
                "Съемка с дрона": "Flipped drone shot",
                "Макро съемка": "Macro detailed shot",
            },
        )

        self.add_category_block(
            scroll_layout,
            "ОБЪЕКТ (Subject):",
            "subject",
            {
                "Кибер-воин": "a mysterious cybernetic warrior",
                "Спортивный авто": "a sleek red sports car",
                "Пушистый дракончик": "a cute fluffy baby dragon",
                "Одинокий человек": "a lone person in a black coat",
            },
        )

        self.add_category_block(
            scroll_layout,
            "ДЕЙСТВИЕ (Action):",
            "action",
            {
                "Стоит неподвижно": "standing still and looking into camera",
                "Мчится на скорости": "speeding down a winding road",
                "Идет под дождем": "walking through the heavy rain",
                "Ловит бабочку": "trying to catch a magical butterfly",
            },
        )

        self.add_category_block(
            scroll_layout,
            "ОСВЕЩЕНИЕ (Lighting):",
            "lighting",
            {
                "Неоновое": "dramatic neon lighting, cyberpunk aesthetic",
                "Закатное (Золотой час)": "golden hour sunset light with long hard shadows",
                "Мягкий свет": "soft volumetric studio lighting",
                "Кино-свет": "cinematic dramatic contrast lighting",
            },
        )

        scroll.add_widget(scroll_layout)
        main_layout.add_widget(scroll)

        return main_layout

    def add_category_block(self, parent_layout, label_text, key, options):
        """Создает блок категории с кнопками выбора."""
        parent_layout.add_widget(
            Label(
                text=label_text,
                halign="left",
                size_hint_y=None,
                height=30,
                color=(0.7, 0.7, 0.8, 1),
            )
        )
        grid_layout = BoxLayout(
            orientation="horizontal", spacing=5, size_hint_y=None, height=45
        )

        for rus_name, eng_val in options.items():
            btn = Button(
                text=rus_name,
                font_size="12sp",
                background_color=(0.2, 0.2, 0.3, 1),
            )
            # Привязываем изменение значения при клике на кнопку
            btn.bind(
                on_press=lambda instance, k=key, v=eng_val: self.update_tag(
                    k, v
                )
            )
            grid_layout.add_widget(btn)

        parent_layout.add_widget(grid_layout)

    def generate_prompt_text(self):
        """Собирает все теги в один связный английский текст."""
        return f"{self.selected_tags['shot']} of {self.selected_tags['subject']}, {self.selected_tags['action']}. {self.selected_tags['lighting']}, {self.selected_tags['quality']}."

    def update_tag(self, key, value):
        """Обновляет выбранный тег и перерисовывает окно вывода."""
        self.selected_tags[key] = value
        self.output_box.text = self.generate_prompt_text()

    def copy_to_clipboard(self, instance):
        """Копирует готовый промт в память телефона."""
        Clipboard.copy(self.output_box.text)


if __name__ == "__main__":
    PromptBuilderApp().run()

