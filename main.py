from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
import os


BASE_PATH = os.path.dirname(__file__)

# Устанавливаем размер окна:
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
Config.write()


class Game(Widget):
    pass


class GameApp(App):
    def build(self):
        game = Game()
        return game


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
