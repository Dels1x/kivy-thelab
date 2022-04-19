from kivy.app import App
from kivy.core.audio import SoundLoader
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


class WidgetsExample(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.tilt, 1 / 3)

    SoundLoader.load("Shadowraze.mp3").play()

    count = 1007
    text = StringProperty(f"{count} - 7")

    def tilt(self, *args):
        self.count -= 7
        self.text = f"{self.count} - 7"


class TheLabApp(App):
    pass

# ya durik

TheLabApp().run()
