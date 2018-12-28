from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

import pygame


def lade_lied():
    file = 'C:\P\P\musictagger\inputmusic\song.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)


def play_song(instance):
    pygame.mixer.music.play()


def pause_song(instance):
    pygame.mixer.music.pause()


def forward_song(instance, motionevent):
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(instance.value)


class EditScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(EditScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 5

        self.add_widget(Label(text='Name Lied'))
        self.add_widget(self.erstelle_lied_leiste())

        song_position = Slider(min=0, max=100)
        song_position.step = 1
        song_position.bind(on_touch_up=forward_song)
        self.add_widget(song_position)

        self.add_widget(self.erstelle_tag_leiste())

    def erstelle_tag_leiste(self):
        tag_leiste = BoxLayout(spacing=5)

        btn1 = ToggleButton(text='Rawstyle', group='gender')
        tag_leiste.add_widget(btn1)

        btn2 = ToggleButton(text='Euphoric', group='gender')
        tag_leiste.add_widget(btn2)

        btn3 = ToggleButton(text='Symphonic')
        tag_leiste.add_widget(btn3)

        btn4 = ToggleButton(text='Karneval')
        tag_leiste.add_widget(btn4)

        return tag_leiste


    def erstelle_lied_leiste(self):
        liedleiste = BoxLayout(spacing=5)
        btn1 = Button(text='Prev')
        liedleiste.add_widget(btn1)

        btn2 = Button(text='Play')
        liedleiste.add_widget(btn2)
        btn2.bind(on_press=play_song)

        btn3 = Button(text='Pause')
        liedleiste.add_widget(btn3)
        btn3.bind(on_press=pause_song)

        btn4 = Button(text='Next')
        liedleiste.add_widget(btn4)

        return liedleiste




class MyApp(App):

    def build(self):
        return EditScreen()


if __name__ == '__main__':
    lade_lied()
    MyApp().run()
