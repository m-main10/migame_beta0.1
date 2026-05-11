import pygame
import math
import random
import  time
pygame.init()
class Pictyre:
    def __init__(self,puctyre,x,y,x_size=100,y_size=100,):
        self.puctyre=puctyre
        self.x=x
        self.y=y
        self.__images=puctyre
        self.__cloct_sistem=pygame.time.Clock()
        self.x_size=x_size
        self.y_size=y_size
    def __inti_new(self,puctyre,x,y,x_size,y_size):
        self.x=x
        self.y=y
        self.x_size=x_size
        self.y_size=y_size
        self.puctyre=puctyre
    def picture_size(self,new_size_x,new_size_y):
        self.__inti_new(self.puctyre,self.x,self.y,new_size_x,new_size_y)
        self.__images=pygame.transform.scale(self.puctyre,(new_size_x,new_size_y))
        return self.__images
    def goto(self,new_x,new_y):
        self.__inti_new(self.puctyre,new_x,new_y,self.x_size,self.y_size)
    def animation(self,fps,frame_int,*args):
            _clock = 0
            _anim=0
            _curet_time=time.time()
            if _curet_time - 1000/fps >= 1000/fps:
                self.__inti_new(args[_anim], self.x,self.y, self.x_size, self.y_size)
                _anim+=1


