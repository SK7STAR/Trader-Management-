# ================================
# SK7•STAR Trader Management App
# Big Font + Slim Aqua Buttons
# Premium Codes (2025–2035) built-in
# ================================

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp
import datetime

# ---------- THEME ----------
NAVY = (8/255, 12/255, 30/255, 1)
AQUA = (0/255, 230/255, 230/255, 1)
WHITE = (1, 1, 1, 1)

Window.clearcolor = NAVY

# ---------- GLOBAL SETTINGS ----------
SETTINGS = {
    "default_risk_pct": 2.0,
    "default_fee_pct": 0.05,
    "default_leverage": 10,
    "trading_app": "Binance",
    "market_type": "Crypto",
}

APP_STATE = {
    "is_premium": False,
    "premium_until": None,
}

# ---------- BUILT-IN PREMIUM CODES (2025–2035) ----------
# Format: "YYYY-MM": "SK7STAR-XXXXX"
PREMIUM_CODES = {
    # 2025
    "2025-01": "SK7STAR-J9XQ2",
    "2025-02": "SK7STAR-M4T8Z",
    "2025-03": "SK7STAR-PQ9L7",
    "2025-04": "SK7STAR-V2RX5",
    "2025-05": "SK7STAR-K7WQ9",
    "2025-06": "SK7STAR-H5LZ2",
    "2025-07": "SK7STAR-Q8RM4",
    "2025-08": "SK7STAR-Z3KP7",
    "2025-09": "SK7STAR-R6NT9",
    "2025-10": "SK7STAR-W9JL3",
    "2025-11": "SK7STAR-T5QX8",
    "2025-12": "SK7STAR-B7MZ4",
    # 2026
    "2026-01": "SK7STAR-X4QJ9",
    "2026-02": "SK7STAR-L8WR2",
    "2026-03": "SK7STAR-C9TM5",
    "2026-04": "SK7STAR-F2VQ7",
    "2026-05": "SK7STAR-R4PK8",
    "2026-06": "SK7STAR-J6MX3",
    "2026-07": "SK7STAR-N2QR9",
    "2026-08": "SK7STAR-Y5TZ1",
    "2026-09": "SK7STAR-U7LK4",
    "2026-10": "SK7STAR-D3WX8",
    "2026-11": "SK7STAR-K5NP6",
    "2026-12": "SK7STAR-P8ZQ2",
    # 2027
    "2027-01": "SK7STAR-G6RT1",
    "2027-02": "SK7STAR-S9MP4",
    "2027-03": "SK7STAR-H3VZ7",
    "2027-04": "SK7STAR-Q5LK2",
    "2027-05": "SK7STAR-Z8JR5",
    "2027-06": "SK7STAR-M4QX9",
    "2027-07": "SK7STAR-T1WP6",
    "2027-08": "SK7STAR-R7NZ3",
    "2027-09": "SK7STAR-V2KM8",
    "2027-10": "SK7STAR-C6QP4",
    "2027-11": "SK7STAR-X9LM2",
    "2027-12": "SK7STAR-J3TZ7",
    # 2028
    "2028-01": "SK7STAR-B7RQ1",
    "2028-02": "SK7STAR-P4MX9",
    "2028-03": "SK7STAR-K2JW6",
    "2028-04": "SK7STAR-W9TZ3",
    "2028-05": "SK7STAR-N5QP8",
    "2028-06": "SK7STAR-Y3LK7",
    "2028-07": "SK7STAR-H8WM2",
    "2028-08": "SK7STAR-Q6NP4",
    "2028-09": "SK7STAR-F1ZX9",
    "2028-10": "SK7STAR-T7JR5",
    "2028-11": "SK7STAR-V4MQ1",
    "2028-12": "SK7STAR-Z8PW6",
    # 2029
    "2029-01": "SK7STAR-D6TZ8",
    "2029-02": "SK7STAR-G9LQ3",
    "2029-03": "SK7STAR-W5MR7",
    "2029-04": "SK7STAR-K2NP1",
    "2029-05": "SK7STAR-X7JW4",
    "2029-06": "SK7STAR-R3KV9",
    "2029-07": "SK7STAR-M8QZ2",
    "2029-08": "SK7STAR-J1PR6",
    "2029-09": "SK7STAR-U4WN8",
    "2029-10": "SK7STAR-L6TZ3",
    "2029-11": "SK7STAR-P8KM1",
    "2029-12": "SK7STAR-F5QX7",
    # 2030
    "2030-01": "SK7STAR-H3RM2",
    "2030-02": "SK7STAR-Q7LW9",
    "2030-03": "SK7STAR-V1JP4",
    "2030-04": "SK7STAR-C6KR8",
    "2030-05": "SK7STAR-M9TZ1",
    "2030-06": "SK7STAR-T5QP7",
    "2030-07": "SK7STAR-Y8LX3",
    "2030-08": "SK7STAR-N2JW6",
    "2030-09": "SK7STAR-Z4TM8",
    "2030-10": "SK7STAR-J7QP2",
    "2030-11": "SK7STAR-R3WX9",
    "2030-12": "SK7STAR-K5NZ4",
    # 2031
    "2031-01": "SK7STAR-P9LX1",
    "2031-02": "SK7STAR-F4WQ7",
    "2031-03": "SK7STAR-X8MR3",
    "2031-04": "SK7STAR-T2JK9",
    "2031-05": "SK7STAR-L7QP4",
    "2031-06": "SK7STAR-H1TZ6",
    "2031-07": "SK7STAR-V3NK8",
    "2031-08": "SK7STAR-Y5PX2",
    "2031-09": "SK7STAR-C9WR7",
    "2031-10": "SK7STAR-Z6MQ1",
    "2031-11": "SK7STAR-R8LK5",
    "2031-12": "SK7STAR-M4JP8",
    # 2032
    "2032-01": "SK7STAR-G2RX9",
    "2032-02": "SK7STAR-J5MQ3",
    "2032-03": "SK7STAR-P8LZ6",
    "2032-04": "SK7STAR-W3TK1",
    "2032-05": "SK7STAR-K7QP4",
    "2032-06": "SK7STAR-F1WM8",
    "2032-07": "SK7STAR-Z9JR2",
    "2032-08": "SK7STAR-Q4NX7",
    "2032-09": "SK7STAR-U6KP5",
    "2032-10": "SK7STAR-D3LZ8",
    "2032-11": "SK7STAR-X7RW1",
    "2032-12": "SK7STAR-H2MQ9",
    # 2033
    "2033-01": "SK7STAR-R5NZ4",
    "2033-02": "SK7STAR-V1JP8",
    "2033-03": "SK7STAR-B8LQ2",
    "2033-04": "SK7STAR-M4TW7",
    "2033-05": "SK7STAR-K6QP9",
    "2033-06": "SK7STAR-J3MR1",
    "2033-07": "SK7STAR-Q7LK6",
    "2033-08": "SK7STAR-Y9TX3",
    "2033-09": "SK7STAR-W2MP5",
    "2033-10": "SK7STAR-T8LZ9",
    "2033-11": "SK7STAR-P4JW2",
    "2033-12": "SK7STAR-X5RQ7",
    # 2034
    "2034-01": "SK7STAR-H9WT3",
    "2034-02": "SK7STAR-N3QP6",
    "2034-03": "SK7STAR-Z7MK1",
    "2034-04": "SK7STAR-R1LZ8",
    "2034-05": "SK7STAR-V4JR9",
    "2034-06": "SK7STAR-K8PQ2",
    "2034-07": "SK7STAR-F6TX7",
    "2034-08": "SK7STAR-D9MQ4",
    "2034-09": "SK7STAR-Q2KP8",
    "2034-10": "SK7STAR-M5LZ3",
    "2034-11": "SK7STAR-Y7WN9",
    "2034-12": "SK7STAR-J4RQ5",
    # 2035
    "2035-01": "SK7STAR-X8LQ2",
    "2035-02": "SK7STAR-P3TW9",
    "2035-03": "SK7STAR-T7MK4",
    "2035-04": "SK7STAR-V2RQ8",
    "2035-05": "SK7STAR-K9JP1",
    "2035-06": "SK7STAR-B6NQ7",
    "2035-07": "SK7STAR-Z4MW5",
    "2035-08": "SK7STAR-H1TK9",
    "2035-09": "SK7STAR-Q5JP3",
    "2035-10": "SK7STAR-F8LR6",
    "2035-11": "SK7STAR-M2WX8",
    "2035-12": "SK7STAR-R7PQ1",
}

