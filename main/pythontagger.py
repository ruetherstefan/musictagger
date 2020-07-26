from kivy.app import App
from kivy.properties import StringProperty, NumericProperty

from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout

import pygame

from main.songdirectory import SongDirectory


songdirectory = SongDirectory()


class EditScreen(BoxLayout):
    song_titel = StringProperty()
    song_length = NumericProperty()

    tags = []

    def __init__(self, **kwargs):
        super(EditScreen, self).__init__(**kwargs)

        self.song_titel = songdirectory.get_current_song_name()
        self.song_length = songdirectory.get_currend_song_length()

        #self.generate_hardstyle_tagging_buttons()
        self.generate_wedding_tagging_buttons()

        self.lade_tags()

    def generate_wedding_tagging_buttons(self):
        self.add_widget(self.erstelle_energy_leiste())
        self.add_widget(self.erstelle_tag_leiste_genre2())
        self.add_widget(self.erstelle_tag_leiste_genre3())
        self.add_widget(self.erstelle_tag_leiste_genre4())

    def generate_hardstyle_tagging_buttons(self):
        self.add_widget(self.erstelle_tag_leiste())
        self.add_widget(self.erstelle_tag_leiste2())
        self.add_widget(self.erstelle_tag_leiste_quellmusik())
        self.add_widget(self.erstelle_tag_leiste_genre())

    def prev_song(self):
        pygame.mixer.music.stop()

        self.save_tags()
        songdirectory.dec_watched_song_index()
        self.lade_lied()

    def next_song(self):
        pygame.mixer.music.stop()

        self.save_tags()
        songdirectory.inc_watched_song_index()
        self.lade_lied()

    def save_tags(self):
        tagstring = ""
        for button in self.tags:
            if button.state == "down":
                tagstring += button.text + " "
        songdirectory.save_comment(tagstring)

    def lade_tags(self):
        comment = songdirectory.load_comment()
        for button in self.tags:
            if button.text in comment:
                button.state = "down"
            else:
                button.state = "normal"

    def lade_lied(self):
        songdirectory.lade_lied()

        self.song_titel = songdirectory.get_current_song_name()
        self.song_length = songdirectory.get_currend_song_length()
        self.lade_tags()

    def play_song(self):
        pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def forward_song(self, widget, touch):
        if widget.collide_point(*touch.pos):
            pygame.mixer.music.rewind()
            pygame.mixer.music.set_pos(widget.value)

# Hardstyle Tags

    def erstelle_tag_leiste(self):
        tag_leiste = BoxLayout(spacing=5)

        tag_leiste.add_widget(self.erstelleGroupButton('rawstyle', 'genre'))
        tag_leiste.add_widget(self.erstelleGroupButton('euphoric', 'genre'))
        tag_leiste.add_widget(self.erstelle_tag_button('fairy'))
        tag_leiste.add_widget(self.erstelle_tag_button('dunkel'))
        tag_leiste.add_widget(self.erstelle_tag_button('happy'))

        return tag_leiste

    def erstelle_tag_leiste2(self):
        tag_leiste = BoxLayout(spacing=5)

        tag_leiste.add_widget(self.erstelle_tag_button('top19'))
        tag_leiste.add_widget(self.erstelle_tag_button('verschwoerung'))
        tag_leiste.add_widget(self.erstelle_tag_button('drogen'))
        tag_leiste.add_widget(self.erstelle_tag_button('intro'))
        tag_leiste.add_widget(self.erstelle_tag_button('hymn'))

        return tag_leiste

    def erstelle_tag_leiste_quellmusik(self):
        tag_leiste = BoxLayout(spacing=5)

        tag_leiste.add_widget(self.erstelle_tag_button('klassik'))
        tag_leiste.add_widget(self.erstelle_tag_button('rock'))
        tag_leiste.add_widget(self.erstelle_tag_button('pop'))
        tag_leiste.add_widget(self.erstelle_tag_button('rap'))
        tag_leiste.add_widget(self.erstelle_tag_button('karneval'))

        return tag_leiste

    def erstelle_tag_leiste_genre(self):
        tag_leiste = BoxLayout(spacing=5)

        tag_leiste.add_widget(self.erstelle_tag_button('hardcore'))
        tag_leiste.add_widget(self.erstelle_tag_button('happyhcore'))
        tag_leiste.add_widget(self.erstelle_tag_button('house'))
        tag_leiste.add_widget(self.erstelle_tag_button('hardtechno'))
        tag_leiste.add_widget(self.erstelle_tag_button('schranz'))

        return tag_leiste

    def erstelle_tag_button(self, name):
        btn = ToggleButton(text=name)
        self.tags.append(btn)
        return btn

# Weddings Tags

    def erstelle_energy_leiste(self):
        tag_leiste = BoxLayout(spacing=5)

        tag_leiste.add_widget(self.erstelleGroupButton('tanzen', 'zweck'))
        tag_leiste.add_widget(self.erstelleGroupButton('entspannen', 'zweck'))

        tag_leiste.add_widget(self.erstelleGroupButton('eGering', 'enegie'))
        tag_leiste.add_widget(self.erstelleGroupButton('eMittel', 'enegie'))
        tag_leiste.add_widget(self.erstelleGroupButton('eHoch', 'enegie'))

        return tag_leiste

    def erstelle_tag_leiste_genre2(self):
        tag_leiste = BoxLayout(spacing=6)

        tag_leiste.add_widget(self.erstelle_tag_button('oldies'))
        tag_leiste.add_widget(self.erstelle_tag_button('roknroll'))
        tag_leiste.add_widget(self.erstelle_tag_button('80s'))
        tag_leiste.add_widget(self.erstelle_tag_button('90s'))
        tag_leiste.add_widget(self.erstelle_tag_button('schlager'))
        tag_leiste.add_widget(self.erstelle_tag_button('ballermann'))

        return tag_leiste

    def erstelle_tag_leiste_genre3(self):
        tag_leiste = BoxLayout(spacing=5)

        tag_leiste.add_widget(self.erstelle_tag_button('urban'))
        tag_leiste.add_widget(self.erstelle_tag_button('rap'))
        tag_leiste.add_widget(self.erstelle_tag_button('pop'))
        tag_leiste.add_widget(self.erstelle_tag_button('dance'))
        tag_leiste.add_widget(self.erstelle_tag_button('house'))

        return tag_leiste

    def erstelle_tag_leiste_genre4(self):
        tag_leiste = BoxLayout(spacing=5)

        tag_leiste.add_widget(self.erstelle_tag_button('alternative'))
        tag_leiste.add_widget(self.erstelle_tag_button('rock'))
        tag_leiste.add_widget(self.erstelle_tag_button('metal'))
        tag_leiste.add_widget(self.erstelle_tag_button('transition'))
        tag_leiste.add_widget(self.erstelle_tag_button('auftritt'))

        return tag_leiste

    def erstelleGroupButton(self, tag, genre):
        button = self.erstelle_tag_button(tag)
        button.group = genre
        return button


class PythontaggerApp(App):

    def build(self):
        return EditScreen()

    def on_stop(self):
        pygame.mixer.stop()
        pygame.mixer.quit()

        self.root.save_tags()
        songdirectory.delete_all_playcopys()


if __name__ == '__main__':
    pygame.mixer.init()
    songdirectory.lade_lied()
    PythontaggerApp().run()
