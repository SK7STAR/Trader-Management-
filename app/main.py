from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


# -----------------------------
# Trade Entry Screen
# -----------------------------
class TradeEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        title = Label(
            text="Trade Entry & P&L (Basic Demo)",
            font_size="20sp",
            size_hint=(1, 0.12)
        )
        layout.add_widget(title)

        # Entry price
        self.entry_input = TextInput(
            hint_text="Entry price",
            multiline=False,
            size_hint=(1, 0.12),
            input_filter="float"
        )
        layout.add_widget(self.entry_input)

        # Stop loss
        self.sl_input = TextInput(
            hint_text="Stop Loss (SL)",
            multiline=False,
            size_hint=(1, 0.12),
            input_filter="float"
        )
        layout.add_widget(self.sl_input)

        # Take profit
        self.tp_input = TextInput(
            hint_text="Take Profit (TP)",
            multiline=False,
            size_hint=(1, 0.12),
            input_filter="float"
        )
        layout.add_widget(self.tp_input)

        # Result label
        self.result_label = Label(
            text="Enter values and tap Calculate.",
            font_size="14sp",
            size_hint=(1, 0.18)
        )
        layout.add_widget(self.result_label)

        # Calculate button
        calc_btn = Button(
            text="Calculate Risk / Reward",
            size_hint=(1, 0.13),
            on_press=lambda x: self._calculate_basic()
        )
        layout.add_widget(calc_btn)

        # Back to Home
        back_btn = Button(
            text="⬅ Back to Home",
            size_hint=(1, 0.13),
            on_press=lambda x: self.manager.current = "home"
        )
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def _calculate_basic(self):
        try:
            entry = float(self.entry_input.text)
            sl = float(self.sl_input.text)
            tp = float(self.tp_input.text)

            risk = abs(entry - sl)
            reward = abs(tp - entry)

            if risk == 0:
                rr_text = "RR: ∞ (SL equals entry)"
            else:
                rr = reward / risk
                rr_text = f"RR: 1 : {rr:.2f}"

            direction = "LONG" if tp > entry else "SHORT"

            self.result_label.text = (
                f"Direction: {direction}\n"
                f"Risk per unit: {risk:.2f}\n"
                f"Reward per unit: {reward:.2f}\n"
                f"{rr_text}"
            )
        except ValueError:
            self.result_label.text = "Please enter valid numbers for Entry, SL, and TP."


# -----------------------------
# Home Screen
# -----------------------------
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

        # Real navigation: Trade Entry screen
        btn_trade = Button(
            text="Trade Entry & P&L",
            size_hint=(1, 0.13),
            on_press=self.open_trade_entry
        )
        layout.add_widget(btn_trade)

        # Placeholders for future screens
        btn_risk = Button(
            text="Risk Management (soon)",
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
            text="Activate Premium (planned)",
            size_hint=(1, 0.13),
            on_press=lambda x: self._placeholder("Activate Premium")
        )
        layout.add_widget(btn_activate)

        btn_settings = Button(
            text="Settings & Help (soon)",
            size_hint=(1, 0.13),
            on_press=lambda x: self._placeholder("Settings & Help")
        )
        layout.add_widget(btn_settings)

        self.add_widget(layout)

    def open_trade_entry(self, *_):
        self.manager.current = "trade_entry"

    def _placeholder(self, name: str):
        print(f"[APP] Button pressed (not implemented yet): {name}")


# -----------------------------
# Screen Manager & App
# -----------------------------
class TraderScreenManager(ScreenManager):
    pass


class TraderApp(App):
    def build(self):
        sm = TraderScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(TradeEntryScreen(name="trade_entry"))
        return sm


if __name__ == "__main__":
    TraderApp().run()
