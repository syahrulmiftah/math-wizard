from manim import *

# manim -p incombrehensible-level.py Incombrehensible


class Incombrehensible(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "\left(t,\ t\\right)",
                "Lets start with the basics",
            ],
            # index 3
            [
                "\left(\sin t,\ \cos t\\right)",
                "Use sine and cosine to make circle",
            ],
            # index 4
            [
                "\left(\sin t,\ \sin\left(t\\right)\cos t\\right)",
                "Add another cosine to make infinity symbol",
            ],
            # index 5
            [
                "\left(\sin t,\ \cos\left(t\\right)\\right)",
                "\left(\sin t,\ 2\sin\left(t\\right)+\cos t\\right)",
                "Lets make saturn",
            ],
            # index 6
            [
                "\left(\sin t,\ \cos\left(t+2v_{1}\\right)\\right)",
                "\left(\sin t,\ 2\sin\left(t+2v_{1}\\right)+\cos t\\right)",
                "Boring animation huh? This one is more exciting...",
            ],
            # index 7
            [
                "\left(t,\sin v_{2}\\right)",
                "\left(t-v_{2},\sin\left(t\\right)\\right)",
                "This is how you draw sine wave",
            ],
            # index 8
            [
                "\left(t,a_{1}\pm 0.5\\right)",
                "\left(t,\pm t+a_{1}\\right)",
                "a_{1}=\sin\left(v_{2}+\sin\left(4v_{2}\\right)\\right)",
                "\left(t-v_{2},\sin\left(t+\sin\left(4t\\right)\\right)\\right)",
                "Too simple? Check out this one...",
            ],
            # index 9
            [
                "\left(\sin t,\ \sin\left(v_{6}+\cos t\\right)\\right)",
                "I think this is cute",
            ],
            # index 10
            [
                "\left(\sin t,\ \sin\left(v_{6}+\cos t\\right)\\right)",
                "\left(4\le t\le5\\right)",
                "\left(0\le t\le1\\right)",
                "Let's give him a friend",
            ],
            # index 11
            [
                "\left(\sin t,\ \sin\left(v_{6}+\cos t\\right)\\right)",
                "\left(4\le t\le5\\right)",
                "\left(0\le t\le1\\right)",
                "\left(0\le t\le2\pi\\right)",
                "Now you can see the whole picture...",
            ],
            # index 12
            [
                "\left(\sin\left(t\\right),\ \sin\left(v_{6}+\cos\left(t+v_{6}\\right)\\right)\\right)",
                "I can draw another wiggly wiggly",
            ],
            # index 13
            [
                "\left(\sin\left(t\\right),\ \sin\left(v_{6}+\cos\left(t+v_{6}\\right)+\sin\left(t+v_{6}\\right)\\right)\\right)",
                "Extraordinarily satisfying",
            ],
            # index 14
            [
                "\left(\sin t,\\tan\left(\\frac{v_{3}t}{2}\\right)\\right)",
                "Lets give 'tan' some proper introduction",
            ],
            # index 15
            [
                "\left(\sin t,\\tan\left(\\frac{v_{3}t}{2}\\right)+\cos\left(t\\right)\\right)",
                "'The cooler tan'",
            ],
            # index 16
            [
                "\left(\sin t,\\tan\left(\\frac{v_{3}t}{2}\\right)\cos t\\right)",
                "'The weird tan'",
            ],
            # index 17
            [
                "\left(\sin t+\cos t,\\tan\left(\\frac{v_{3}t}{2}\\right)\cos t\\right)",
                "'The even weirder tan'",
            ],
            # index 18
            [
                "\left(\sin t+\cos t,\\tan\left(\\frac{v_{3}t}{2}\\right)\cos\left(3v_{3}t\\right)+\sin\left(v_{3}t+v_{6}\\right)\\right)",
                "'The idk wtf is going on tan'",
            ],
            # index 19
            [
                "\left(\\tan\left(4t\\right),\ \sin\left(v_{4}9t\\right)\\right)",
                "Out of nothing",
            ],
            # index 20
            [
                "\left(\\tan\left(t\\right),\ \sec\left(\\frac{v_{5}t}{2}\\right)\\right)",
                "Never let them know your next move",
            ],
            # index 21
            [
                "\left(\\tan\left(t+v_{5}\pi\\right),\ \sec\left(t\\right)\\right)",
                "This is a repeating pattern",
            ],
            # index 22
            [
                "\left(\\tan\left(t+v_{5}\pi\\right),\ \sec\left(\\frac{t}{2}\\right)\\right)",
                """You can use this as a screensaver or loading animation,
                
                Whatever you like""",
            ],
            # index 23
            [
                "\left(\sin\left(0.98t\\right)+\cos\left(\\frac{v_{5}t}{2}\\right),\ \cos\left(t\\right)\\right)",
                "We're starting to get into the realm of incomprehensibility",
            ],
            # index 24
            [
                "\left(\sin\left(0.98t\\right)+\cos\left(t\\right),\ \cos\left(10v_{5}+t\\right)\\right)",
                "Put on some interstellar music while watching this graph",
            ],
            # index 25
            [
                "\left(\\tan\left(20.5t\\right),\ \sec\left(t\\right)+\sin\left(41t\\right)\\tan\left(t+v_{7}\pi\\right)\\right)",
                "This is lit!",
            ],
            # index 26
            [
                "\left(\\tan\left(20.5t\\right),\ \sec\left(t\\right)+\sin\left(41t\\right)\\tan\left(\\frac{v_{7}t}{2}\\right)\\right)",
                "Graph go brr...",
            ],
            # index 27
            [
                "\left(\\tan\left(20.5t\\right),\ \csc\left(v_{8}t\\right)+\cos\left(41t\\right)\\tan\left(t\\right)\\right)",
                "This graph has the coolest intro i've ever seen",
            ],
            # index 28
            [
                "\left(\\tan\left(10v_{8}t-0.5t\\right),\ \sec\left(t\\right)+\sin\left(20v_{8}t\\right)\\right)",
                "Take a moment to appreciate the beauty of this graph",
            ],
            # index 29
            [
                "\left(\\tan\left(19.5t\\right),\ \sec\left(t\\right)+\sin\left(40t+v_{9}\\right)\\right)",
                "I call this 'The moving dimension'",
            ],
            # index 30
            [
                "\left(\\tan\left(10v_{8}t-0.5t\\right),\ \sec\left(t\\right)+5\cos\left(20v_{8}t\\right)\\right)",
                "The graphs look like they're going to fight each other.",
            ],
            # index 31
            [
                "\left(\\tan\left(19.5t\\right),\ \sec\left(t\\right)+5\cos\left(40t+v_{9}\\right)\\right)",
                "Everything can be made into repeating graphs",
            ],
            # index 32
            [
                "\left(\\frac{\\tan\left(50t\\right)}{4}+\sin\left(t+v_{10}\pi\\right),\ \csc\left(t\\right)+\sin\left(100t\\right)\cos\left(0.6v_{10}t\\right)\\right)",
                """Try to understand this grarph
                
                Level: Impossible""",
            ],
            # index 33
            [
                "\left(\\frac{\\tan\left(50t+v_{10}\pi\\right)}{4}+\sin\left(t+v_{10}\pi\\right),\ \csc\left(t\\right)+\sin\left(100t\\right)\cos\left(1.2t+v_{10}\pi\\right)\\right)",
                "Looks like Tsunamis in outer space or something",
            ],
            # index 34
            [
                "\left(5\\tan\left(t+v_{10}\pi\\right)\cos\left(1.96t\\right),\\tan\left(t\\right)\\right)",
                "He is speaking the language of gods",
            ],
            # index 35
            [
                "\left(\\tan\left(30t+v_{10}\pi\\right)+\sin\left(t+v_{10}\pi\\right),\ t\sin\left(30t+v_{10}\pi\\right)\\right)",
                """
                I'll end my video with a quote by nikola tesla

                'You will live to see man made Graphs beyond your comprehension'
                """,
            ],     
        ]

        lis = [
            [
                "\left(\\frac{\\tan\left(50t+v_{10}\pi\\right)}{4}+\sin\left(t+v_{10}\pi\\right)\\right),",
                "\left(csc\left(t\\right)+\sin\left(100t\\right)\cos\left(1.2t+v_{10}\pi\\right)\\right)",
                "Well, well, well, if it isn't the Dark Lord himself.",
            ],              
        ]

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

# manim -p incombrehensible-level.py Incombrehensible

