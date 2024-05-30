from manim import *


class ParametricIndividual(Scene):
    def construct(self):
        lis = [
            # index 1
            "Let's start with the basics",
            # index 2
            'its regular sin, but only positive',
            # index 3
            'typical tan graph',
            # index 4
            'Lets try sine and secant',
            # index 5
            'how about cosecant and secant',
            # index 6
            'sine and cosine will get you circle',
            # index 7
            'Why not add 9?',
            # index 8
            'Well its square now',
            # index 9
            'nine never dissapoints',
            # index 10
            'It all starts from here',
            # index 11
            'whoa, take it easy',
            # index 12
            'inverse circle',
            # index 13
            '9 always brings joy',
            # index 14
            'Ellipse',
            # index 15
            'increase the sine value and you get something wiggly',
            # index 16
            'How could there be a parallelogram?',
            # index 17
            'well that just looks like rectangle with extra step',
            # index 18
            '''
            Okay, let's go back to the basics. 
            
            Trust me, it's all uphill from here!
            ''',
            # index 19
            'The graph just went from 0 to 100 real quick',
            # index 20
            '''
            From here on, the graphs will always contain tan, 
            
            and you will absolutely love it
            ''',
            # index 21
            'streched out',
            # index 22
            """
            Here, I'm laying the groundwork, 
            
            setting the stage for what's to come
            """,
            # index 23
            'Add bunch of numbers and BOOM...',
            # index 24
            'Its a tunnel',
            # index 25
            'Someone just bent space and time',
            # index 26
            '19.5 is magical',
            # index 27
            'We are living in simulation...',
            # index 28
            'planet square',
            # index 29
            'I call this "the collision"',
            # index 30
            'Slightly bent magnetic field',
            # index 31
            'Ahh yes, Pattern',
            # index 32
            'Wormhole?',
            # index 33
            'The definition of insane',
            # index 34
            'The Tree of Life',
            # index 35
            'Its almost like you can feel the 3d space',
            # index 36
            'The Good the Bad and the Ugly',
            # index 37
            'Beyond the realm of graphs...',
            # index 38
            'Tip to tip',
            # index 39
            'Honestly i dont know why i choose 1.98',
            # index 40
            'I cant understand how this one bends',
            # index 41
            'I call this "The Math Scroll"',
            # index 42
            'This graph hits hard',
            # index 43
            'When celestial objects collide...',
            # index 44
            'This one looks like perfect lips',
            # index 45
            '''
            This is the endgame, Thanks for watching till the end
            
            The wizard will be back with more magic
            '''
        ]

        eq = [
            '\left(t,\ t\\right)',
            '\left(t,\ \sin\left(t\\right)\\right)',
            '\left(t,\ \\tan\left(t\\right)\\right)',
            '\left(\sin\left(t\\right),\ \sec\left(t\\right)\\right)',
            '\left(\csc\left(t\\right),\ \sec\left(t\\right)\\right)',
            '\left(\cos\left(t\\right),\ \sin\left(t\\right)\\right)',
            '\left(\cos\left(t\\right),\ \sin\left(9t\\right)\\right)',
            '\left(\cos\left(t\\right),\ \sin\left(99t\\right)\\right)',
            '\left(\cos\left(t\\right),\ \sin\left(0.99t\\right)\\right)',
            '\left(\sin\left(t\\right),\ \csc\left(t\\right)\cos\left(t\\right)\\right)',
            '\left(\sin\left(t\\right),\ \csc\left(t\\right)\cos\left(99t\\right)\\right)',
            '\left(\sin\left(t\\right),\ \csc\left(99t\\right)\cos\left(t\\right)\\right)',
            '\left(\sin\left(9t\\right),\ \csc\left(99t\\right)\cos\left(t\\right)\\right)',
            '\left(\sin\left(t\\right)+\cos\left(t\\right),\ \cos\left(t\\right)\\right)',
            '\left(\sin\left(5t\\right)+\cos\left(t\\right),\ \cos\left(t\\right)\\right)',
            '\left(\sin\left(0.98t\\right)+\cos\left(t\\right),\ \cos\left(t\\right)\\right)',
            '\left(\sin\left(t\\right)+\cos\left(t\\right),\ \cos\left(1.67t\\right)\\right)',
            '\left(\cos\left(t\\right),\ \sec\left(t\\right)\\right)',
            '\left(4\cos\left(9.9t\\right),\ \\frac{\sec\left(10t\\right)}{2}\\right)',
            '\left(\\tan\left(t\\right),\ \sin\left(t\\right)\\right)',
            '\left(\\tan\left(8t\\right),\ \sin\left(9t\\right)\\right)',
            '\left(\\tan\left(t\\right),\ \sec\left(t\\right)\\right)',
            '\left(\\tan\left(40t\\right),\ \\frac{\sec\left(7t\\right)}{2}\\right)',
            '\left(\\tan\left(t\\right),\ \sec\left(t\\right)\sin\left(40t\\right)\\right)',
            '\left(\\tan\left(19.5t\\right),\ \sec\left(t\\right)+\sin\left(40t\\right)\\right)',
            '\left(\\tan\left(19.5t\\right),\ \sec\left(t\\right)+\sin\left(40t\\right)\\tan\left(t\\right)\\right)',
            '\left(\\tan\left(20.5t\\right),\ \sec\left(t\\right)+\sin\left(41t\\right)\\tan\left(t\\right)\\right)',
            '\left(\\tan\left(20.5t\\right),\ \csc\left(2t\\right)+\cos\left(41t\\right)\\tan\left(t\\right)\\right)',
            '\left(\\tan\left(19.5t\\right),\ \sec\left(t\\right)+5\cos\left(40t\\right)\\right)',
            '\left(\\tan\left(19.5t\\right),\ \sec\left(t\\right)\sin\left(40t\\right)\\right)',
            '\left(\\tan\left(41t\\right),\ \sec\left(t\\right)\sin\left(40t\\right)\\right)',
            '\left(\\tan\left(19t\\right),\ \sec\left(t\\right)\sin\left(40t\\right)\\right)',
            '\left(\\tan\left(20t\\right),\ \sec\left(39t\\right)\sin\left(40t\\right)\\right)',
            '\left(\\tan\left(30t\\right)+\sin\left(t\\right),\ \sec\left(t\\right)\sin\left(30t\\right)\\right)',
            '\left(9\\tan\left(30t\\right)+\sin\left(t\\right),\ \sec\left(t\\right)\sin\left(30t\\right)\\right)',
            '\left(\\tan\left(25t\\right)+\sin\left(99t\\right),\ \sec\left(50t\\right)+\sin\left(t\\right)\\right)',
            '\left(\\tan\left(t\\right),\ \csc\left(t\\right)\\tan\left(0.98t\\right)-\sin\left(t\\right)\\right)',
            '\left(\sin\left(2t\\right)+\\tan\left(t\\right)\cos\left(1.96t\\right),\\tan\left(t\\right)+\sin\left(4t\\right)\\right)',
            '\left(\sin\left(2t\\right)+\cos\left(1.98t\\right),\\tan\left(2t\\right)+\sin\left(4t\\right)\\right)',
            '\left(\\tan\left(30t\\right)+\sin\left(t\\right),\ t\sin\left(30t\\right)\\right)',
            '\left(2\sin\left(4t\\right)+\cos\left(1.98t\\right),\\tan\left(t\\right)+\sin\left(4t\\right)\\right)',
            '\left(5\\tan\left(t\\right)\cos\left(1.96t\\right),\\tan\left(t\\right)\\right)',
            '\left(\\frac{\\tan\left(50t\\right)}{4}+\sin\left(t\\right),\ \sec\left(t\\right)+\sin\left(100t\\right)\\right)',
            '\left(\\frac{\\tan\left(50t\\right)}{4}+\sin\left(t\\right),\ \csc\left(t\\right)+\sin\left(100t\\right)\cos\left(1.2t\\right)\\right)',
            '\left(\\tan\left(25t\\right)+\cos\left(t\\right),\ \\tan\left(t\\right)\sin\left(50t\\right)\\right)'
        ]

        to_make = [9,13,17,19,21,32,35,36,38,42,44]
        # 1
        for i in to_make:
            equation = MathTex(eq[i]).scale(1.25).shift(UP).set_color(YELLOW)
            level = Text(lis[i]).scale(0.5).next_to(equation, DOWN*3)
            self.wait(0.25)
            self.play(FadeIn(equation))
            self.play(FadeIn(level, shift=UP))
            self.wait(3)
            self.clear()