# ---------- HELPERS ----------

def make_label(text, size=20, height=0.1, bold=False, halign="center"):
    lbl = Label(
        text=text,
        color=WHITE,
        font_size=size,
        bold=bold,
        size_hint=(1, height),
        halign=halign,
        valign="middle",
    )
    lbl.bind(size=lambda label, *_: setattr(label, "text_size", label.size))
    return lbl


def make_button(text, callback, height_dp=56, font_size=20):
    btn = Button(
        text=text,
        size_hint=(1, None),
        height=dp(height_dp),
        background_normal="",
        background_color=AQUA,
        color=WHITE,
        font_size=font_size,
        bold=True,
        border=(24, 24, 24, 24),
    )
    btn.bind(on_press=callback)
    return btn


def get_summary_text():
    return (
        f"{SETTINGS['market_type']} on {SETTINGS['trading_app']}  |  "
        f"Lev {SETTINGS['default_leverage']}x  |  "
        f"Fee {SETTINGS['default_fee_pct']}%"
    )


def get_current_month_key():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m")


# ---------- SCREENS ----------

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=10)

        title = make_label("Trader Management", size=34, height=0.16, bold=True)
        self.status_label = make_label("", size=18, height=0.10)

        root.add_widget(title)
        root.add_widget(self.status_label)

        # Spacer above buttons
        root.add_widget(Widget(size_hint_y=1))

        grid = GridLayout(
            cols=2,
            spacing=dp(12),
            size_hint=(1, None),
            padding=(0, dp(10))
        )
        grid.height = dp(3 * 56 + 2 * 12)

        grid.add_widget(make_button("Trade Entry", self.goto_trade))
        grid.add_widget(make_button("Risk Mgmt", self.goto_risk))
        grid.add_widget(make_button("Premium Tools", self.goto_premium_tools))
        grid.add_widget(make_button("Activate Premium", self.goto_activate))
        grid.add_widget(make_button("Settings", self.goto_settings))
        grid.add_widget(make_button("Help", self.goto_help))

        root.add_widget(grid)

        # Spacer below buttons
        root.add_widget(Widget(size_hint_y=1))

        self.add_widget(root)

    def on_pre_enter(self, *args):
        mode = "Premium User" if APP_STATE["is_premium"] else "Free User"
        extra = ""
        if APP_STATE["is_premium"] and APP_STATE["premium_until"]:
            extra = f" (valid until {APP_STATE['premium_until']})"
        self.status_label.text = f"Status: {mode}{extra}\n{get_summary_text()}"

    def goto_trade(self, *_):
        self.manager.current = "trade_entry"

    def goto_risk(self, *_):
        self.manager.current = "risk"

    def goto_premium_tools(self, *_):
        # Protection popup if not premium
        if not APP_STATE["is_premium"]:
            self.show_premium_popup()
        self.manager.current = "premium_tools"

    def goto_activate(self, *_):
        self.manager.current = "activate_premium"

    def goto_settings(self, *_):
        self.manager.current = "settings"

    def goto_help(self, *_):
        self.manager.current = "help"

    def show_premium_popup(self):
        box = BoxLayout(orientation="vertical", padding=15, spacing=10)
        box.add_widget(make_label(
            "Premium required to use SK7•STAR Pro tools.\n\n"
            "Enter your monthly code in 'Activate Premium'.",
            size=16, height=0.7
        ))
        btns = BoxLayout(orientation="horizontal", size_hint=(1, 0.3), spacing=10)
        popup = Popup(title="Premium Locked", content=box,
                      size_hint=(0.85, 0.5), auto_dismiss=False)

        def go_activate(*_):
            popup.dismiss()
            self.manager.current = "activate_premium"

        def close_popup(*_):
            popup.dismiss()

        btns.add_widget(make_button("Activate", go_activate, height_dp=44, font_size=16))
        btns.add_widget(make_button("Later", close_popup, height_dp=44, font_size=16))
        box.add_widget(btns)
        popup.open()


