from kivy.app import App
from kivy.properties import StringProperty, NumericProperty

from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

import pygame

from main.songdirectory import SongDirectory


songdirectory = SongDirectory()


class EditScreen(Widget):
    song_titel = StringProperty()
    song_length = NumericProperty()

    def __init__(self, **kwargs):
        super(EditScreen, self).__init__(**kwargs)

        self.song_titel = songdirectory.get_current_song_name()
        self.song_length = songdirectory.get_currend_song_length()

        #self.add_widget(self.erstelle_tag_leiste())
        #self.add_widget(self.erstelle_tag_leiste2())
        #self.add_widget(self.erstelle_tag_leiste3())

    def prev_song(self):
        pygame.mixer.music.stop()

        songdirectory.save_id3()
        songdirectory.dec_watched_song_index()
        self.lade_lied()

    def next_song(self):
        pygame.mixer.music.stop()

        songdirectory.save_id3()
        songdirectory.inc_watched_song_index()
        self.lade_lied()

    def lade_lied(self):
        songdirectory.lade_lied()
        self.song_titel = songdirectory.get_current_song_name()
        self.song_length = songdirectory.get_currend_song_length()

    def play_song(self):
        pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def forward_song(self, widget, touch):
        if widget.collide_point(*touch.pos):
            pygame.mixer.music.rewind()
            pygame.mixer.music.set_pos(widget.value)


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


class PythontaggerApp(App):

    def build(self):
        return EditScreen()

    def on_stop(self):
        pygame.mixer.stop()
        pygame.mixer.quit()
        songdirectory.delete_all_playcopys()


if __name__ == '__main__':
    pygame.mixer.init()
    songdirectory.lade_lied()
    PythontaggerApp().run()
