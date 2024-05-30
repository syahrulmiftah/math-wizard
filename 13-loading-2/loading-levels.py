from manim import *

# manim -p loading-levels.py Loading


class Loading(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "\left(t,0\\right)",
                "0 \le t\le v_{4}",
                "This is like the most basic loading screen",
            ],
            # index 2
            [
                "\left(t,0\\right)",
                "v_{4}+\left|v_{4}-2\\right|-4 \le t\le v_{4}-\left|v_{4}-2\\right|",
                "Lets repeat the line",
            ],
            # index 3
            [
                "\left(t,0\\right)",
                "a_{5}+\left|a_{5}-2\\right|-4 \le t\le a_{5}-\left|a_{5}-2\\right|",
                "a_{5}=4\sin\left(v_{5}\\right)",
                "Now i am using sine rate of function to make it smoother",
            ],
            # index 4
            [
                "\left(\pi t,0\\right)",
                "a \le t\le a",
                "\left(\sin\left(t\\right),\cos\left(t\\right)\\right)",
                "a_{2} \le t\le a_{2}",
                "\left(\sin\left(t\\right),\cos\left(t\\right)\\right)",
                "a_{2}+\pi \le t\le a_{2}+\pi",
                "a=\sin\left(v\\right)",
                "a_{2}=\\frac{a\pi}{2}",
                "This one is unique loading screen",
            ],
            # index 5
            [
                "\left(\pi t,0\\right)",
                "a \le t\le a",
                "\left(\sin\left(t\\right),\cos\left(t\\right)\\right)",
                "a_{2} \le t\le a_{2}",
                "\left(\sin\left(t\\right)+\\frac{\pi}{2},\cos\left(t\\right)\\right)",
                "a_{3} \le t\le a_{3}",
                "a_{3}=\pi\left(\\frac{\sin(v)}{2}+1\\right)",
                "I have another werid dots movement",
            ],
            # index 6
            [
                "\left(\sin\left(t+l+v_{1}\\right),\cos\left(t+l+v_{1}\\right)\\right)",
                "0 \le t\le 0",
                "l=\left[\\frac{\pi}{4},2\\frac{\pi}{4}...,2\pi\\right]",
                "Now this is looks like generic animation",
            ],
            # index 7
            [
                "\left(\sin\left(t+l-1.1v_{1}\\right),\cos\left(t+l-1.1v_{1}\\right)\\right)",
                "0 \le t\le 0",
                "l=\left[\\frac{\pi}{4},2\\frac{\pi}{4}...,2\pi\\right]",
                "lets stack the previous one with this",
            ],
            # index 8
            [
                "\left(2\sin\left(t+l+k_{1}\\right),2\cos\left(t+l+k_{1}\\right)\\right)",
                "0 \le t\le 0.2",
                "k_{1}=2\pi\sin\left(v_{1}\\right)",
                "l=\left[\\frac{\pi}{4},2\\frac{\pi}{4}...,2\pi\\right]",
                "Here i use sine rate of function",
            ],
            # index 9
            [
                "\left(\cos\left(t\\right),\sin\left(t\\right)\\right)",
                "v-1 \le t\le v",
                "\left(\cos\left(t\\right),\sin\left(t\\right)\\right)",
                "v \le t\le v",
                "Now lets play with worm",
            ],
            # index 10
            [
                "\left(\cos\left(t\\right)\sin\left(t\\right),\sin\left(t\\right)\\right)",
                "v-1 \le t\le v",
                "\left(\cos\left(t\\right)\sin\left(t\\right),\sin\left(t\\right)\\right)",
                "v \le t\le v",
                "Lets change his movement path",
            ],
            # index 11
            [
                "\left(3\cos\left(t\\right)\sin\left(t\\right),\sin\left(3t\\right)\\right)",
                "v \le t\le v",
                "\left(3\cos\left(t\\right)\sin\left(t\\right),\sin\left(3t\\right)\\right)",
                "v-1 \le t\le v",
                "Longer!",
            ],
            # index 12
            [
                "\left(3\cos\left(t\\right)\sin\left(t\\right)-\cos\left(3t\\right),\sin\left(3t\\right)+\cos\left(5t\\right)\\right)",
                "v \le t\le v",
                "v- 0.5 \le t\le v",
                "\left(3\cos\left(t\\right)\sin\left(t\\right)-\cos\left(3t\\right),\sin\left(3t\\right)+\cos\left(5t\\right)\\right)",
                "Haha worm go brr",
            ],
            # index 13
            [
                "\left(\cos\left(t\\right),\sin\left(t\\right)\\right)",
                "v_{2} \le t\le v_{2}+3",
                "\left(\cos\left(t\\right),\sin\left(t\\right)\\right)",
                "-v_{2} \le t\le -v_{2}+2",
                "Not your ordinary circle loading screen",
            ],
            # index 14
            [
                "\left(0.8\cos\left(t\\right),0.8\sin\left(t\\right)\\right)",
                "v_{2}+\pi \le t\le v_{2}+3+\pi",
                "\left(0.8\cos\left(t\\right),0.8\sin\left(t\\right)\\right)",
                "-v_{2}+\pi \le t\le -v_{2}+2+\pi",
                "Stack it up",
            ],
            # index 15
            [
                "\left(\sin\left(t+l1.1v_{1}\\right),\cos\left(t+l1.1v_{1}\\right)\\right)",
                "0 \le t\le 0",
                "l=\left[\\frac{\pi}{4},2\\frac{\pi}{4}...,2\pi\\right]",
                "Have you ever seen loading scree like this?",
            ],
            # index 16
            [
                "\left(\sin\left(t+l1.1v_{1}\\right),\cos\left(t+l1.1v_{1}\\right)\\right)",
                "0 \le t\le 0.5",
                "l=\left[\\frac{\pi}{4},2\\frac{\pi}{4}...,2\pi\\right]",
                "This is one is cool",
            ],
            # index 17
            [
                "\left(\sin\left(t+l+v_{1}\\right),\cos\left(t+l1.1v_{1}\\right)\\right)",
                "0 \le t\le 0",
                "l=\left[\\frac{\pi}{4},2\\frac{\pi}{4}...,2\pi\\right]",
                "Such a weird dots",
            ],
            # index 18
            [
                "\left(\sin\left(t+l+1.1v_{1}\\right),\cos\left(t+l1.1v_{1}\\right)\\right)",
                "0 \le t\le 1",
                "l=\left[\\frac{\pi}{4},2\\frac{\pi}{4}...,2\pi\\right]",
                "So satisfying",
            ],
            # index 19
            [
                "\left(2\sin\left(t+l_{1}+v_{1}\\right),2\cos\left(t+l_{1}+v_{1}\\right)\sin\left(t+l_{1}+v_{1}\\right)\\right)",
                "0 \le t\le 0.2",
                "l_{1}=\left[\\frac{\pi}{8},2\\frac{\pi}{8}...,\\frac{8\pi}{8}\\right]",
                "I think this could really be used",
            ],
            # index 20
            [
                "\left(2\sin\left(t+l_{1}+v_{1}\\right),2\cos\left(t+l_{1}+v_{1}\\right)\\right)",
                "0 \le t\le 0.2",
                "l_{1}=\left[\\frac{\pi}{8},2\\frac{\pi}{8}...,\\frac{8\pi}{8}\\right]",
                "Stacking graphs is certainly a fun thing to do",
            ],


            # index 28
            [
                "\left(0,t+a_{7}\\right)",
                "0 \le t\le 0",
                "\left(t-0.5,-0.4\\right)",
                "0 \le t\le 1",
                "a_{7}=3\left|\sin\left(v_{7}\\right)\\right|",
                "A bouncing ball",
            ],
            # index 29
            [
                "\left(\ 2t,t\left|\sin\left(t\\right)\\right|\\right)",
                "v_{8}-1 \le t\le v_{8}",
                "\left(\ 2t,t\left|\sin\left(t\\right)\\right|\\right)",
                "v_{8} \le t\le v_{8}",
                "Bouncing ball, but it get increasingly higher",
            ],
            # index 30
            [
                "\left(\ t,2\left|\sin\left(t\\right)\\right|+0.1\\right) \pm",
                "v_{8}-2 \le t\le v_{8}a",
                "\left(\ t,-2\left|\sin\left(t\\right)\\right|-0.1\\right) \pm",
                "v_{8}-2 \le t\le v_{8}",
                "Satisfying",
            ],


            # index 21
            [
                "\left(l_{5},t\sin\left(v_{6}+l_{5}\\right)\\right)",
                "l_{5}=\left[-\\frac{3\pi}{8},-\\frac{2\pi}{8},...,\\frac{3\pi}{8}\\right]",
                "-1 \le t\le 1",
                "I think I have seen this one on a website",
            ],
            # index 22
            [
                "\left(l_{2},t\sin\left(v_{6}+l_{2}\\right)\\right)",
                "-1 \le t\le 1",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "Here is the full version of previous graph",
            ],
            # index 23
            [
                "\left(l_{2},t\sin\left(v_{6}+l_{2}\\right)\\right)",
                "0 \le t\le 1",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "I used half the range on this graph, and damn, it's cool",
            ],
            # index 24
            [
                "\left(l_{2},t\sin\left(v_{6}+2\pi l_{2}\\right)\\right)",
                "0 \le t\le 1",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "Here is another version",
            ],
            # index 25
            [
                "\left(l_{2},t+\sin\left(v_{6}+l_{2}\\right)\\right)",
                "0 \le t\le 1",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "Challenge: make a sine wave, but only with straight lines",
                "Also, check out my previous video about the same topic"
            ],
            # index 26
            [
                "\left(l_{2},t\sin\left(v_{6}+l_{2}\\right)\\right)",
                "1 \le t\le 3",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "2 wave. 1 animation. stick only",
            ],
            # index 27
            [
                "\left(l_{2},t+\sin\left(v_{6}+l_{2}\\right)\cos\left(v_{6}+t\\right)\\right)",
                "0 \le t\le 1",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "goofy graph",
            ],

            # index 31
            [
                "m_{1}=\cos\left(l_{8}+v_{11}\\right)",
                "m_{2}=\left(l_{8}+v_{11}\\right)",
                "l_{8}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "\left(t+m_{2},m_{1}\\right)",
                "0 \le t\le 1",
                "\left(m_{2},m_{1}\\right)",
                "\left(m_{2}+1,m_{1}\\right)",
                "Bonus! A snake, dragon, DNA, or whatever you want call it",
            ],
        ]

        lis = [
            [
                "\left(\pi t,0\\right)",
                "a \le t\le a",
                "\left(\sin\left(t\\right),\cos\left(t\\right)\\right)",
                "a_{2} \le t\le a_{2}",
                "\left(\sin\left(t\\right),\cos\left(t\\right)\\right)",
                "a_{2}+\pi \le t\le a_{2}+\pi",
                "a=\sin\left(v\\right)",
                "a_{2}=\\frac{a\pi}{2}",
                "This one is unique loading screen",
            ],
        ]
        # 1
        for item in lis:
            first_eq = MathTex(item[0]).to_edge(UP).set_color(YELLOW).scale(1)

            mini_text = Text(item[-1]).scale(0.5).set_color("##e0e0e0")            
            variables = {}
            equations = item[1:-1]
            for i in range(len(equations)):
                # Create variables v1, v2, v3, ..., vn with values 1, 2, 3, ..., n
                variables[f"v{i+1}"] = MathTex(equations[i]).set_color(YELLOW).scale(1)

            vars = [variables[f"v{i}"] for i in range(1, len(equations) + 1)]
            vg = VGroup(first_eq, *vars, mini_text)
            vg.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

            self.wait(0.25)
            [self.play(FadeIn(x, shift=UP)) for x in vg]
            self.wait(2.5)
            self.clear()

# manim -p loading-levels.py Loading
