from manim import *

# manim -p interesting-chapter.py Chapter


class Chapter(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "Level 1",
                "Simple graphs that most people can sketch",
            ],
            # index 2
            [
                "Level 2",
                """
                This is where things get really interesting

                The graphs in this level can be very difficult to sketch
                """,
            ],
            # index 3
            [
                "Level 3",
                """
                At this level just try to enjoy the beauty of math
                
                Rather than trying to solve it
                """,
            ],
        ]


        # 1
        for item in lis:
            v1 = Text(item[0]).scale(1).set_color(YELLOW)
            v2 = Text(item[1]).scale(0.5).set_color(WHITE)            
            vg = VGroup(v1,v2)
            vg.arrange(DOWN, aligned_edge=UP, buff=1.5)

            self.wait(0.25)
            self.play(FadeIn(v1, shift=UP))
            self.play(Write(v2), run_time=1)
            self.wait(3)
            self.play(FadeOut(vg))
            self.clear()

# manim -p chapter.py Chapter
