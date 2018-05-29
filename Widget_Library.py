from Main import *
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from functools import partial
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.scrollview import ScrollView
import datetime
from kivy.graphics import Color
from kivy.clock import Clock
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
import numpy as np
import matplotlib.pyplot as plt
from kivy.core.window import Window











class Background(FloatLayout):


    def set_pos(self, posx, posy):
        return (Window.width * posx, Window.height * posy)

    def update_time(self, dt):

        self.children[1].text = str(datetime.datetime.now().strftime('%d-%m-%Y'))
        self.children[2].text = str(datetime.datetime.now().strftime('%H: %M: %S'))











    def init(self):
        self.add_widget(Image(), 3)
        for i in range(3):
            self.add_widget(Label(),i)
            self.children[i].halign = 'left'
            self.children[i].valign = 'middle'
            self.children[i].color = (0.8, 0.8, 0.8, 1)
            self.children[i].font_size = 12
            self.children[i].size_hint = 0.05, 0.05





        self.children[3].allow_stretch = True
        self.children[3].keep_ratio = False
        self.children[3].size_hint = self.parent.size_hint
        self.children[3].pos = self.set_pos(0,0)
        self.children[3].source= "picture_lib/Background.png"


        self.children[0].color = (0.8, 0.8, 0.1, 1)
        self.children[0].pos=self.set_pos(0.25,-0.005)
        self.children[0].font_size = 26
        self.children[0].text="Online Measurement"






        Clock.schedule_interval(self.update_time,1)
        self.children[1].pos=self.set_pos(0.90,0.000)
        self.children[2].pos = self.set_pos(0.90, -0.015)
        self.children[1].font_size = 10
        self.children[2].font_size = 10


class Sliding_Menu(ScrollView):

    pass


class ImageButton(ButtonBehavior, Image):
    angle = NumericProperty(0)
    pass


class CheckBox(CheckBox):
    pass


class TextInput(TextInput):
    pass




class Label(Label):
    pass


class Inputs_Widget(GridLayout):
    def __init__(self,*args):
        super(Inputs_Widget, self).__init__(*args)

        self.rows = 1
        self.add_widget(TextInput(size_hint=(None, None), size=(Window.width*0.1,Window.height*0.042), multiline=False))
        self.add_widget(TextInput(size_hint=(None, None), size=(Window.width*0.1,Window.height*0.042), multiline=False))
        self.add_widget(TextInput(size_hint=(None, None), size=(Window.width*0.06,Window.height*0.042), multiline=False))
        self.add_widget(TextInput(size_hint=(None, None), size=(Window.width*0.1,Window.height*0.042), multiline=False))
        self.add_widget(TextInput(size_hint=(None, None), size=(Window.width*0.1,Window.height*0.042), multiline=False))
        self.add_widget(ImageButton(source='picture_lib/add.png'))
        self.add_widget(ImageButton(source='picture_lib/save.png'))
        self.add_widget(ImageButton(source='picture_lib/arrow.png'))
        self.size_hint_y = None
        self.height = 31
        self.spacing = 10

class pareto_panel(BoxLayout):
        def set_pos(self, posx, posy):
            return (Window.width * posx, Window.height * posy)

        def update(self):
                Clock.schedule_interval(self.plot, 1)

        def plot(self,state):

            import matplotlib.pyplot as plt
            import matplotlib.animation as animation
            import matplotlib.patches as mpatches
            from matplotlib import style
            import pandas as pd
            from mpldatacursor import datacursor

            style.use('fivethirtyeight')

            fig = plt.gcf()
            fig.canvas.draw()
            ax1 = fig.add_subplot(1, 1, 1)
            ax2 = fig.add_subplot(1, 1, 1)
            graph_data = pd.read_csv('data.csv')
            xs = []
            ys = []
            ys1 = []

            for line in range(len(graph_data)):
                xs.append(graph_data['Time'][line])
                ys.append(graph_data['Value1'][line])
                ys1.append(graph_data['Value2'][line])

            ax1.clear()
            ax2.clear()
            ax1.stackplot(xs, ys, color='#e20000', alpha=0.5, linewidth=2)
            ax2.stackplot(xs, ys1, color='#f92727', alpha=0.5, linewidth=2)
            ax1.set_ylim([1400, 2000])
            ax2.set_ylim([1400, 2000])
            ax1.set_xlim([min(xs), max(xs)])
            ax1.set_facecolor('#050001')

            # creating the legend manually
            plt.legend([mpatches.Patch(color='#e20000'),
                        mpatches.Patch(color='#f92727')],
                       ['meas_1', 'meas_2'])




        def init(self,size):



            self.orientation='horizontal'


            self.update()


            self.children[0].add_widget(FigureCanvasKivyAgg(plt.gcf()))


















class Aksiyon_Paneli(FloatLayout):


    def add_new(self,state):

                self.children[0].children[0].add_widget(Inputs_Widget())
                self.children[0].children[0].size=(self.children[0].children[0].size[0],self.children[0].children[0].size[1]+20)
                for child in range(len(self.children[0].children[0].children)):
                    self.children[0].children[0].children[child].children[2].bind(on_press=self.add_new)

    def init(self,size):
        self.cols=1
        self.spacing=10
        self.size_hint_y=None
        self.size=size


        self.add_widget(ImageButton(),1) # Panel View
        self.add_widget(Sliding_Menu(),0) # Sliding Menu

        self.children[1].source='picture_lib/action_panel.png'
        self.children[1].size_hint_y=None
        self.children[1].allow_stretch=True
        self.children[1].keep_ratio=False
        self.children[1].height=40

        self.children[0].children[0].size=(self.size[0],self.size[1]*1.1)
        self.children[0].pos=(self.pos[0],self.pos[1]*0.78)
        self.children[1].pos = (self.pos[0], (self.pos[1] * 0.78+self.height+10))




        for i in range(3):
            self.add_new(1)


















