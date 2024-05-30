
from manim import *
import math

# manim -p loading-intro.py LoadingIntro

class LoadingIntro(Scene):
    def construct(self):
        level = Text("""
                    This is Part 2 of the video where I try to make a unique and 
                     
                    amazing loading screen animation using math
                     
                    Enjoy :)
                     """
                     ).scale(0.5).set_color(BLUE)
        self.play(Write(level))
        self.wait(5)

#Some of the graphs may look weird or inconsistent; this is due to the limitations of the graphing calculator. But don't worry, the graph will still look beautiful and pleasing to the eye.        
