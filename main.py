from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        screen = MDScreen()

        # Кнопка с текстом
        btn = MDRaisedButton(
            text="Hello, World",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        screen.add_widget(btn)

        return screen


MainApp().run()
