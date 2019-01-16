from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config


# Устанавливаем размер окна:
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', '1')
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

if __name__ == '__main__':
    GameApp().run()
