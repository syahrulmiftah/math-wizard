
from manim import *
import math

# manim -p screensaver-intro.py ScreensaverIntro

class ScreensaverIntro(Scene):
    def construct(self):
        level = Text("""
                    Hello everyone! Welcome to my channel.


                    Today, I will share with you some beautiful math graphs.

                     

                    The theme of this video is a loading screen or screensaver.

                    So basically I created a compilation of math graphs that can be repeated infinitely, 
                    
                    making it suitable for a screensaver or loading screen.

                     

                    There will be some unique or rather unconventional designs because, well, I use math. 
                     
                    But nonetheless, I hope you like it.
                     

                     
                    As usual, the link to these graphs will be included in the description.

                    Enjoy :)"""
                     ).scale(0.4).set_color(BLUE)
        self.play(Write(level))
        self.wait(5)

