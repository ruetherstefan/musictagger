import os

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

import pygame

from main.songdirectory import SongDirectory


songdirectory = SongDirectory()



def play_song(instance):
    pygame.mixer.music.play()


def pause_song(instance):
    pygame.mixer.music.pause()


def forward_song(self, touch):
    if self.collide_point(*touch.pos):
        pygame.mixer.music.rewind()
        pygame.mixer.music.set_pos(self.value)


def next_song(instance):
    pygame.mixer.music.stop()

    songdirectory.save_id3()
    songdirectory.inc_watched_song_index()
    songdirectory.lade_lied()


def prev_song(instance):
    pygame.mixer.music.stop()

    songdirectory.save_id3()
    songdirectory.dec_watched_song_index()
    songdirectory.lade_lied()


class EditScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(EditScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 5

        self.add_widget(self.erstelle_kopf_leiste())
        self.add_widget(self.erstelle_lied_leiste())

        song_position = Slider(min=0, max=songdirectory.get_song_length())
        song_position.step = 1
        song_position.bind(on_touch_up=forward_song)
        self.add_widget(song_position)

        self.add_widget(self.erstelle_tag_leiste())
        self.add_widget(self.erstelle_tag_leiste2())
        self.add_widget(self.erstelle_tag_leiste3())

    def erstelle_kopf_leiste(self):
        kopf_leiste = BoxLayout(spacing=5)

        titel = Label(text=str(songdirectory.directory_files[songdirectory.watched_song_index]))
        kopf_leiste.add_widget(titel)

        laenge = Label(text=str(songdirectory.get_song_length()))
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
        tag_leiste.add_widget(self.erstelle_tag_button('intro'))

        return tag_leiste

    def erstelle_tag_leiste3(self):
        tag_leiste = BoxLayout(spacing=5)

        tag_leiste.add_widget(self.erstelle_tag_button('hardcore'))
        tag_leiste.add_widget(self.erstelle_tag_button('happyhardcore'))
        tag_leiste.add_widget(self.erstelle_tag_button('house'))
        tag_leiste.add_widget(self.erstelle_tag_button('hardtechno'))

        return tag_leiste

    def erstelle_tag_button(self, name):
        btn1 = ToggleButton(text=name)
        btn1.bind(state=lambda o, val: songdirectory.tags.set(name, val == "down"))
        return btn1

    def erstelle_lied_leiste(self):
        liedleiste = BoxLayout(spacing=5)

        liedleiste.add_widget(self.erstelle_button_mit_titel_und_funktion('Prev', prev_song))
        liedleiste.add_widget(self.erstelle_button_mit_titel_und_funktion('Play', play_song))
        liedleiste.add_widget(self.erstelle_button_mit_titel_und_funktion('Pause', pause_song))
        liedleiste.add_widget(self.erstelle_button_mit_titel_und_funktion('Next', next_song))

        return liedleiste

    def erstelle_button_mit_titel_und_funktion(self, name, funktion):
        btn4 = Button(text=name)
        btn4.bind(on_press=funktion)
        return btn4





class MyApp(App):

    def build(self):
        return EditScreen()

    def on_stop(self):
        pygame.mixer.stop()
        pygame.mixer.quit()
        songdirectory.delete_all_playcopys()


if __name__ == '__main__':
    pygame.mixer.init()
    songdirectory.lade_lied()
    MyApp().run()
