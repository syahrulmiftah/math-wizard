from manim import *

# manim -p chapter.py Chapter


class Chapter(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "Chapter 1",
                "Rotation and Revolution",
            ],
            # index 2
            [
                "Chapter 2",
                "More than one",
            ],
            # index 3
            [
                "Chapter 3",
                "Sense of Rotation",
            ],
            # index 4
            [
                "Chapter 4",
                "Trace",
            ],
            # index 5
            [
                "Chapter 5",
                "Center Modifiaction",
            ],
            # index 6
            [
                "Chapter 6",
                "Three Dimension",
            ],
        ]


        # 1
        for item in lis:
            v1 = Text(item[0]).scale(0.5).set_color(WHITE)
            v2 = Text(item[1]).scale(1).set_color(YELLOW)            
            vg = VGroup(v1,v2)
            vg.arrange(DOWN, aligned_edge=UP, buff=0.5)

            self.wait(0.25)
            self.play(FadeIn(v1, shift=UP))
            self.play(Write(v2), run_time=1)
            self.wait(0.5)
            self.play(FadeOut(vg))
            self.clear()

# manim -p chapter.py Chapter
