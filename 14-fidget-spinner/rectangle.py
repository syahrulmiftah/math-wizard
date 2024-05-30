from manim import *

# manim -p rectangle.py Rectangle

class Rectangle(Scene):
    def construct(self):
        #text = Text("1234567").scale(0.75)
        text = Text("12345").scale(0.35)
        #surrounding_rectangle = SurroundingRectangle(text, color=YELLOW, buff=0.5)
        #self.play(Create(surrounding_rectangle))
        self.play(Circumscribe(text, fade_out=True, run_time=2))


