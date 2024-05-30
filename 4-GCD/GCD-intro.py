
from manim import *
import math


class GCDText(Scene):
    def construct(self):
        level = Text("""
                    Hello everyone! Welcome to my channel.
                     
               

                    Today, I will share with you some beautiful math graphs.
                     
                     

                    For today's video, I'll use GCD (Greatest Common Divisor). 
                     
                    This means every graph will contain at least one GCD operation.
                     
                     


                    I use Desmos to create these graphs.
                     
        
                    Enjoy :)"""
                     ).scale(0.5).set_color(BLUE)
        self.play(Write(level))
        self.wait(5)

#Some of the graphs may look weird or inconsistent; this is due to the limitations of the graphing calculator. But don't worry, the graph will still look beautiful and pleasing to the eye.        
