from manim import *

# manim -p subscribe.py Subscribe

class Subscribe(Scene):
    def construct(self):
        lis = [
            [
                """
                If you enjoy these graphs, give it a like!
                
                And subscribe for more videos like this
                """
            ],  
        ]
        for item in lis:
            for x in item:
                txt = Text(x).scale(0.5).set_color(YELLOW).shift(DOWN*2)
                self.play(FadeIn(txt, shift=UP))
                self.wait(3)
                self.clear()
                self.wait(0.25)
            


           