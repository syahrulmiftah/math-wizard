from manim import *

# manim -p desmos-levels.py Desmos


class Desmos(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "",
                "",
            ],
            # index 2
            [
                "",
                "",
            ],
            # index 3
            [
                "",
                "",
            ],
            # index 4
            [
                "",
                "",
            ],
            # index 5
            [
                "",
                "",
            ],
            # index 6
            [
                "",
                "",
            ],
            # index 7
            [
                "",
                "",
            ],
            # index 8
            [
                "",
                "",
            ],
            # index 9
            [
                "",
                "",
            ],
            # index 10
            [
                "",
                "",
            ],
            # index 11
            [
                "",
                "",
            ],
            # index 12
            [
                "",
                "",
            ],
            # index 13
            [
                "",
                "",
            ],
            # index 14
            [
                "",
                "",
            ],
            # index 15
            [
                "",
                "",
            ],
            # index 16
            [
                "",
                "",
            ],
            # index 17
            [
                "",
                "",
            ],
            # index 18
            [
                "",
                "",
            ],
            # index 19
            [
                "",
                "",
            ],
            # index 20
            [
                "",
                "",
            ],
            # index 21
            [
                "",
                "",
            ],
            # index 22
            [
                "",
                "",
            ],
            # index 23
            [
                "",
                "",
            ],
            # index 24
            [
                "",
                "",
            ],
            # index 25
            [
                "",
                "",
            ],
            # index 26
            [
                "",
                "",
            ],
            # index 27
            [
                "",
                "",
            ],
            # index 28
            [
                "",
                "",
            ],
            # index 29
            [
                "",
                "",
            ],
            # index 30
            [
                "",
                "",
            ],
            # index 31
            [
                "",
                "",
            ],
            # index 32
            [
                "",
                "",
            ],
            # index 33
            [
                "",
                "",
            ],
            # index 34
            [
                "",
                "",
            ],
            # index 35
            [
                "",
                "",
            ],
            # index 36
            [
                "",
                "",
            ],
            # index 37
            [
                "",
                "",
            ],
            # index 38
            [
                "",
                "",
            ],
            # index 39
            [
                "",
                "",
            ],
            # index 40
            [
                "",
                "",
            ],
            # index 41
            [
                "",
                "",
            ],
            # index 42
            [
                "",
                "",
            ],
            # index 43
            [
                "",
                "",
            ],
            # index 44
            [
                "",
                "",
            ],
            # index 45
            [
                "",
                "",
            ],
        ]

        fix = [22]

        # 1
        for item in lis:
            first_eq = MathTex(item[0]).to_edge(UP).set_color(YELLOW)

            mini_text = Text(item[-1]).scale(0.5).set_color("##e0e0e0")            
            variables = {}
            equations = item[1:-1]
            for i in range(len(equations)):
                # Create variables v1, v2, v3, ..., vn with values 1, 2, 3, ..., n
                variables[f"v{i+1}"] = MathTex(equations[i]).set_color(YELLOW)

            vars = [variables[f"v{i}"] for i in range(1, len(equations) + 1)]
            vg = VGroup(first_eq, *vars, mini_text)
            vg.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

            self.wait(0.25)
            [self.play(FadeIn(x, shift=UP)) for x in vg]
            self.wait(3.5)
            self.clear()

# manim -p desmos-levels.py Desmos
