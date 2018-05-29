
from Main import *
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.core.window import Window

class AppScreen(FloatLayout):
    app=ObjectProperty(None)

class Configuration_Window(AppScreen):
    def __init__(self, app):  # init the object, receiving the MainApp instance
        super(Configuration_Window, self).__init__()
        self.app = app  # get the MainApp reference
        self.init()
        self.ids.back.init()
        self.ids.back.children[0].text=''

    def set_pos(self,posx,posy):
        return (Window.width*posx,Window.height*posy)


    def set_color(self,status):
        if status==True:
            return (1, 1, 1, 1)
        else:
            return (0.5, 0.5, 0.5, 1)


    def init(self):



        self.ids.exit_button.angle = 0
        self.ids.exit_button.pos = self.set_pos(.96,0.94)
        self.ids.exit_button.size_hint = (0.020, 0.035)







    def open_window(self,i):

        if i==0:
            self.init()
            self.app.open_screen('menu')
        elif i==1:
            self.init()
            self.app.open_screen('password')



    def x_app(self, *args):
        self.ids.exit_button.angle = 0
        App.get_running_app().stop()

    def close_app(self):
        animation = Animation(angle=360, duration=0.2)
        animation.start(self.ids.exit_button)
        animation.bind(on_complete=self.x_app)

    def connect_device(self):
        print("Cihaza Bağlanıldı")