# ----- FREE TRADE ENTRY -----

class TradeEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Trade Entry & P&L (Pro)", size=28, height=0.14, bold=True))
        self.summary_label = make_label("", size=18, height=0.08)
        root.add_widget(self.summary_label)

        field_bg = (0.12, 0.14, 0.22, 1)

        self.entry = TextInput(
            hint_text="Entry Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.exit = TextInput(
            hint_text="Target / Exit Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.sl = TextInput(
            hint_text="Stop Loss (for RR)",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.qty = TextInput(
            hint_text="Quantity / Position Size",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.fee = TextInput(
            hint_text=f"Fee % per side (default {SETTINGS['default_fee_pct']})",
            text=str(SETTINGS["default_fee_pct"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )

        root.add_widget(self.entry)
        root.add_widget(self.exit)
        root.add_widget(self.sl)
        root.add_widget(self.qty)
        root.add_widget(self.fee)

        self.result = make_label(
            "Fill values and tap Calculate.",
            size=18,
            height=0.26,
            halign="left",
        )
        root.add_widget(self.result)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Calculate", self.calculate))
        grid.add_widget(make_button("Back", self.back_home))
        root.add_widget(grid)

        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.summary_label.text = get_summary_text()
        if not self.fee.text.strip():
            self.fee.text = str(SETTINGS["default_fee_pct"])

    def calculate(self, *_):
        try:
            entry = float(self.entry.text)
            exit_p = float(self.exit.text)
            sl = float(self.sl.text)
            qty = float(self.qty.text)
            fee_pct = float(self.fee.text) if self.fee.text.strip() else SETTINGS["default_fee_pct"]
            fee = fee_pct / 100.0

            direction = "LONG" if exit_p > entry else "SHORT"

            gross_pl = (exit_p - entry) * qty
            if direction == "SHORT":
                gross_pl = -gross_pl

            notional = entry * qty
            fees = notional * fee + exit_p * qty * fee
            net_pl = gross_pl - fees

            risk_per_unit = abs(entry - sl)
            risk = risk_per_unit * qty
            rr = net_pl / risk if risk > 0 else 0

            lines = [
                f"Direction: {direction}",
                f"Gross P&L: {gross_pl:.2f}",
                f"Fees (round-trip): {fees:.2f}",
                f"Net P&L: {net_pl:.2f}",
                f"RR: 1 : {abs(rr):.2f}" if rr > 0 else "RR: N/A",
            ]
            self.result.text = "\n".join(lines)
        except Exception:
            self.result.text = "Enter valid numbers for Entry, Exit, SL, Qty, and Fee."

    def back_home(self, *_):
        self.manager.current = "home"


# ----- RISK MANAGEMENT -----

class RiskScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Risk Management", size=28, height=0.14, bold=True))

        field_bg = (0.12, 0.14, 0.22, 1)

        self.account = TextInput(
            hint_text="Account Size (₹)",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.risk_pct = TextInput(
            hint_text=f"Risk % per trade (default {SETTINGS['default_risk_pct']})",
            text=str(SETTINGS["default_risk_pct"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.entry = TextInput(
            hint_text="Entry Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.sl = TextInput(
            hint_text="Stop Loss (SL)",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )

        root.add_widget(self.account)
        root.add_widget(self.risk_pct)
        root.add_widget(self.entry)
        root.add_widget(self.sl)

        self.result = make_label(
            "Enter values and Calculate.",
            size=18,
            height=0.26,
            halign="left",
        )
        root.add_widget(self.result)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Calculate", self.calculate))
        grid.add_widget(make_button("Back", self.back_home))
        root.add_widget(grid)

        self.add_widget(root)

    def calculate(self, *_):
        try:
            account = float(self.account.text)
            risk_pct = float(self.risk_pct.text) if self.risk_pct.text.strip() else SETTINGS["default_risk_pct"]
            entry = float(self.entry.text)
            sl = float(self.sl.text)

            risk_amount = account * (risk_pct / 100.0)
            risk_per_unit = abs(entry - sl)
            qty = risk_amount / risk_per_unit if risk_per_unit > 0 else 0

            self.result.text = (
                f"Risk Amount: ₹{risk_amount:.2f}\n"
                f"Risk per unit: {risk_per_unit:.4f}\n"
                f"Position Size: {qty:.4f} units"
            )
        except Exception:
            self.result.text = "Enter valid Account, Risk %, Entry and SL."

    def back_home(self, *_):
        self.manager.current = "home"


# ----- SETTINGS -----

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Settings", size=30, height=0.14, bold=True))

        field_bg = (0.12, 0.14, 0.22, 1)

        self.risk = TextInput(
            hint_text="Default Risk % per trade",
            text=str(SETTINGS["default_risk_pct"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.fee = TextInput(
            hint_text="Default Fees % per side",
            text=str(SETTINGS["default_fee_pct"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.leverage = TextInput(
            hint_text="Default Leverage (x)",
            text=str(SETTINGS["default_leverage"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.app_name = TextInput(
            hint_text="Trading App / Exchange (Delta, Binance, etc.)",
            text=SETTINGS["trading_app"],
            multiline=False,
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.market_type = TextInput(
            hint_text="Market Type (Crypto, Stocks, Forex, etc.)",
            text=SETTINGS["market_type"],
            multiline=False,
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )

        root.add_widget(self.risk)
        root.add_widget(self.fee)
        root.add_widget(self.leverage)
        root.add_widget(self.app_name)
        root.add_widget(self.market_type)

        self.info = make_label("", size=18, height=0.20, halign="left")
        root.add_widget(self.info)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Save", self.save))
        grid.add_widget(make_button("Back", self.back_home))
        root.add_widget(grid)

        self.add_widget(root)

    def save(self, *_):
        try:
            SETTINGS["default_risk_pct"] = float(self.risk.text)
            SETTINGS["default_fee_pct"] = float(self.fee.text)
            SETTINGS["default_leverage"] = float(self.leverage.text)
            SETTINGS["trading_app"] = self.app_name.text.strip() or "Binance"
            SETTINGS["market_type"] = self.market_type.text.strip() or "Crypto"

            self.info.text = (
                "Settings Saved ✅\n"
                f"Risk {SETTINGS['default_risk_pct']:.1f}% | "
                f"Fee {SETTINGS['default_fee_pct']:.2f}% | "
                f"Lev {SETTINGS['default_leverage']:.0f}x\n"
                f"{SETTINGS['market_type']} on {SETTINGS['trading_app']}"
            )
        except Exception:
            self.info.text = "Enter valid numbers for Risk, Fee, and Leverage."

    def back_home(self, *_):
        self.manager.current = "home"


# ----- ACTIVATE PREMIUM (USING BUILT-IN CODES) -----

class ActivatePremiumScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Activate Premium", size=30, height=0.14, bold=True))
        self.summary_label = make_label("", size=18, height=0.08)
        root.add_widget(self.summary_label)

        info = (
            "Price: ₹50 / 30 days\n\n"
            "Premium unlocks all SK7•STAR tools:\n"
            "• Pro calculators\n"
            "• Fees & BE tools\n"
            "• Position Size Master+\n"
            "• P&L Journal (Pro)\n"
            "• Premium alerts (future)\n\n"
            "Use your monthly SK7STAR code provided by admin."
        )
        root.add_widget(make_label(info, size=16, height=0.38, halign="left"))

        self.code_input = TextInput(
            hint_text="Enter Premium Code for this month",
            multiline=False,
            foreground_color=WHITE,
            background_color=(0.12, 0.14, 0.22, 1),
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.10),
        )
        root.add_widget(self.code_input)

        self.code_status = make_label("", size=16, height=0.18)
        root.add_widget(self.code_status)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Verify Code", self.verify_code))
        grid.add_widget(make_button("Back", self.back_home))
        root.add_widget(grid)

        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.summary_label.text = get_summary_text()
        self.code_status.text = "Enter your SK7STAR monthly code and tap Verify."

    def verify_code(self, *_):
        code_entered = self.code_input.text.strip()
        if not code_entered:
            self.code_status.text = "Please enter your premium code."
            return

        key = get_current_month_key()
        expected = PREMIUM_CODES.get(key)

        if not expected:
            self.code_status.text = (
                f"No code set for {key}.\n"
                "Update the app if needed."
            )
            return

        if code_entered == expected:
            APP_STATE["is_premium"] = True
            now = datetime.datetime.now()
            # Expiry = last day of current month
            next_month = now.replace(day=28) + datetime.timedelta(days=4)
            last_day = (next_month - datetime.timedelta(days=next_month.day)).day
            APP_STATE["premium_until"] = f"{now.year}-{now.month:02d}-{last_day:02d}"
            self.code_status.text = (
                "✅ Premium Activated!\n"
                f"Valid until {APP_STATE['premium_until']}."
            )
        else:
            self.code_status.text = "❌ Invalid code for this month."

    def back_home(self, *_):
        self.manager.current = "home"


# ----- PREMIUM TOOLS MENU -----

class PremiumToolsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Premium Tools", size=30, height=0.14, bold=True))
        self.summary_label = make_label("", size=18, height=0.08)
        root.add_widget(self.summary_label)

        # Buttons to each premium tool
        buttons = BoxLayout(orientation="vertical", spacing=10, size_hint=(1, 0.55))

        buttons.add_widget(make_button("Pro Trade Calculator", self.goto_pro_trade))
        buttons.add_widget(make_button("RR Dashboard (Pro)", self.goto_rr))
        buttons.add_widget(make_button("Fees & BE Master", self.goto_fees_be))
        buttons.add_widget(make_button("Position Size Master+", self.goto_pos_master))
        buttons.add_widget(make_button("P&L Journal (Pro)", self.goto_journal))
        buttons.add_widget(make_button("Premium Alerts (Planned)", self.goto_alerts))

        root.add_widget(buttons)

        self.bottom = make_label(
            "",
            size=16,
            height=0.16,
        )
        root.add_widget(self.bottom)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Activate Premium", self.goto_activate))
        grid.add_widget(make_button("Back", self.back_home))
        root.add_widget(grid)

        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.summary_label.text = get_summary_text()
        if APP_STATE["is_premium"]:
            self.bottom.text = "All SK7•STAR tools unlocked for this month. Trade smart, not heavy. 🧠"
        else:
            self.bottom.text = (
                "Tools are in VIEW mode only.\n"
                "Activate premium with your monthly SK7STAR code to fully use them."
            )
            # Popup when entering (extra protection)
            self.show_premium_popup()

    def show_premium_popup(self):
        if APP_STATE["is_premium"]:
            return
        box = BoxLayout(orientation="vertical", padding=15, spacing=10)
        box.add_widget(make_label(
            "Premium tools are locked.\n\n"
            "Use 'Activate Premium' and enter your SK7STAR code.",
            size=16, height=0.7
        ))
        btns = BoxLayout(orientation="horizontal", size_hint=(1, 0.3), spacing=10)
        popup = Popup(title="Premium Locked", content=box,
                      size_hint=(0.85, 0.5), auto_dismiss=False)

        def go_activate(*_):
            popup.dismiss()
            self.manager.current = "activate_premium"

        def ok_later(*_):
            popup.dismiss()

        btns.add_widget(make_button("Activate", go_activate, height_dp=44, font_size=16))
        btns.add_widget(make_button("OK", ok_later, height_dp=44, font_size=16))
        box.add_widget(btns)
        popup.open()

    # Navigation helpers (premium screens themselves will also check)
    def goto_pro_trade(self, *_):
        self.manager.current = "pro_trade"

    def goto_rr(self, *_):
        self.manager.current = "rr_dash"

    def goto_fees_be(self, *_):
        self.manager.current = "fees_be"

    def goto_pos_master(self, *_):
        self.manager.current = "pos_master"

    def goto_journal(self, *_):
        self.manager.current = "journal"

    def goto_alerts(self, *_):
        self.manager.current = "alerts"

    def goto_activate(self, *_):
        self.manager.current = "activate_premium"

    def back_home(self, *_):
        self.manager.current = "home"


# ----- PRO TRADE CALCULATOR (PREMIUM) -----

class ProTradeCalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Pro Trade Calculator", size=28, height=0.14, bold=True))
        self.summary_label = make_label("", size=18, height=0.08)
        root.add_widget(self.summary_label)

        field_bg = (0.12, 0.14, 0.22, 1)

        self.entry = TextInput(
            hint_text="Entry Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.tp1 = TextInput(
            hint_text="Target 1 Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.tp2 = TextInput(
            hint_text="Target 2 Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.tp3 = TextInput(
            hint_text="Target 3 Price (optional)",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.sl = TextInput(
            hint_text="Stop Loss",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.qty = TextInput(
            hint_text="Quantity / Position Size",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.fee = TextInput(
            hint_text=f"Fee % per side (default {SETTINGS['default_fee_pct']})",
            text=str(SETTINGS["default_fee_pct"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )

        root.add_widget(self.entry)
        root.add_widget(self.tp1)
        root.add_widget(self.tp2)
        root.add_widget(self.tp3)
        root.add_widget(self.sl)
        root.add_widget(self.qty)
        root.add_widget(self.fee)

        self.result = make_label("", size=18, height=0.30, halign="left")
        root.add_widget(self.result)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Analyse", self.calculate))
        grid.add_widget(make_button("Back", self.back_home))
        root.add_widget(grid)

        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.summary_label.text = get_summary_text()
        if not APP_STATE["is_premium"]:
            self.result.text = "Premium required. Activate with your SK7STAR code."
        else:
            self.result.text = ""

    def calculate(self, *_):
        if not APP_STATE["is_premium"]:
            self.result.text = "Premium required. Activate in 'Activate Premium'."
            return
        try:
            entry = float(self.entry.text)
            tp1 = float(self.tp1.text)
            tp2 = float(self.tp2.text)
            qty = float(self.qty.text)
            sl = float(self.sl.text)
            fee_pct = float(self.fee.text) if self.fee.text.strip() else SETTINGS["default_fee_pct"]
            fee = fee_pct / 100.0

            tps = [tp1, tp2]
            if self.tp3.text.strip():
                tps.append(float(self.tp3.text))

            lines = []
            net_pl_total = 0
            for i, tp in enumerate(tps, start=1):
                gross = (tp - entry) * qty
                direction = "LONG" if tp > entry else "SHORT"
                if direction == "SHORT":
                    gross = -gross
                notional = entry * qty
                fees = notional * fee + tp * qty * fee
                net_pl = gross - fees
                rr = net_pl / (abs(entry - sl) * qty) if abs(entry - sl) > 0 else 0
                net_pl_total += net_pl
                lines.append(
                    f"TP{i} @ {tp:.2f} | Net: {net_pl:.2f} | RR: 1:{abs(rr):.2f}"
                )

            avg_net = net_pl_total / len(tps)
            be_price = entry  # simple BE

            lines.append(f"\nAvg Net P&L: {avg_net:.2f}")
            lines.append(f"Approx Break-even price: {be_price:.4f}")

            self.result.text = "\n".join(lines)
        except Exception:
            self.result.text = "Enter valid numbers for Entry, TPs, SL, Qty and Fee."

    def back_home(self, *_):
        self.manager.current = "premium_tools"


# ----- RR DASHBOARD (PREMIUM) -----

class RrDashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("RR Dashboard (Pro)", size=28, height=0.14, bold=True))
        self.summary_label = make_label("", size=18, height=0.08)
        root.add_widget(self.summary_label)

        field_bg = (0.12, 0.14, 0.22, 1)

        self.entry = TextInput(
            hint_text="Entry Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.sl = TextInput(
            hint_text="Stop Loss",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.tp1 = TextInput(
            hint_text="Target 1 Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.tp2 = TextInput(
            hint_text="Target 2 Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )
        self.tp3 = TextInput(
            hint_text="Target 3 Price (optional)",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.08),
        )

        root.add_widget(self.entry)
        root.add_widget(self.sl)
        root.add_widget(self.tp1)
        root.add_widget(self.tp2)
        root.add_widget(self.tp3)

        self.result = make_label("", size=18, height=0.30, halign="left")
        root.add_widget(self.result)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Analyse", self.calculate))
        grid.add_widget(make_button("Back", self.back_home))
        root.add_widget(grid)

        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.summary_label.text = get_summary_text()
        if not APP_STATE["is_premium"]:
            self.result.text = "Premium required. Activate with your SK7STAR code."
        else:
            self.result.text = ""

    def _quality(self, rr):
        if rr < 1:
            return "Poor (avoid)"
        elif rr < 1.5:
            return "Average"
        elif rr < 2:
            return "Good"
        else:
            return "Very Good / A+"

    def calculate(self, *_):
        if not APP_STATE["is_premium"]:
            self.result.text = "Premium required. Activate in 'Activate Premium'."
            return
        try:
            entry = float(self.entry.text)
            sl = float(self.sl.text)
            tps = [float(self.tp1.text), float(self.tp2.text)]
            if self.tp3.text.strip():
                tps.append(float(self.tp3.text))

            risk = abs(entry - sl)
            lines = []
            max_rr = 0

            for i, tp in enumerate(tps, start=1):
                rr = abs(tp - entry) / risk if risk > 0 else 0
                max_rr = max(max_rr, rr)
                quality = self._quality(rr)
                lines.append(f"TP{i} @ {tp:.2f}  |  RR: 1:{rr:.2f}  |  Quality: {quality}")

            winrate_be = 100 / (1 + max_rr) if max_rr > 0 else 0
            lines.append(f"\nMax RR: 1:{max_rr:.2f}")
            lines.append(f"Break-even winrate ≈ {winrate_be:.1f}%")

            overall = "Good setup. Suitable for normal trading." if max_rr >= 2 else "Risk / reward is not very attractive."
            lines.append(f"Overall: {overall}")

            self.result.text = "\n".join(lines)
        except Exception:
            self.result.text = "Enter valid Entry, SL and Targets."

    def back_home(self, *_):
        self.manager.current = "premium_tools"


# ----- FEES & BE MASTER (PREMIUM) -----

class FeesBeMasterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Fees & BE Master", size=28, height=0.14, bold=True))
        self.summary_label = make_label("", size=18, height=0.08)
        root.add_widget(self.summary_label)

        field_bg = (0.12, 0.14, 0.22, 1)

        self.entry = TextInput(
            hint_text="Entry Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.exit = TextInput(
            hint_text="Exit Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.qty = TextInput(
            hint_text="Quantity",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.maker_fee = TextInput(
            hint_text="Maker fee % (per side)",
            text=str(SETTINGS["default_fee_pct"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.taker_fee = TextInput(
            hint_text="Taker fee % (per side)",
            text=str(SETTINGS["default_fee_pct"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.funding = TextInput(
            hint_text="Funding rate % (per 8h, optional)",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.hours = TextInput(
            hint_text="Hours held (optional)",
            multiline=False,
            input_filter="int",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )

        root.add_widget(self.entry)
        root.add_widget(self.exit)
        root.add_widget(self.qty)
        root.add_widget(self.maker_fee)
        root.add_widget(self.taker_fee)
        root.add_widget(self.funding)
        root.add_widget(self.hours)

        self.result = make_label("", size=18, height=0.34, halign="left")
        root.add_widget(self.result)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Analyse", self.calculate))
        grid.add_widget(make_button("Back", self.back_home))
        root.add_widget(grid)

        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.summary_label.text = get_summary_text()
        if not APP_STATE["is_premium"]:
            self.result.text = "Premium required. Activate with your SK7STAR code."
        else:
            self.result.text = ""

    def calculate(self, *_):
        if not APP_STATE["is_premium"]:
            self.result.text = "Premium required. Activate in 'Activate Premium'."
            return
        try:
            entry = float(self.entry.text)
            exit_p = float(self.exit.text)
            qty = float(self.qty.text)
            maker = float(self.maker_fee.text) / 100.0
            taker = float(self.taker_fee.text) / 100.0

            funding_rate = float(self.funding.text) / 100.0 if self.funding.text.strip() else 0.0
            hours = int(self.hours.text) if self.hours.text.strip() else 0

            notional = entry * qty
            entry_fee = notional * maker
            exit_fee = exit_p * qty * taker

            funding_fee = 0.0
            if funding_rate and hours:
                periods = hours / 8.0
                funding_fee = notional * funding_rate * periods

            total_fees = entry_fee + exit_fee + funding_fee

            gross_pl = (exit_p - entry) * qty
            net_pl = gross_pl - total_fees

            be_price = entry + (total_fees / qty) if qty > 0 else entry

            lines = [
                f"Entry fee (maker): {entry_fee:.4f}",
                f"Exit fee (taker): {exit_fee:.4f}",
                f"Funding fee: {funding_fee:.4f}",
                f"Total fees: {total_fees:.4f}",
                "",
                f"Gross P&L: {gross_pl:.4f}",
                f"Net P&L (after all fees): {net_pl:.4f}",
                f"Break-even price (fees+funding): {be_price:.4f}",
            ]
            self.result.text = "\n".join(lines)
        except Exception:
            self.result.text = "Enter valid prices, quantity and fee values."

    def back_home(self, *_):
        self.manager.current = "premium_tools"


# ----- POSITION SIZE MASTER+ (PREMIUM) -----

class PositionSizeMasterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Position Size Master+", size=28, height=0.14, bold=True))
        self.summary_label = make_label("", size=18, height=0.08)
        root.add_widget(self.summary_label)

        field_bg = (0.12, 0.14, 0.22, 1)

        self.account = TextInput(
            hint_text="Account Size (₹)",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.risk_pct = TextInput(
            hint_text=f"Total risk % (default {SETTINGS['default_risk_pct']})",
            text=str(SETTINGS["default_risk_pct"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.trades = TextInput(
            hint_text="Number of trades (1–3)",
            text="2",
            multiline=False,
            input_filter="int",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )

        root.add_widget(self.account)
        root.add_widget(self.risk_pct)
        root.add_widget(self.trades)

        self.trade_inputs = []
        for i in range(1, 4):
            root.add_widget(make_label(
                f"Trade {i}" + (" (optional)" if i > 1 else ""),
                size=20, height=0.06, bold=True, halign="left"
            ))
            entry = TextInput(
                hint_text="Entry Price",
                multiline=False,
                input_filter="float",
                foreground_color=WHITE,
                background_color=field_bg,
                cursor_color=WHITE,
                font_size=20,
                size_hint=(1, 0.07),
            )
            sl = TextInput(
                hint_text="Stop Loss",
                multiline=False,
                input_filter="float",
                foreground_color=WHITE,
                background_color=field_bg,
                cursor_color=WHITE,
                font_size=20,
                size_hint=(1, 0.07),
            )
            root.add_widget(entry)
            root.add_widget(sl)
            self.trade_inputs.append((entry, sl))

        self.result = make_label("", size=18, height=0.32, halign="left")
        root.add_widget(self.result)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Calculate", self.calculate))
        grid.add_widget(make_button("Back", self.back_home))
        root.add_widget(grid)

        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.summary_label.text = get_summary_text()
        if not APP_STATE["is_premium"]:
            self.result.text = "Premium required. Activate with your SK7STAR code."
        else:
            self.result.text = ""

    def calculate(self, *_):
        if not APP_STATE["is_premium"]:
            self.result.text = "Premium required. Activate in 'Activate Premium'."
            return
        try:
            account = float(self.account.text)
            risk_pct = float(self.risk_pct.text)
            total_trades = int(self.trades.text)
            total_trades = max(1, min(3, total_trades))

            total_risk = account * (risk_pct / 100.0)
            risk_per_trade = total_risk / total_trades

            lines = [
                f"Account: ₹{account:.2f}",
                f"Total risk: {risk_pct:.2f}%  →  ₹{total_risk:.2f}",
                f"Active trades: {total_trades}  |  Risk per trade: ₹{risk_per_trade:.2f}",
                ""
            ]

            for idx in range(total_trades):
                entry_text, sl_text = self.trade_inputs[idx]
                if not entry_text.text.strip() or not sl_text.text.strip():
                    continue
                entry = float(entry_text.text)
                sl = float(sl_text.text)
                ru = abs(entry - sl)
                size = risk_per_trade / ru if ru > 0 else 0
                lines.append(
                    f"Trade {idx+1}: Entry {entry:.4f} | SL {sl:.4f}\n"
                    f"Risk per unit: {ru:.4f}  |  Position Size: {size:.4f} units\n"
                )

            self.result.text = "\n".join(lines)
        except Exception:
            self.result.text = "Enter valid account, risk and trade prices."

    def back_home(self, *_):
        self.manager.current = "premium_tools"


# ----- P&L JOURNAL (PREMIUM) -----

class PlJournalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.trades = []

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("P&L Journal (Pro)", size=28, height=0.14, bold=True))
        self.summary_label = make_label("", size=20, height=0.08)
        root.add_widget(self.summary_label)

        field_bg = (0.12, 0.14, 0.22, 1)

        self.date = TextInput(
            hint_text="Date (optional, e.g. 2025-12-10)",
            multiline=False,
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.symbol = TextInput(
            hint_text="Symbol (e.g. ETH, BTC)",
            multiline=False,
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.direction = TextInput(
            hint_text="Direction (long / short)",
            multiline=False,
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.entry = TextInput(
            hint_text="Entry Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.exit = TextInput(
            hint_text="Exit Price",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.qty = TextInput(
            hint_text="Quantity / Size",
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.fee = TextInput(
            hint_text=f"Fee % per side (default {SETTINGS['default_fee_pct']})",
            text=str(SETTINGS["default_fee_pct"]),
            multiline=False,
            input_filter="float",
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=20,
            size_hint=(1, 0.07),
        )
        self.note = TextInput(
            hint_text="Note (optional: setup, emotions, etc.)",
            multiline=True,
            foreground_color=WHITE,
            background_color=field_bg,
            cursor_color=WHITE,
            font_size=18,
            size_hint=(1, 0.12),
        )

        root.add_widget(self.date)
        root.add_widget(self.symbol)
        root.add_widget(self.direction)
        root.add_widget(self.entry)
        root.add_widget(self.exit)
        root.add_widget(self.qty)
        root.add_widget(self.fee)
        root.add_widget(self.note)

        self.stats_label = make_label("", size=20, height=0.09)
        root.add_widget(self.stats_label)

        self.trades_label = make_label("", size=18, height=0.22, halign="left")
        root.add_widget(self.trades_label)

        grid = GridLayout(cols=2, spacing=dp(15), size_hint=(1, None))
        grid.height = dp(70)
        grid.add_widget(make_button("Save Trade", self.save_trade, font_size=20))
        grid.add_widget(make_button("Back", self.back_home, font_size=20))
        root.add_widget(grid)

        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.summary_label.text = get_summary_text()
        self._update_stats()

    def save_trade(self, *_):
        if not APP_STATE["is_premium"]:
            self.stats_label.text = "Premium required. Activate premium to save trades."
            return
        try:
            entry = float(self.entry.text)
            exit_p = float(self.exit.text)
            qty = float(self.qty.text)
            fee_pct = float(self.fee.text) if self.fee.text.strip() else SETTINGS["default_fee_pct"]
            fee = fee_pct / 100.0

            direction = self.direction.text.strip().upper() or "LONG"

            gross = (exit_p - entry) * qty
            if "SHORT" in direction:
                gross = -gross

            notional = entry * qty
            notional_exit = exit_p * qty
            fees = (notional + notional_exit) * fee
            net_pl = gross - fees

            trade = {
                "date": self.date.text.strip() or datetime.datetime.now().strftime("%Y-%m-%d"),
                "symbol": self.symbol.text.strip().upper() or "-",
                "direction": direction,
                "entry": entry,
                "exit": exit_p,
                "qty": qty,
                "net_pl": net_pl,
            }
            self.trades.append(trade)

            self.entry.text = ""
            self.exit.text = ""
            self.qty.text = ""
            self.note.text = ""

            self._update_stats()
        except Exception:
            self.stats_label.text = "Error: enter valid Entry, Exit and Qty."

    def _update_stats(self):
        if not self.trades:
            self.stats_label.text = "No trades saved yet."
            self.trades_label.text = ""
            return

        total = len(self.trades)
        wins = sum(1 for t in self.trades if t["net_pl"] > 0)
        net = sum(t["net_pl"] for t in self.trades)
        winrate = (wins / total) * 100

        self.stats_label.text = f"Trades: {total} | Wins: {wins} | Winrate: {winrate:.1f}% | Total Net P&L: {net:.2f}"

        lines = []
        for i, t in enumerate(self.trades[-5:], start=max(1, total - 4)):
            lines.append(
                f"{i}. {t['date']} {t['symbol']} {t['direction']} | "
                f"E {t['entry']:.2f} → X {t['exit']:.2f} | Qty {t['qty']:.2f} | Net: {t['net_pl']:.2f}"
            )

        self.trades_label.text = "\n".join(lines)

    def back_home(self, *_):
        self.manager.current = "premium_tools"


# ----- PREMIUM ALERTS (PLANNED) -----

class PremiumAlertsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Premium Alerts (Planned)", size=28, height=0.14, bold=True))
        self.summary_label = make_label("", size=18, height=0.08)
        root.add_widget(self.summary_label)

        text = (
            "This screen is a preview of future SK7•STAR alerts.\n\n"
            "Ideas for Premium Alerts:\n"
            "• Daily Risk Alert → warns if you risk more than your limit.\n"
            "• Drawdown Alert → when account is down X% from peak.\n"
            "• Win/Loss Streak Alert → pause trading after N losses in a row.\n"
            "• Time Alert → remind you to stop trading at your cutoff time.\n\n"
            "When alerts are implemented, you will be able to set:\n"
            "• Max daily risk %\n"
            "• Max weekly drawdown %\n"
            "• Max trades per day\n"
            "• Notification style (popup / sound / message).\n\n"
            "For now this is information only — alerts will come in a future update."
        )

        root.add_widget(make_label(text, size=18, height=0.66, halign="left"))

        root.add_widget(make_button("Back", self.back_home))

        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.summary_label.text = get_summary_text()

    def back_home(self, *_):
        self.manager.current = "premium_tools"


# ----- HELP SCREEN -----

class HelpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        root.add_widget(make_label("Help & Info", size=30, height=0.16, bold=True))

        text = (
            "SK7•STAR Trader Management App\n\n"
            "Free tools:\n"
            "• Trade Entry & P&L\n"
            "• Risk Management\n"
            "• Settings\n\n"
            "Premium tools:\n"
            "• Pro Trade Calculator\n"
            "• RR Dashboard (Pro)\n"
            "• Fees & BE Master\n"
            "• Position Size Master+\n"
            "• P&L Journal (Pro)\n"
            "• Premium Alerts (future only)\n\n"
            "Activate premium using the monthly SK7STAR code\n"
            "on the 'Activate Premium' screen."
        )
        root.add_widget(make_label(text, size=18, height=0.66, halign="left"))

        root.add_widget(make_button("Back", self.back_home))

        self.add_widget(root)

    def back_home(self, *_):
        self.manager.current = "home"


# ---------- APP ----------

class TraderApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(TradeEntryScreen(name="trade_entry"))
        sm.add_widget(RiskScreen(name="risk"))
        sm.add_widget(SettingsScreen(name="settings"))
        sm.add_widget(ActivatePremiumScreen(name="activate_premium"))
        sm.add_widget(PremiumToolsScreen(name="premium_tools"))
        sm.add_widget(ProTradeCalculatorScreen(name="pro_trade"))
        sm.add_widget(RrDashboardScreen(name="rr_dash"))
        sm.add_widget(FeesBeMasterScreen(name="fees_be"))
        sm.add_widget(PositionSizeMasterScreen(name="pos_master"))
        sm.add_widget(PlJournalScreen(name="journal"))
        sm.add_widget(PremiumAlertsScreen(name="alerts"))
        sm.add_widget(HelpScreen(name="help"))
        return sm


if __name__ == "__main__":
    TraderApp().run()