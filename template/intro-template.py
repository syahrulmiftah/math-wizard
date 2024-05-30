
from manim import *
import math

# manim -p desmos-intro.py DesmosIntro

class DesmosIntro(Scene):
    def construct(self):
        level = Text("""
            Hello everyone! Welcome to my channel.
                     


            Today, I will share with you some beautiful math graphs.
                     


            As you guys requested, for today's video, I will not just show the graph, 
                     
            but I will also animate it, primarily using the Desmos slider feature.
                     


            So, sit back, relax, and prepare yourself for some incredible graphs.

            Enjoy :)"""
                     ).scale(0.5).set_color(BLUE)
        self.play(Write(level))
        self.wait(5)

#Some of the graphs may look weird or inconsistent; this is due to the limitations of the graphing calculator. But don't worry, the graph will still look beautiful and pleasing to the eye.        
