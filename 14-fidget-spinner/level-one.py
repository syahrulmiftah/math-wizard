from manim import *

# manim -p level-one.py levelOne


class levelOne(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "Level one",
                "\left(\sin t,\ \sin\left(v_{6}+\cos t\\right)\\right)",
                "\left(4\le t\le5\\right)",
                "\left(0\le t\le1\\right)",
                "\left(0\le t\le2\pi\\right)",
                "Now you can see the whole picture...",
            ],
        ]


        # 1
        text_size = 0.75
        spacing = 0.4
        pause_after_v1 = 0

        # broken index "feels off" and last index 

        # min_index = 0
        start_index = 0
        # max_index = 25
        end_index = 1

        #lis = lis[-2:]
 
        for item in lis:
            variables = {}
            for i in range(len(item)):
                if "\le" in item[i] or "r=" in item[i]:
                    if "\le t\le" in item[i] or "\le v" in item[i]:
                        variables[f"v{i+1}"] = MathTex(item[i]).scale(text_size).set_color(BLUE)
                    else:
                        variables[f"v{i+1}"] = MathTex(item[i]).scale(text_size).set_color(YELLOW)    
                else:
                    variables[f"v{i+1}"] = Text(item[i]).scale(text_size/2).set_color(WHITE)


            vars = [variables[f"v{i}"] for i in range(2,len(item)+1)]
            vg1 = VGroup(variables[f"v{1}"])
            vg2 = VGroup(*vars)
            vg3 = VGroup(vg1, vg2)

            vg1.arrange(DOWN, aligned_edge=LEFT, buff=spacing)
            vg2.arrange(DOWN, aligned_edge=LEFT, buff=spacing)
            vg3.arrange(DOWN, aligned_edge=LEFT, buff=spacing)

            self.wait(0.25)
            [self.play(FadeIn(x, shift=UP)) for x in vg1]
            self.wait(pause_after_v1)
            [self.play(FadeIn(x, shift=UP)) for x in vg2]
            self.wait(2)
            self.clear()

# manim -p level-one.py LevelOne