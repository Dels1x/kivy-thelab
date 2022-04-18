from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 1)
            Line(points=(400, 0, 100, 100, 400, 200), width=2)
            Color(1, 1, 0)
            Line(circle=(400, 200, 100), width=4)
            Color(1, 0, 1)
            Line(points=(400, 200, 100, 300, 400, 400), width=2)
            Line(rectangle=(200, 100, 400, 206))
            Color(0.6, 0.2, 1)
            self.rect = Rectangle(pos=(300, 200), size=(50, 90))

    def on_button_click(self):
        inc = 16
        diff = self.width - (self.rect.size[0] + self.rect.pos[0])

        if diff < inc:
            inc = diff

        if self.rect.pos[0] < self.width - self.rect.size[0]:
            self.rect.pos = (self.rect.pos[0] + inc, self.rect.pos[1])
        else:
            self.rect.pos = (self.width - self.rect.size[0], self.rect.pos[1])


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = (dp(50), dp(62))
        with self.canvas:
            self.egg = Ellipse(pos=self.center, size=self.ball_size)

        Clock.schedule_interval(self.update, 1 / 66)

    def on_size(self, *args):
        print(f"Window size: {self.width}x{self.height}")
        self.egg.pos = (self.center[0] - self.ball_size[0] / 2, self.center[1] - self.ball_size[1] / 2)

    def update(self, dt):
        self.egg.pos = (self.egg.pos[0] + 1, self.egg.pos[1])


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class WidgetsExample(GridLayout):
    count = 0
    count_enabled = BooleanProperty(True)
    add = 1
    text = StringProperty("0")
    slider_text = StringProperty("50")
    text_input = StringProperty("Welcome to da hood")

    def on_toggle_5_state(self, widget):
        if widget.state == "down":
            widget.text = "*5:ON"
            self.add = 5
        else:
            widget.text = "*5: OFF"
            self.add = 1

    def on_toggle_enable_state(self, widget):
        if widget.state == "down":
            widget.text = "Lock: ON"
            self.count_enabled = False
        else:
            widget.text = "Lock: OFF"
            self.count_enabled = True

    def on_plus_button_click(self):
        self.count += self.add
        self.text = str(self.count)

    def on_minus_button_click(self):
        self.count -= self.add
        self.text = str(self.count)

    def on_text_input_validate(self, widget):
        self.text_input = widget.text


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

# ya durik

TheLabApp().run()
