import  pygame
import warnings
from . import color

_sistem_color=color.Color()
pygame.init()
class Screen:
    def __init__(self):
        self.__screen_pygame=pygame.display
        self.__window=None
        self._ranning=False
    def set_window(self,x,y):
        try:
             self.__window=self.__screen_pygame.set_mode((x,y))
        except:
            try:
                self.__window = self.__screen_pygame.set_mode((int(x), int(y)))
                warnings.warn("RU Внимание: размеры окна нужно передавать как числа (int), а не как текст в кавычках!")
                warnings.warn("Attention: window sizes must be passed as numbers (int), and not as text in quotes!")



            except:
                raise  TypeError
        self._ranning=True


    def blit(self,picture,x,y):
        try:
           self.__window.blit(picture,(x,y))
        except:
            try:
                self.__window.blit(picture, (int(x), int(y)))
                warnings.warn("RU Внимание: координаты картинки нужно передавать как числа (int), а не как текст в кавычках!")
                warnings.warn("Attention: image coordinates must be transmitted as numbers (int), and not as text in quotes!")


            except:
                raise TypeError
    def fill(self,r,g,b):
        try:
          self.rgb=_sistem_color._rgb(r,g,b)
          self.__window.fill(self.rgb)
        except:
            try:
                self.__window.fill((int(r),int(g),int(b)))
                warnings.warn("RU Внимание: значения цвета R, G, B нужно передавать как числа (int), а не как текст в кавычках!")
                warnings.warn("Attention: color values R, G, B must be passed as numbers (int), and not as text in quotes!")



            except:
                raise TypeError

    def update(self):
        self.__screen_pygame.update()
    def end(self):
        self._ranning=False
        self.__window=None
