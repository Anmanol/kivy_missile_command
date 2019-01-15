from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config


# Устанавливаем размер окна:
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', '0')
Config.write()


class Game(Widget):
    pass


class GameApp(App):
    @staticmethod
    def get_label_x(self):
        return self.label.center_x - self.label.texture_size[0] * .5 + 950

    @staticmethod
    def get_label_y(self):
        return self.label.center_y - self.label.texture_size[1] * .5 + 650

    def build(self):
        game = Game()

        self.score = 10

        self.label = Label(text='Score: {}'.format(self.score))
        self.label.x = self.get_label_x(self)
        self.label.font_size = '30'
        self.label.y = self.get_label_y(self)
        self.label.texture_update()

        self.score = 0

        game.add_widget(self.label, canvas='after')
        return game


if __name__ == '__main__':
    GameApp().run()
