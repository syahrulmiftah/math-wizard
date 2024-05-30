from manim import *

# manim -p square.py Square

class Square(Scene):
    def construct(self):
        # Create some text
        text = Text("Specific Size Rectangle Example")
        
        # Position the text at the center
        self.add(text)
        
        # Create a rectangle with a specific size
        rectangle = Rectangle(width=6, height=2, color=YELLOW)
        
        # Position the rectangle around the text
        rectangle.move_to(text)
        
        # Add the rectangle to the scene
        self.play(Create(rectangle))
        
        # Wait for a few seconds
        self.wait(2)

        # Remove the rectangle
        self.play(FadeOut(rectangle))
        
        # Wait for a few more seconds before ending the scene
        self.wait(1)

# To render the scene, run the following command in your terminal:
# manim -pql your_script_name.py SpecificSizeRectangleExample
