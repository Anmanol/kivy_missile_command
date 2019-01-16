from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config
import os


BASE_PATH = os.path.dirname(__file__)

# Устанавливаем размер окна:
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', '0')
Config.write()


class Game(Widget):

    score = 230

#    self.label = Label(text='Score: {}'.format(self.score))
#    self.label.x = self.width - 150
#    self.label.y = self.height - 150
#   self.label.font_size = '20'

#    game.add_widget(self.label, canvas='after')


class GameApp(App):
    #@staticmethod
    #def get_label_x(self):
        #return self.width - 140

    #@staticmethod
    #def get_label_y(self):
        #return self.label.center_y - self.label.texture_size[1] * .5 + 650

    def build(self):
        game = Game()

        return game

class Base(Widget):
    pass

# class Building(Widget):
#
#     INITIAL_HEALTH = 1000
#
#     def __init__(self, x, y, name):
#         self.name = name
#         self.health = self.INITIAL_HEALTH
#         pic_path = os.path.join(BASE_PATH, 'images', self.get_pic_name())
#         self.image = Image(source=pic_path, pos=(x, y))
#
#     def get_pic_name(self):
#         if self.health < self.INITIAL_HEALTH * 0.2:
#             return f"{self.name}_3.gif"
#         if self.health < self.INITIAL_HEALTH * 0.8:
#             return f"{self.name}_2.gif"
#         return f"{self.name}_1.gif"
#
#     def is_alive(self):
#         return self.health >= 0


if __name__ == '__main__':
    GameApp().run()
