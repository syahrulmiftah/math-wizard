from manim import *

# manim -p onscreen-level.py OnScreen

class OnScreen(Scene):
    def construct(self):
        lis = [
            [
                "So here we have three variables, V, Vsize, and Vtrajectory",
                "The 'V' variable is only used to spin the circle",
                "And the Vsize, as the name suggests, is used to resize the circle",
                "The Vtrajectory is used to correct the trajectory of the circle",
                """
                To make the two circles tangent to each other,

                we need to find the right combination of Vsize and Vtrajectory
                """,
                "And in this case, it's 0.5 for Vsize and 1.5 for Vtrajectory",

            ],
            [
                "I set the first variable, namely V4, up to twice the usual 2π",
                "Now the secret lies in the second variable, namely V5",
                "I make the second variable start increasing once V4 reaches 2π",
                """
                At the first stage of the trace, V5 is zero and V4 starts increasing

                up to 2π. So the circle is being formed fully from the beginning.
                """,
                "At the second stage of the trace, V5 starts increasing",
                "This keeps the upper limit of 't' at 2π.",
                """
                Meanwhile, the lower limit of 't' decreases

                from 2π all the way to 0
                """,
                "This makes the circle erase completely from the end",
                "And the pattern continues indefinitely...",
            ],    
            [
                "Here we have three modifiable variables",
                "K twist is used to give the initial twist to the graph",
                "This creates an illusion of a 3D graph",
                """
                K vertical, as the name implies, is used to rotate the graph vertically

                along the x-axis.
                """,
                """
                Well to be fair, it's not really used to rotate the graph

                because at higher values of 'K' the graph starts to get stretched out.
                """,
                """
                I think it's more like changing the camera angle in a way that

                I'm yet to understand.
                """,
                "It's like zooming in and out while rotating, idk.",
                "K horizontal is exactly the same, but it's for the y-axis or horizontal plane",
                "And that's how you make 3D graphs..."
            ],    
        ]
        lis = [
            [
                "Thats all for today",
                "Thank you for watching...",
            ],
        ]
        for item in lis:
            for x in item:
                txt = Text(x).scale(0.75).set_color(YELLOW).shift(DOWN*3)
                self.play(FadeIn(txt, shift=UP))
                self.wait(3)
                self.clear()
                self.wait(0.25)
            
# manim -p onscreen-level.py OnScreen


           