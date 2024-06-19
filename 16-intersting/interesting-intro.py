
from manim import *
import math

# manim -p interesting-intro.py Intro

class Intro(Scene):
    def construct(self):
        self.camera.background_color = "#00ff00"
        level = Text("""
                    Mathematics as an expression of the human mind reflects the active will, 
                     
                    the contemplative reason, and the desire for aesthetic perfection.
                     

                    ~ Richard Courant
                    """
                     ).scale(0.4).set_color(WHITE)
        self.play(Write(level))
        self.wait(8)

