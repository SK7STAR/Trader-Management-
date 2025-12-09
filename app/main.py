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
            size_hint=(1, 0.13)
        )
        calc_btn.bind(on_press=self._calculate_basic)
        layout.add_widget(calc_btn)

        # Back to Home
        back_btn = Button(
            text="⬅ Back to Home",
            size_hint=(1, 0.13)
        )
        back_btn.bind(on_press=self.go_back_home)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def _calculate_basic(self, *_):
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

    def go_back_home(self, *_):
        self.manager.current = "home"


# -----------------------------
# Risk Management Screen
# -----------------------------
class RiskManagementScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        title = Label(
            text="Risk Management (Basic Demo)",
            font_size="20sp",
            size_hint=(1, 0.12)
        )
        layout.add_widget(title)

        # Account size
        self.account_input = TextInput(
            hint_text="Account size (₹)",
            multiline=False,
            size_hint=(1, 0.12),
            input_filter="float"
        )
        layout.add_widget(self.account_input)

        # Risk percent
        self.risk_percent_input = TextInput(
            hint_text="Risk % per trade (e.g. 2)",
            multiline=False,
            size_hint=(1, 0.12),
            input_filter="float"
        )
        layout.add_widget(self.risk_percent_input)

        # Entry & SL prices
        self.entry_input = TextInput(
            hint_text="Entry price",
            multiline=False,
            size_hint=(1, 0.12),
            input_filter="float"
        )
        layout.add_widget(self.entry_input)

        self.sl_input = TextInput(
            hint_text="Stop Loss (SL)",
            multiline=False,
            size_hint=(1, 0.12),
            input_filter="float"
        )
        layout.add_widget(self.sl_input)

        # Result label
        self.result_label = Label(
            text="Enter values and tap Calculate.",
            font_size="14sp",
            size_hint=(1, 0.18)
        )
        layout.add_widget(self.result_label)

        # Calculate button
        calc_btn = Button(
            text="Calculate Safe Position Size",
            size_hint=(1, 0.13)
        )
        calc_btn.bind(on_press=self._calculate_risk)
        layout.add_widget(calc_btn)

        # Back to Home
        back_btn = Button(
            text="⬅ Back to Home",
            size_hint=(1, 0.13)
        )
        back_btn.bind(on_press=self.go_back_home)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def _calculate_risk(self, *_):
        try:
            account_size = float(self.account_input.text)
            risk_percent = float(self.risk_percent_input.text)
            entry = float(self.entry_input.text)
            sl = float(self.sl_input.text)

            per_unit_risk = abs(entry - sl)
            if per_unit_risk == 0:
                self.result_label.text = "Entry and SL cannot be the same."
                return

            max_loss = account_size * (risk_percent / 100.0)
            position_size = max_loss / per_unit_risk

            self.result_label.text = (
                f"Max loss allowed: ₹{max_loss:.2f}\n"
                f"Risk per unit: {per_unit_risk:.2f}\n"
                f"Recommended position size: {position_size:.4f} units"
            )
        except ValueError:
            self.result_label.text = "Please fill all fields with valid numbers."

    def go_back_home(self, *_):
        self.manager.current = "home"


# -----------------------------
# Premium Tools Screen (UI only, locked feel)
# -----------------------------
class PremiumToolsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        title = Label(
            text="Premium Tools (Locked Demo)",
            font_size="20sp",
            size_hint=(1, 0.15)
        )
        layout.add_widget(title)

        info = Label(
            text=(
                "Premium features planned:\n"
                "- Advanced profit calculator\n"
                "- Fees analysis\n"
                "- Capital growth, journal, export\n\n"
                "Upgrade to premium to unlock in future versions."
            ),
            font_size="14sp",
            size_hint=(1, 0.55)
        )
        layout.add_widget(info)

        back_btn = Button(
            text="⬅ Back to Home",
            size_hint=(1, 0.15)
        )
        back_btn.bind(on_press=self.go_back_home)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_back_home(self, *_):
        self.manager.current = "home"


# -----------------------------
# Activate Premium Screen (UI only, payment planned)
# -----------------------------
class ActivatePremiumScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        title = Label(
            text="Activate Premium",
            font_size="20sp",
            size_hint=(1, 0.15)
        )
        layout.add_widget(title)

        plan = Label(
            text=(
                "Plan: ₹50 / 30 days\n\n"
                "Premium will unlock:\n"
                "- Advanced calculators\n"
                "- Fees system\n"
                "- Growth & journal tools\n\n"
                "Payment gateway integration is planned.\n"
                "In future, this button will start the real payment."
            ),
            font_size="14sp",
            size_hint=(1, 0.55)
        )
        layout.add_widget(plan)

        fake_pay_btn = Button(
            text="(Demo) Pay ₹50 & Unlock Premium",
            size_hint=(1, 0.15)
        )
        fake_pay_btn.bind(on_press=self._demo_payment)
        layout.add_widget(fake_pay_btn)

        back_btn = Button(
            text="⬅ Back to Home",
            size_hint=(1, 0.15)
        )
        back_btn.bind(on_press=self.go_back_home)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def _demo_payment(self, *_):
        print("[APP] In future this will start the real payment flow via backend + gateway.")

    def go_back_home(self, *_):
        self.manager.current = "home"


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

        # Trade Entry navigation
        btn_trade = Button(
            text="Trade Entry & P&L",
            size_hint=(1, 0.13)
        )
        btn_trade.bind(on_press=self.open_trade_entry)
        layout.add_widget(btn_trade)

        # Risk Management navigation
        btn_risk = Button(
            text="Risk Management",
            size_hint=(1, 0.13)
        )
        btn_risk.bind(on_press=self.open_risk_management)
        layout.add_widget(btn_risk)

        # Premium Tools navigation
        btn_premium_tools = Button(
            text="Premium Tools (Locked Demo)",
            size_hint=(1, 0.13)
        )
        btn_premium_tools.bind(on_press=self.open_premium_tools)
        layout.add_widget(btn_premium_tools)

        # Activate Premium navigation
        btn_activate = Button(
            text="Activate Premium (Planned)",
            size_hint=(1, 0.13)
        )
        btn_activate.bind(on_press=self.open_activate_premium)
        layout.add_widget(btn_activate)

        # Settings placeholder
        btn_settings = Button(
            text="Settings & Help (soon)",
            size_hint=(1, 0.13)
        )
        btn_settings.bind(on_press=lambda x: self._placeholder("Settings & Help"))
        layout.add_widget(btn_settings)

        self.add_widget(layout)

    def open_trade_entry(self, *_):
        self.manager.current = "trade_entry"

    def open_risk_management(self, *_):
        self.manager.current = "risk_management"

    def open_premium_tools(self, *_):
        self.manager.current = "premium_tools"

    def open_activate_premium(self, *_):
        self.manager.current = "activate_premium"

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
        sm.add_widget(RiskManagementScreen(name="risk_management"))
        sm.add_widget(PremiumToolsScreen(name="premium_tools"))
        sm.add_widget(ActivatePremiumScreen(name="activate_premium"))
        return sm


if __name__ == "__main__":
    TraderApp().run()reen):
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
