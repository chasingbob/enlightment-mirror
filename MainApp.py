import datetime
import weather
import route

import os
#os.environ['KIVY_WINDOW'] = 'sdl2'
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

Builder.load_file('Main.kv')

class TimeWidget(Widget):
    time = StringProperty()
    date = StringProperty()

    def update(self, *args):
        self.date = datetime.date.today().strftime("%A, %d %B %Y")
        self.time = datetime.datetime.now().strftime("%H:%M")

class TrafficWidget(Widget):
    duration = StringProperty('')
    distance = StringProperty('')

    def update(self, *args):
        dis,dur = route.get_current_traffic('2 Impala ave sandton', '39 Rivonia Rd sandton')
        self.duration = dur
        self.distance = dis


class WeatherWidget(Widget):
    temperature = StringProperty()
    description = StringProperty()
    imgpath = StringProperty()

    def update(self, *args):
        temp,desc,_icon = weather.get_current_weather()
        t = '{0}{1}C'.format(temp,u'\xb0')
        self.temperature = t
        self.description = desc
        self.imgpath = _icon



class Container(FloatLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

        anchor_tr = AnchorLayout(anchor_x='right', anchor_y='top', size_hint=(1,1))
        tw = TimeWidget()
        tw.update()
        Clock.schedule_interval(tw.update,60)
        anchor_tr.add_widget(tw)
        self.add_widget(anchor_tr)

        anchor_rc = AnchorLayout(anchor_x='right', anchor_y='center')
        ww = WeatherWidget()
        ww.update()
        Clock.schedule_interval(ww.update,300)
        anchor_rc.add_widget(ww)
        self.add_widget(anchor_rc)

        anchor_lc = AnchorLayout(anchor_x='left', anchor_y='top')
        tw = TrafficWidget()
        tw.update()
        Clock.schedule_interval(tw.update,300)
        anchor_lc.add_widget(tw)
        self.add_widget(anchor_lc)




class MainApp(App):
    def build(self):
        cc = Container()
        return cc

if __name__ == "__main__":
    MainApp().run()
