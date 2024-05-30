
from manim import *
import math

# manim -p straight-line-intro.py StraightLineIntro

class StraightLineIntro(Scene):
    def construct(self):
        level = Text("""
                    Hello everyone!

                     

                    Today, I will share some unique and beautiful math graphs, 
                     
                    but there's a catch! 
                     
                     
                    That is, I will only be using straight lines.
                     
                    Yeah, that's right, no curves allowed.
                     

                    Sounds insane, but let's see what I can do.
                     

                     
                    Enjoy :)"""
                     ).scale(0.5).set_color(BLUE)
        self.play(Write(level))
        self.wait(5)

