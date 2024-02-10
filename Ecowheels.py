import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty

class EcoWheelWidgets(Widget):
    pass

class EcoWheelsApp(App):
    def build(self):
        return EcoWheelWidgets()
EcoWheelsApp.run()