
from manim import *
import math

# manim -p intro.py Intro
# manim -p E:\Youtube\Math\satisfying\1-oddly\intro.py Intro
# before i start, id like to say ...
# As a person who likes math and music
#                    If you're new here, I'm the Math Wizard, and this channel is all about creating
                      
#                    interesting stuff with mathematics.

class Intro(Scene):
    def construct(self):
        self.camera.background_color = "#00ff00"
        level = Text("""
                    Hi there, Welcome to my channel.


                    Today, I'd like to show you some really cool graphs.

                    These are not just regular math graphs; these are graphs that are almost 
                     
                    impossible to draw without a calculator. They're also animated in real-time. 
                     
                     
                    And the best part is, I synchronized the graphs with the music, 
                    
                    so it's very satisfying to watch.
                                                            

                    As always, I'll be using dark mode because, it's easier on the eyes and besides, 
                     
                    it looks amazing. All these graphs and animations are made using DESMOS.
                                        
                    (link in the description)

                     
                    Enjoy :)
                    """
                     ).scale(0.4).set_color(WHITE)
        self.play(Write(level))
        self.wait(5)

#Some of the graphs may look weird or inconsistent; this is due to the limitations of the graphing calculator. But don't worry, the graph will still look beautiful and pleasing to the eye.        
