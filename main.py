from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    count = 0
    count_enabled = True
    add = 1
    text = StringProperty("0")

    def on_toggle_5_state(self, widget):
        if widget.state == "down":
            widget.text = "*5:ON"
            self.add = 5
        else:
            widget.text = "*5: OFF"
            self.add = 1

    def on_toggle_enable_state(self, widget):
        if widget.state == "down":
            widget.text = "Counter lock: ON"
            self.count_enabled = False
        else:
            widget.text = "Counter lock: OFF"
            self.count_enabled = True

    def on_plus_button_click(self):
        if self.count_enabled:
            self.count += self.add
            self.text = str(self.count)

    def on_minus_button_click(self):
        if self.count_enabled:
            self.count -= self.add
            self.text = str(self.count)


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        self.padding = (dp(20), dp(20), dp(20), dp(20))
        for i in range(1, 100):
            size = dp(100)
            z = Button(text=str(i), size_hint=(None, None), size=(size, size))
            self.add_widget(z)


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    """def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)"""
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

TheLabApp().run()
