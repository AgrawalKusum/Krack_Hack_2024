import kivy
import firebase_admin
from firebase_admin import db, credentials
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

#auathentication of firebase
'''credential=credentials.Certificate("credential.json")
firebase_admin.initialize_app(credential, {"databaseurl": "https://ecowheels-89aa9-default-rtdb.asia-southeast1.firebasedatabase.app/"})
ref=db.reference('databaseurl')
username=ref.child('users')'''
#for login page
class Your_Details(Screen):
    pass
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
    '''def registeration_deets(self):
        username.child(self.root.ids.user.text).set({"Username": self.root.ids.user.text, "Password": self.root.ids.password.text})
    def login_deets(user_name):
        username.child(user_name).get().key()'''
EcoWheelsApp().run()