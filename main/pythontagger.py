from os import listdir
import os

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

import pygame

song_ordner = "C:\P\P\musictagger\inputmusic\\"
directory_files = listdir(song_ordner)
watched_song_index = 0

name_of_current_song = ""

def get_currend_song_path():
    return song_ordner + 'currentsong.mp3'


def get_current_song_real_path():
    return song_ordner + str(directory_files[watched_song_index])


def lade_lied():
    name_of_current_song = str(directory_files[watched_song_index])
    os.rename(get_current_song_real_path(), get_currend_song_path())

    pygame.mixer.init()
    pygame.mixer.music.load(get_currend_song_path())


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

        self.add_widget(Label(text=str(directory_files[watched_song_index])))
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

    def on_stop(self):
        pygame.mixer.stop()
        pygame.mixer.quit()
        os.rename(get_currend_song_path(), get_current_song_real_path())


if __name__ == '__main__':
    lade_lied()
    MyApp().run()
