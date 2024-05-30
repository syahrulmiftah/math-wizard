
from manim import *
import math

# manim -p 3d-intro.py ThreeDimensionIntro

class ThreeDimensionIntro(Scene):
    def construct(self):
        level = Text("""
                    Hello everyone! Welcome to my channel.

                    

                    Today, I will share with you some beautiful math graphs.

                     

                    As many of you requested, this time I will be sharing 3D graphs,
                     
                    and I hope you like them.

                     

                    I use the math3d.org website to create all these graphs.

                    As usual, the link to these graphs will be included in the description.

                        

                    Enjoy :)"""
                     ).scale(0.4).set_color(BLUE)
        self.play(Write(level))
        self.wait(5)

