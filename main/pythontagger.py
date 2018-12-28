from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout


class EditScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(EditScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 5

        self.add_widget(Label(text='Name Lied'))
        self.add_widget(self.erstelle_lied_leiste())
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

        btn3 = Button(text='Pause')
        liedleiste.add_widget(btn3)

        btnminus = Button(text='Minus 10')
        liedleiste.add_widget(btnminus)

        btnplus = Button(text='Plus 10')
        liedleiste.add_widget(btnplus)

        btn4 = Button(text='Next')
        liedleiste.add_widget(btn4)

        return liedleiste


class MyApp(App):

    def build(self):
        return EditScreen()


if __name__ == '__main__':
    MyApp().run()
