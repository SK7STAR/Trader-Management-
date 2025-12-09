from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        title = Label(
            text="📱 Trader Management",
            font_size="24sp",
            size_hint=(1, 0.2)
        )
        layout.add_widget(title)

        subtitle = Label(
            text="Status: Free User (premium system planned)",
            font_size="14sp",
            size_hint=(1, 0.1)
        )
        layout.add_widget(subtitle)

        # Buttons for main sections (for now they just print text)
        btn_trade = Button(
            text="Trade Entry & P&L",
            size_hint=(1, 0.13),
            on_press=lambda x: self._placeholder("Trade Entry & P&L")
        )
        layout.add_widget(btn_trade)

        btn_risk = Button(
            text="Risk Management",
            size_hint=(1, 0.13),
            on_press=lambda x: self._placeholder("Risk Management")
        )
        layout.add_widget(btn_risk)

        btn_premium_tools = Button(
            text="Premium Tools (Locked)",
            size_hint=(1, 0.13),
            on_press=lambda x: self._placeholder("Premium Tools")
        )
        layout.add_widget(btn_premium_tools)

        btn_activate = Button(
            text="Activate Premium (Payment planned)",
            size_hint=(1, 0.13),
            on_press=lambda x: self._placeholder("Activate Premium")
        )
        layout.add_widget(btn_activate)

        btn_settings = Button(
            text="Settings & Help",
            size_hint=(1, 0.13),
            on_press=lambda x: self._placeholder("Settings & Help")
        )
        layout.add_widget(btn_settings)

        self.add_widget(layout)

    def _placeholder(self, name: str):
        # For now this just prints to console.
        # Later we will open real screens here.
        print(f"[APP] Button pressed: {name}")


class TraderScreenManager(ScreenManager):
    pass


class TraderApp(App):
    def build(self):
        sm = TraderScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        return sm


if __name__ == "__main__":
    TraderApp().run()
