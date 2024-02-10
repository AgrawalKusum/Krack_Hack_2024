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
from kivy.uix.screenmanager import ScreenManager, Screen

#for login page
class EntryChoice(Screen):
    pass
class Registration(Screen):
    pass

class Login(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class EcoWheelsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette= "Cyan"
        return Builder.load_file('login_page.kv')
    def clear(self):
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
        return None
    '''def switch_screen(self):
        screen_manager = self.root.ids.screen_manager
        current_screen = screen_manager.current
        if current_screen == 'screen1':
            screen_manager.current = 'screen2'
        else: screen_manager.current = 'screen1'''

EcoWheelsApp().run()