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
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty

#for login page
class EcoWheelWidgets(Widget):
    pass

class EcoWheelsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette= "Cyan"
        return Builder.load_file('login_page.kv')
    def clear(self):
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

EcoWheelsApp().run()