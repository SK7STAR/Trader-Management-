from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class TraderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        title = Label(
            text="📱 Trader Management App",
            font_size='24sp'
        )
        layout.add_widget(title)
        return layout


if __name__ == "__main__":
    TraderApp().run()
