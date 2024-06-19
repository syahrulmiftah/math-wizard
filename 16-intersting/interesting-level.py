from manim import *

# manim -p interesting-level.py Level
# "If you enjoy these graphs, give it a like!",
# "And subscribe for more videos like this"


class Level(Scene):
    def construct(self):
        self.camera.background_color = "#00ff00"
        # 7, 13, 17
        lis = [        
            # chapter 1
            [
                "y=2^{x}-x",
                "Let's start with some uninteresting equations first",
            ],                        
            [
                "3x^{2}+y^{2}=2",
                "You probably still remember how to solve this",
            ],                        
            [
                "y=\left|x\\right|-x",
                "Absolute value, difficult to calculate but sometimes makes nice graphs",
            ],                        
            [
                "y=\log\left(x^{2}\\right)+x",
                "Ah yes, logarithms, who doesn't like them?",
            ],                        
            [
                "r=\\frac{\\theta}{5}",
                "This is a polar graph",
                "A polar graph plots points using distance and angle (θ) from the origin",
            ],                        
            [
                "\sqrt{\sin\left(x\\right)}+\sin\left(\left|x\\right|\\right)",
                "its a crime to not include some trigonometric graphs",
            ],                        
            [
                "\operatorname{ceil}\left(\sin\left(2x\\right)+\cos\left(x\\right)\\right)",
                "The ceiling function rounds a number up to the nearest integer.",
            ],                        
            [
                "\left(\sin\left(t\\right),t+\sin\left(t\\right)\\right)",
                "This is a parametric function",
                "Parametric functions give a way to represent functions with a",
                "one-dimensional input (t) and a multidimensional output.",
            ],                        
            # chapter 2
            [
                "\left|y\\right|^{x}>x^{2}",
                "let's start off with some inequalities",
            ],                        
            [
                "y=\sin\left(x\\right)^{x}",
                "Have you ever thought about this equation?",
            ],                        
            [
                "x^{3}+y^{3}=x+y",
                "Good luck differentiating this one",
            ],                        
            [
                "y=e^{\sin\left(x\\right)}+\left|x\\right|",
                "(e) or Euler's number is a constant approximately equal to 2.71828",
            ],                        
            [
                "\left(t+\sin\left(2t\\right),2\sin\left(t\\right)\\right)",
                "Parametric function can make some weird graph",
            ],                        
            [
                "\ln\left(\cos\left(y\\right)\\right)+y<x",
                "(ln) or The natural logarithm  is the inverse function of the",
                "exponential function with base 'e'",
            ],                        
            [
                "\\frac{x}{\sin\left(x\\right)}=y",
                "It's basically a cosecant function",
            ],                        
            [
                "y+\sin\left(x\\right)=\cos\left(y^{x}\\right)",
                "What if we put exponent inside a trigonometric function",
            ],                        
            [
                "\sin\left(x\\right)+\sin\left(y\\right)=1",
                "o o o o o o",
                "o o o o o o",
                "o o o o o o",
            ],                        
            [
                "r=\operatorname{ceil}\left(\\theta\\right)",
                "This isn't that hard to sketch, but it's beautiful nonetheless.",
            ],                        
            [
                "\left|\\tan\left(x\\right)\\right|=e^{\left(\ln\left(\\tan\left(y\\right)\\right)\\right)}",
                "This is how you make a function look more complicated than it actually is",
            ],                        
            [
                "y<\sin\left(\left|x\\right|\\right)\ln\left(xy\\right)",
                "bright side vs dark side",
            ],                        
            [
                "\gcd\left(x,y\\right)=1",
                "The gcd (greatest common divisor) function finds the",
                "largest number that divides two or more integers without remainder",
                "And the graph is absolutely stunning",
            ],
            # chapter 3                                             
            [
                "\sin\left(x\\right)<\sin\left(y\\right)",
                "So this is how you make a chessboard, huh?",
            ],
            [
                "y=\sin\left(\operatorname{ceil}\left(\left|x\\right|\\right)+3\cos\left(x\\right)\\right)",
                "Looks like some ancient alphabet if you ask me",
            ],
            [
                "e^{2\sin\left(x\\right)+2\csc\left(y\\right)}=y",
                "I'll throw in some random graph and let's call it 'modern art'",
                "Nah, just kidding...",
            ],
            [
                "y=\sec\left(x^{2}\\right)+\sin\left(x\\right)",
                "This graph gets denser the further you move along the x-axis",
            ],
            [
                "\left(\\tan\left(8t\\right),\ \ \cos\left(9t\\right)\\right)",
                "Another simple yet nice pattern",
            ],
            [
                "y=\\frac{2^{x}}{\sin\left(x^{y}\\right)}",
                "It's just random noise at this point",
            ],
            [
                "r=2+\left(\\frac{\left|\cos(3\\theta)\\right|+\\frac{1}{2}-2\left|\cos\left(3\\theta+\\frac{\pi}{2}\\right)\\right|}{2+8\left|\cos(6\\theta+\\frac{\pi}{2})\\right|}\\right)",
                "This is just a glimpse on how you can draw a nice shape with mathematics",
                "Let me know if you want more of this kind of stuff",
            ],
            [
                "r=4-\operatorname{ceil}\left(8\left|\cos\left(4\\theta\\right)^{2}\\right|\\right)",
                "r=4-8\left|\cos\left(4\\theta\\right)^{2}\\right|",
                "I'll give you two graphs, before and after the ceiling function is applied",
            ],
            [
                "y<\\frac{\sin\left(\sin\left(y\\right)\\right)}{x^{\sin\left(x\\right)}}",
                "Inequality graphs is always a pleasure to look at",
            ],
            [
                "r=6\sin\left(1.2\\theta\\right)-\cos\left(6\\theta\\right)",
                "This is the pinnacle of beautiful graphs",
            ],
            [
                "y=\exp\left(\\frac{1}{2}\\arctan\left(100\\tan\left(4x\\right)\\right)\\right)\sin\left(x\\right)",
                "I almost forgot to include some inverse trigonometric functions",
            ],
            [
                "y=x\\tan\left(x^{2}+y^{2}\\right)",
                "You know, sometimes I wonder if this kind of graph has any",
                "real-world applications (other than for art and entertainment)",
            ],
            [
                "\operatorname{lcm}\left(x,y\\right)=2\gcd\left(x,y\\right)",
                "LCM (Least Common Multiple), when combined with the GCD function,",
                "makes for a really nice graph",
            ], 
            [
                "\left(\\tan\left(24.5t\\right),\ \\frac{\sec\left(t\\right)}{\cos\left(50t\\right)}\\right)",
                "This graph gives me chills",
                "It feels like you are in space or at the edge of the universe",
            ],
            [
                "y=\\frac{\sin\left(x\\right)}{\cos\left(y\\right)}x+\cot\left(yx\\right)",
                "This one is probably my favorite",
                "Seems like it's random but still has a pattern, truly mesmerizing",
            ],
            [
                "\cos\left(2xy\\right)=\cos\left(x^{2}+y^{2}\\right)+\cos\left(9x\\right)",
                "Pareidolia is a psychological phenomenon where we tend to perceive",
                "familiar patterns, such as faces or objects, in random or unrelated stimuli.",
            ],
            [
                "\gcd\left(\sec\left(x\\right)+\\frac{\\tan\left(9y\\right)}{\cos\left(3x\\right)},\sin\left(x\\right)y+\cos\left(y\\right)\\tan\left(x\\right)\\right)=1",
                "Nah, this one is just too incomprehensible for us mere mortals",
                "Also, check out my video on incomprehensible graphs",
            ],
        ]
        lis = [            
            [
                "\gcd\left(x,y\\right)=1",
                "The gcd (greatest common divisor) function finds the",
                "largest number that divides two or more integers without remainder",
                "And the graph is absolutely stunning",
            ],            
               
        ]
        # 1
        text_size = 0.9 
        spacing = 0.5

        keywords = [
            "\le", 
            "=", 
            "+",
            ">", 
            "<", 
            "^", 
            ]

        for item in lis:
            self.camera.background_color = "#00ff00"
            variables = {}
            for i in range(len(item)):
                if any(keyword in item[i] for keyword in keywords):
                    variables[f"v{i+1}"] = MathTex(item[i]).scale(text_size*1.2).set_color(YELLOW)
                    counter = i+2    
                else:
                    variables[f"v{i+1}"] = Text(item[i]).scale(text_size/2).set_color(WHITE)


            equations = [variables[f"v{i}"] for i in range(1,counter)]
            texts = [variables[f"v{i}"] for i in range(counter,len(item)+1)]
            vg_equations = VGroup(*equations)
            vg_equations.arrange(DOWN, aligned_edge=LEFT, buff=spacing/2)

            vg_texts = VGroup(*texts)
            vg_texts.arrange(DOWN, aligned_edge=LEFT, buff=spacing/2)

            vg_all = VGroup(vg_equations,vg_texts)
            vg_all.arrange(DOWN, aligned_edge=LEFT, buff=spacing*2)

            self.wait(0.25)
            [self.play(FadeIn(x, shift=UP)) for x in vg_all]
            self.wait(5)
            self.camera.background_color = "#FF00AD"
            self.wait(0.1)
            self.clear()
            

# manim -p interesting-level.py Level