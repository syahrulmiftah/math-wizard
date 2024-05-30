
from manim import *
import math


class ParametricText(Scene):
    def construct(self):
        level = Text("""
                    Hello Everyone! Welcome to my channel

                     


                    Today i will share with you some beautiful math graphs.
                     
                    For today's video, I'll exclusively use parametric functions, 
                     
                    which means the graph will be represented using sets of (x, y) coordinates.
                     
                

                     
                    
                    This time, I made sure that the graphs and the text are all in dark mode. 
                     
                    (I am terribly sorry for the harsh black and white transitions in my previous video; 
                     
                    I did not anticipate that.)
                     
                     

                    I use DESMOS to write these graphs.
                     
                    Enjoy!"""
                     ).scale(0.4).set_color(BLUE)
        self.play(Write(level))
        self.wait(5)
