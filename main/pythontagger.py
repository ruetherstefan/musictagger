from os import listdir
import os
import math

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

import pygame

import eyed3

from main.tags import Tags

song_ordner = "C:\P\P\musictagger\inputmusic\\"
directory_files = listdir(song_ordner)
watched_song_index = 0

name_of_current_song = ""

tags = Tags()


def get_song_length():
    audiofile = eyed3.load(get_currend_song_path())
    return int(math.floor(audiofile.info.time_secs))


def get_currend_song_path():
    return song_ordner + 'currentsong.mp3'


def get_current_song_real_path():
    return song_ordner + str(directory_files[watched_song_index])


def lade_lied():
    name_of_current_song = str(directory_files[watched_song_index])
    os.rename(get_current_song_real_path(), get_currend_song_path())

    pygame.mixer.init()
    pygame.mixer.music.load(get_currend_song_path())

    pygame.mixer.music.play()


def play_song(instance):
    pygame.mixer.music.play()


def pause_song(instance):
    pygame.mixer.music.pause()


def forward_song(self, touch):
    if self.collide_point(*touch.pos):
        pygame.mixer.music.rewind()
        pygame.mixer.music.set_pos(self.value)


class EditScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(EditScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 5

        self.add_widget(self.erstelle_kopf_leiste())
        self.add_widget(self.erstelle_lied_leiste())

        song_position = Slider(min=0, max=get_song_length())
        song_position.step = 1
        song_position.bind(on_touch_up=forward_song)
        self.add_widget(song_position)

        self.add_widget(self.erstelle_tag_leiste())
        self.add_widget(self.erstelle_tag_leiste2())

    def erstelle_kopf_leiste(self):
        kopf_leiste = BoxLayout(spacing=5)

        titel = Label(text=str(directory_files[watched_song_index]))
        kopf_leiste.add_widget(titel)

        laenge = Label(text=str(get_song_length()))
        kopf_leiste.add_widget(laenge)

        return kopf_leiste

    def erstelle_tag_leiste(self):
        tag_leiste = BoxLayout(spacing=5)

        rawstyle = self.erstelle_tag_button('rawstyle')
        rawstyle.group = 'genre'
        tag_leiste.add_widget(rawstyle)
        euphoric = self.erstelle_tag_button('euphoric')
        euphoric.group = 'genre'
        tag_leiste.add_widget(euphoric)

        tag_leiste.add_widget(self.erstelle_tag_button('fairy'))
        tag_leiste.add_widget(self.erstelle_tag_button('karneval'))

        return tag_leiste

    def erstelle_tag_leiste2(self):
        tag_leiste = BoxLayout(spacing=5)

        tag_leiste.add_widget(self.erstelle_tag_button('top18'))
        tag_leiste.add_widget(self.erstelle_tag_button('klassik'))
        tag_leiste.add_widget(self.erstelle_tag_button('verschwoerung'))
        tag_leiste.add_widget(self.erstelle_tag_button('hardcore'))

        return tag_leiste

    def erstelle_tag_button(self, name):
        btn1 = ToggleButton(text=name)
        btn1.bind(state=lambda o, val: tags.set(name, val == "down"))
        return btn1

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
