from manim import *


class GCDAwesome(Scene):
    def construct(self):
        lis = [
            # index 1
            "Let's start with the basics",
            # index 2
            "Now let's add y",
            # index 3
            "change y to x",
            # index 4
            "a little weird but okay",
            # index 5
            "slightly off target",
            # index 6
            "change x to y",
            # index 7
            "let's square y",
            # index 8
            "let's square x also",
            # index 9
            "Enough with zero",
            # index 10
            "let's multiply with x",
            # index 11
            "We are entering the 'interesting graph' zone.",
            # index 12
            "Let's multiply x with y",
            # index 13
            "How about division",
            # index 14
            "This looks a lot cleaner",
            # index 15
            "Multiply y with x... again",
            # index 16
            "It's trig time!",
            # index 17
            "'Tan' graphs can be messy sometimes",
            # index 18
            "Oddly satisfying",
            # index 19
            "Lets try trig division",
            # index 20
            "It's getting chaotic...",
            # index 21
            "Lawful Evil",
            # index 22
            "This one looks wild",
            # index 23
            "Even though it looks random, there is still some pattern here",
            # index 24
            "Nice pattern indeed",
            # index 25
            "There is a lot to unpack here",
            # index 26
            "True harmony",
            # index 27
            "Add the number '9' and it changes everything",
            # index 28
            "clean and simple",
            # index 29
            "Are these circles real?",
            # index 30
            "I wish Desmos could render this in full detail",
            # index 31
            "Here, you start seeing faces",
            # index 32
            "What did you see here?",
            # index 33
            "Chaotic Evil",
            # index 34
            "This is my final form, Thanks for watching till the end",
        ]

        eq = [
            'y=\gcd\left(1,0\\right)',
            'y=\gcd\left(y,0\\right)',
            'y=\gcd\left(x,0\\right)',
            'y=x\gcd\left(x,0\\right)',
            'y=xy\gcd\left(x,0\\right)',
            'y=xy\gcd\left(y,0\\right)',
            'y^{2}=\gcd\left(x,0\\right)',
            'y^{2}=\gcd\left(x^{2},0\\right)',
            'y=\gcd\left(x,y\\right)',
            'y=x\gcd\left(x,y\\right)',
            '\gcd\left(x,y\\right)=1',
            '\gcd\left(xy,y\\right)=1',
            '\gcd\left(\\frac{x}{y},x\\right)=1',
            '\gcd\left(\\frac{x}{y},y\\right)=1',
            '\gcd\left(\\frac{x}{y},xy\\right)=1',
            '\gcd\left(\sin\left(x\\right),y\\right)=1',
            '\gcd\left(\\tan\left(y\\right),x\\right)=1',
            '\gcd\left(\\tan\left(y\\right),\sin\left(x\\right)\\right)=1',
            '\gcd\left(\\frac{\sin\left(x\\right)}{\cos\left(y\\right)},y\\right)=1',
            '\gcd\left(\\frac{\\tan\left(x\\right)}{\cos\left(y\\right)},\\frac{\sin\left(x\\right)}{y}\\right)=1',
            '\gcd\left(\\frac{\\tan\left(x\\right)}{\cos\left(y\\right)},\\frac{\sin\left(x\\right)}{\\tan\left(y\\right)}\\right)=1',
            '\gcd\left(\\frac{x}{\sin\left(y\\right)+\sin\left(x\\right)},y\\right)=1',
            '\gcd\left(\\frac{x}{\cos\left(y\\right)},yx\\right)=1',
            '\gcd\left(\csc\left(x\\right),\\tan\left(x\\right)+\sin\left(3y\\right)\\right)=1',
            '\gcd\left(\sin\left(y\\right)+\cos\left(x\\right),\\tan\left(x\\right)+\sin\left(y\\right)\\right)=1',
            '\gcd\left(\sec\left(x\\right)+\\tan\left(y\\right),\sin\left(x\\right)\\right)=1',
            '\gcd\left(\sec\left(x\\right)+\\tan\left(y\\right),\sin\left(9x\\right)\\right)=1',
            '\gcd\left(\sec\left(x\\right)+\\frac{\\tan\left(9y\\right)}{\cos\left(x\\right)},\sin\left(x\\right)\\right)=1',
            '\gcd\left(\sec\left(x\\right)+\\frac{\\tan\left(9y\\right)}{\cos\left(x\\right)},\sin\left(x\\right)\cos\left(y\\right)\\right)=1',
            '\gcd\left(\csc\left(x\\right)+\\frac{\\tan\left(9y\\right)}{\sin\left(2x\\right)},\\tan\left(y\\right)+\cos\left(y\\right)\\tan\left(x\\right)\\right)=1',
            '\gcd\left(\csc\left(x\\right)+\\tan\left(y\\right),\\tan\left(x\\right)\sin\left(y\\right)\\right)=1',
            '\gcd\left(\sec\left(x\\right)+\\frac{\\tan\left(y\\right)}{\cos\left(3x\\right)},\sin\left(x\\right)y+\cos\left(y\\right)\\tan\left(x\\right)\\right)=1',
            '\gcd\left(\sec\left(x\\right)+\\frac{\\tan\left(9y\\right)}{\cos\left(3x\\right)},\sin\left(x\\right)y+\cos\left(y\\right)\\tan\left(x\\right)\\right)=1',
            '\gcd\left(\csc\left(x\\right)+\\frac{\\tan\left(y\\right)}{\sin\left(2x\\right)},\sin\left(x\\right)y+\cos\left(y\\right)\\tan\left(x\\right)\\right)=1',
        ]



        for i in range(29, len(eq)):
            equation = MathTex(eq[i]).scale(1.15).shift(UP).set_color(YELLOW)
            level = Text(lis[i]).scale(0.5).next_to(equation, DOWN*3)
            self.wait(0.25)
            self.play(FadeIn(equation))
            self.play(FadeIn(level, shift=UP))
            self.wait(3)
            self.clear()
