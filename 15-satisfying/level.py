from manim import *

# manim -p level.py levelOne
# v_\{(\d+)\}



class levelOne(Scene):
    def construct(self):
        self.camera.background_color = "#00ff00"
        lis = [
                "v_{slider}\sin\left(x\\right)=\cos\left(y\\right)+\sin\left(2x\\right)",
                "v_{slider}\left|\sin\left(x\\right)\\right|=\sin\left(y\\right)",
                "v_{slider}\left|\sin\left(x\\right)\\right|=\sin\left(y\\right)+\sin\left(x\\right)",
                "v_{slider}\left|\sin\left(x\\right)\\right|=\cos\left(y\\right)+\sin\left(2x\\right)",
                "v_{slider}\left|\sin\left(x\\right)\\right|=\left|\cos\left(y\\right)\\right|+\sin\left(x\\right)",
                "v_{slider}\sin\left(2x\\right)=\cos\left(y\\right)+\sin\left(x\\right)",
                "v_{slider}\sin\left(2x\\right)+\sin\left(x\\right)=\left|\cos\left(y\\right)+\sin\left(x\\right)\\right|",
                "\sin\left(x\\right)=\cos\left(\sin\left(v_{slider}+y\\right)\\right)+\cos\left(y\\right)",
                "\sin\left(x\\right)=\cos\left(\sin\left(v_{slider}+y+x\\right)\\right)+\cos\left(y\\right)",
                "\sin\left(x+y\\right)=\cos\left(\sin\left(v_{slider}+y\\right)\\right)+\cos\left(y\\right)",
                "\sin\left(x\\right)=\cos\left(\sin\left(v_{slider}+y+2x\\right)\\right)+\cos\left(y\\right)",
                "\left|\sin\left(x\\right)\\right|=\cos\left(\sin\left(v_{slider}+y\\right)\\right)+\cos\left(y\\right)",
                "\sin\left(x\\right)=\cos\left(\sin\left(v_{slider}+y\\right)+y\\right)+\cos\left(y\\right)",
                "\sin\left(x\\right)=\cos\left(\sin\left(v_{slider}+y\\right)+\left|y\\right|\\right)+\cos\left(y\\right)",
                "\sin\left(x\\right)=\cos\left(\sin\left(v_{slider}+y\\right)+x\\right)+\cos\left(y\\right)",
                "v_{slider}\sin\left(\cos\left(x\\right)+\sin\left(y\\right)\\right)=\cos\left(\sin\left(y\\right)+\cos\left(x\\right)\\right)",
                "v_{slider}\sin\left(\cos\left(x\\right)+\left|\sin\left(y\\right)\\right|\\right)=\cos\left(\sin\left(y\\right)+\cos\left(x\\right)\\right)",
                "v_{slider}\sin\left(\cos\left(x\\right)+\sin\left(y\\right)\\right)=\cos\left(\sin\left(y\\right)+\left|\cos\left(x\\right)\\right|\\right)",
                "v_{slider}\sin\left(\cos\left(x\\right)+\sin\left(y\\right)\\right)=\cos\left(\left|\sin\left(y\\right)\\right|+\left|\cos\left(x\\right)\\right|\\right)",
                "v_{slider}\sin\left(v_{slider}\cos\left(x\\right)+\sin\left(y\\right)\\right)=\cos\left(\sin\left(x\\right)+\cos\left(y\\right)\\right)",
                "v_{slider}\sin\left(v_{slider}\cos\left(x\\right)+\sin\left(y\\right)\\right)=\cos\left(\left|\sin\left(x\\right)\\right|+\left|\cos\left(y\\right)\\right|\\right)",
                "v_{slider}\sin\left(v_{slider}\cos\left(x\\right)+\sin\left(y\\right)\\right)=\cos\left(\sin\left(2x\\right)+\cos\left(2y\\right)\\right)",
                "\sin\left(x\\right)=\cos\left(\sin\left(v_{slider}+y\\right)+2x\\right)+\cos\left(y\\right)",
                "\sin\left(x\\right)=\cos\left(\sin\left(v_{slider}+y\\right)+2x\\right)+\cos\left(y+x\\right)",
                "\sin\left(y\\right)+\cos\left(y\\right)=\cos\left(\sin\left(v_{slider}+y\\right)+x\\right)+\left|\cos\left(x\\right)\\right|",
                "\sin\left(y\\right)+\cos\left(2y\\right)=\cos\left(\sin\left(v_{slider}+2y\\right)+x\\right)+\left|\cos\left(x\\right)\\right|",
                "v_{slider}\sin\left(\cos\left(x\\right)+\sin\left(y\\right)+v_{slider}\\right)=\cos\left(\sin\left(x\\right)+\cos\left(y\\right)\\right)",
                "v_{slider}\sin\left(\cos\left(2x\\right)+\sin\left(y\\right)+v_{slider}\\right)=\cos\left(\sin\left(x\\right)+\cos\left(y\\right)\\right)",
                "v_{slider}\sin\left(\cos\left(x\\right)+\sin\left(y\\right)+v_{slider}\\right)=\cos\left(\left|\sin\left(x\\right)\\right|+\cos\left(y\\right)\\right)",
                "v_{slider}\sin\left(\cos\left(x\\right)+\sin\left(y\\right)\\right)=\left|\cos\left(\left|\sin\left(x\\right)\\right|+\cos\left(y\\right)\\right)\\right|",
        ]

        rectangle = Rectangle(
            width=config.frame_width + 5,
            height=config.frame_height + 5
        )
        rectangle.set_fill(YELLOW, opacity=1)
        
             
        for item in lis:
            self.camera.background_color = "#00ff00"
            graph = MathTex(item).scale(0.75).set_color(WHITE)

            self.wait(0.25)
            self.play(FadeIn(graph, shift=UP))
            self.wait(6)
            self.camera.background_color = "#FF00AD"
            self.wait(0.1)
            self.clear()

# manim -p -t level.py LevelOne