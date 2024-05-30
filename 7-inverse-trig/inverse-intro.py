
from manim import *
import math

# manim -p inverse-intro.py InverseIntro

class InverseIntro(Scene):
    def construct(self):
        level = Text("""
                    Hello everyone! Welcome to my channel.
                            


                    Today, I will share with you some beautiful math graphs featuring 
                            
                    the inverse trigonometric function.
                            

                            
                    For this video, I'm going to try different ways of presenting the graphs,
                     
                    mainly by animating the creation of each graph,
                     
                    and I hope you like it.
                            
                            

                            
                    I use DESMOS to write these graphs.
                            
                    As usual, the link to these graphs will be included in the description.
                            


                    Enjoy :)"""
                     ).scale(0.4).set_color(BLUE)
        self.play(Write(level))
        self.wait(5)

#Some of the graphs may look weird or inconsistent; this is due to the limitations of the graphing calculator. But don't worry, the graph will still look beautiful and pleasing to the eye.        
