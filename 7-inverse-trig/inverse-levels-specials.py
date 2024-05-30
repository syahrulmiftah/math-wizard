from manim import *

# manim -p inverse-levels-specials.py Inverse


class Inverse(Scene):
    def construct(self):
        lis = [
            [
                "r=\\arccos\left(\\tan\left(1.5\\theta\\right)\\right)", #4
                "r=\\arccos\left(\cot\left(1.5\\theta\\right)\\right)", #1
                "Today i'll make something different",              #2
                "Let's make two graphs at once",                    #3
            ],
            [
                """
                r&=\\arccos\left(\\tan\left(0.3\\theta\\right)\\right) \\\\
                r&=\\arccos\left(\cot\left(0.3\\theta\\right)\\right)
                """,
                """
                r&=\\arccos\left(\cot\left(0.3\\theta+\\frac{\pi}{2}\\right)\\right) \\\\
                r&=\\arccos\left(\\tan\left(0.3\\theta+\\frac{\pi}{2}\\right)\\right)
                """,
                "Prepare for trouble",
                "and make it double",
            ],            
            [
                "r=\\arctan\left(\sin\left(1.5\\theta\\right)+\\tan\left(1.5\\theta\\right)\\right)",
                "I am not in danger",
                "I am the DANGER",
            ],            
        ]


        item = lis[2]

        # 1

        equation = MathTex(item[0]).scale(
            1).shift(UP).set_color(YELLOW)
        
        #equation2 = MathTex(item[0]).scale(1).shift(UP).set_color(YELLOW).next_to(equation, UP*2)
    
        mini_text = Text(item[1]).scale(0.4).next_to(equation, DOWN*3).set_color("#e0e0e0")
        mini_text2 = Text(item[2]).scale(0.4).next_to(mini_text, DOWN*3).set_color("#e0e0e0")

        self.wait(0.25)
        self.play(FadeIn(equation))
        self.play(FadeIn(mini_text, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(mini_text2, shift=UP))
        #self.play(FadeIn(equation2, shift=DOWN))
        self.wait(3.5)
        self.clear()

# manim -p inverse-levels-specials.py Inverse

