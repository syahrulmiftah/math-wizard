
from manim import *
import math

# manim -p cosine-intro.py CosineIntro

class CosineIntro(Scene):
    def construct(self):
        level = Text("""
            Hello everyone! Welcome to my channel.
                     


            Today, I will share with you some beautiful math graphs featuring 
                     
            only the cosine function. (Out of all trigonometric functions)
                     

                     
            I use DESMOS to write these graphs.
                     
            As usual, the link to these graphs will be included in the description.
                     


            Enjoy :)"""
                     ).scale(0.5).set_color(BLUE)
        self.play(Write(level))
        self.wait(5)

#Some of the graphs may look weird or inconsistent; this is due to the limitations of the graphing calculator. But don't worry, the graph will still look beautiful and pleasing to the eye.        
