
from manim import *
import math

# manim -p incombrehensible-intro.py IncombrehensibleIntro

class IncombrehensibleIntro(Scene):
    def construct(self):
        level = Text("""
                     What you're about to see are some of the most incomprehensible, 
                     

                     mind-blowing, space-bending, thought-provoking, and 
                     

                     incredibly satisfying math graphs i've ever made.
                    """
                     ).scale(0.5).set_color(WHITE)
        self.play(Write(level))
        self.wait(5)

#Some of the graphs may look weird or inconsistent; this is due to the limitations of the graphing calculator. But don't worry, the graph will still look beautiful and pleasing to the eye.        
