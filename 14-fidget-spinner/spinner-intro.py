
from manim import *
import math

# manim -p spinner-intro.py SpinnerIntro

class SpinnerIntro(Scene):
    def construct(self):
        level = Text("""
                    In this video, I'll show you how to create a fidget spinner 
                     
                    using a math graph calculator. 
                     

                    Follow along step by step, and you'll be able to make one yourself!
                    """
                     ).scale(0.5).set_color(WHITE)
        self.play(Write(level))
        self.wait(8)

#Some of the graphs may look weird or inconsistent; this is due to the limitations of the graphing calculator. But don't worry, the graph will still look beautiful and pleasing to the eye.        
