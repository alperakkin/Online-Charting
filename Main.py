from kivy.config import Config
# Config.set('graphics','width','1600') #1000
# Config.set('graphics','height','1000')#600
Config.set('graphics','borderless','1')
Config.set('graphics','resizable','0')
Config.set('graphics','fullscreen','auto')
Config.set('input','mouse','mouse,multitouch_on_demand')

# Internal Libraries
from Widget_Library import *
from Config_Screen import *

#


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty,NumericProperty,StringProperty,BooleanProperty
from kivy.animation import Animation
from kivy.core.window import Window




import csv


class OpenDialog(Popup):
    kullanici=StringProperty()
    passw=StringProperty()
    error=StringProperty()
    check=BooleanProperty()



    def __init__(self,parent,app,*args):
        super(OpenDialog,self).__init__(*args)
        self.parent = parent
        self.bind(kullanici=self.parent.setter('user'))
        self.bind(passw=self.parent.setter('passw'))
        self.bind(check=self.parent.setter('check'))
        self.app = app  # get the MainApp reference
        self.init()
    def init(self):
        self.title='Yetkili Girişi'
        self.ids.t1.text='Kullanıcı Adı: '
        self.ids.input.hint_text='Kullanıcı adınızı girin...'
        self.ids.input.font_size=12
        self.ids.t2.text="Şifre: "
        self.ids.input2.font_size = 12
        self.ids.input2.hint_text='Şifrenizi girin...'
    def on_error(self,inst,text):
        if text:
            self.lb_error.size_hint_y=None
            self.size_hint = self.size_hint

        else:
            self.lb_error.size_hint_y = None
            self.lb_error.height=0
            self.size_hint = self.size_hint



    def enter(self):
        if not self.text or not self.text2 :
            self.error="Hatalı veya eksik giriş!!"
        else:
            self.kullanici = str(self.text)
            self.passw = str(self.text2)

            if MainMenu.Read_Password(self,self.kullanici,self.passw)!=True:
                self.error = "Hatalı veya eksik giriş!!"

            else:
                self.check=True
                self.dismiss()


    def cancel(self):
        self.check=False
        self.dismiss()


class AppScreen(FloatLayout):
    app=ObjectProperty(None)


class MainMenu(AppScreen):
    def __init__(self, app):  # init the object, receiving the MainApp instance
        super(MainMenu, self).__init__()
        self.app = app  # get the MainApp reference
        self.init()
        self.ids.back.init()




    def set_pos(self, posx, posy):
        return (Window.width * posx, Window.height * posy)

    def init(self):

        self.ids.exit_button.angle = 0
        self.ids.exit_button.pos = self.set_pos(0.977, 0.005)
        self.ids.exit_button.size_hint = (0.017, 0.031)
        self.ids.configure_button.angle = 0
        self.ids.configure_button.pos = self.set_pos(0.955, 0.002)
        self.ids.configure_button.size_hint = (0.020, 0.035)

        self.ids.prt.pos = self.set_pos(0.15, 0.3)
        self.ids.prt.size_hint = (0.5, 0.5)
        self.ids.prt.init(self.ids.prt.size_hint)
























    def change_color(self,button_name,button_picture,a,b,c):
        if button_name=='s':
            self.ids.s_button.source = button_picture
            animation=Animation(size_hint=(0.075, 0.17), duration=0.5, t='out_sine')
            animation.start(self.ids.s_button)
        if button_name == 'q':
            self.ids.q_button.source = button_picture
            animation = Animation(size_hint=(0.075, 0.17), duration=0.5, t='out_sine')
            animation.start(self.ids.q_button)
        if button_name == 'd':
            self.ids.d_button.source = button_picture
            animation = Animation(size_hint=(0.075, 0.17), duration=0.5, t='out_sine')
            animation.start(self.ids.d_button)
        if button_name == 'c':
            self.ids.c_button.source = button_picture
            animation = Animation(size_hint=(0.075, 0.17), duration=0.5, t='out_sine')
            animation.start(self.ids.c_button)
        if button_name == 'e':
            self.ids.e_button.source = button_picture
            animation = Animation(size_hint=(0.075, 0.17), duration=0.5, t='out_sine')
            animation.start(self.ids.e_button)



    def anim_sinyal(self,button_name):
        if button_name=='s':
            if self.ids.s_button.sinyal==True:
                self.ids.s_button.sinyal=False
                button_picture=("picture_lib/s_kirmizi.png")
            else:
                self.ids.s_button.sinyal=True
                button_picture=("picture_lib/s_yesil.png")

            animation = Animation(size_hint=(0,0), duration=0.2, t='out_sine')
            animation.bind(on_progress=partial(self.change_color, button_name, button_picture))
            animation.start(self.ids.s_button)

        if button_name == 'q':
            if self.ids.q_button.sinyal==True:
                self.ids.q_button.sinyal=False
                button_picture=("picture_lib/q_kirmizi.png")
            else:
                self.ids.q_button.sinyal=True
                button_picture=("picture_lib/q_yesil.png")


            animation = Animation(size_hint=(0, 0), duration=0.2, t='out_sine')
            animation.bind(on_progress=partial(self.change_color, button_name, button_picture))
            animation.start(self.ids.q_button)
        if button_name == 'd':
            if self.ids.d_button.sinyal==True:
                self.ids.d_button.sinyal=False
                button_picture=("picture_lib/d_kirmizi.png")
            else:
                self.ids.d_button.sinyal=True
                button_picture=("picture_lib/d_yesil.png")

            animation = Animation(size_hint=(0, 0), duration=0.2, t='out_sine')
            animation.bind(on_progress=partial(self.change_color, button_name, button_picture))
            animation.start(self.ids.d_button)
        if button_name == 'c':
            if self.ids.c_button.sinyal==True:
                self.ids.c_button.sinyal=False
                button_picture=("picture_lib/c_kirmizi.png")
            else:
                self.ids.c_button.sinyal=True
                button_picture=("picture_lib/c_yesil.png")

            animation = Animation(size_hint=(0, 0), duration=0.2, t='out_sine')
            animation.bind(on_progress=partial(self.change_color, button_name, button_picture))
            animation.start(self.ids.c_button)
        if button_name == 'e':
            if self.ids.e_button.sinyal==True:
                self.ids.e_button.sinyal=False
                button_picture=("picture_lib/e_kirmizi.png")
            else:
                self.ids.e_button.sinyal=True
                button_picture=("picture_lib/e_yesil.png")

            animation = Animation(size_hint=(0, 0), duration=0.2, t='out_sine')
            animation.bind(on_progress=partial(self.change_color, button_name, button_picture))
            animation.start(self.ids.e_button)



    def x_app(self,*args):
        self.ids.exit_button.angle=0
        App.get_running_app().stop()

    def close_app(self):
        animation=Animation(angle=360,duration=0.2)
        animation.start(self.ids.exit_button)
        animation.bind(on_complete=self.x_app)

    def open_configure(self,*args):
        self.init()
        self.app.open_screen('configure')

    def  anim_configure(self):
        animation = Animation(angle=360, duration=0.2)
        animation.start(self.ids.configure_button)
        animation.bind(on_complete=self.open_configure)













class MainApp(App):
    def build(self):

        self.screens = {}  # list of app screens
        self.screens['menu'] = MainMenu(self)  # self the MainApp instance, so others objects can change the screen
        self.screens['configure'] = Configuration_Window(self)
        self.root = FloatLayout()


        self.open_screen('menu')
        return self.root

    def open_screen(self,name):

        self.root.clear_widgets()
        self.root.add_widget(self.screens[name])





if __name__ == '__main__':
    MainApp().run()