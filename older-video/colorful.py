
from manim import *
import math

# cd it-gets-better/colorful-graph
# manim -p colorful.py Colorful

class Colorful(MovingCameraScene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-15, 15, 1),
            y_range=(-10, 10, 1),
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(1)
        self.add(number_plane)
        #self.play(self.camera.frame.animate.scale(1/3).move_to(ORIGIN))

        def a(theta): return np.tan(theta * 1.1)

        graph = number_plane.plot_polar_graph(
            a,
            theta_range=[0, 10 * np.pi, 0.01],
            color="#fcfc03",
            use_smoothing=True,

        )

        # graph.set_stroke(width=2)
        self.camera.frame.save_state()

        self.play(Create(graph), run_time=5)
        #self.play(self.camera.frame.animate.scale(3).move_to(ORIGIN), rate_func=smooth, run_time=1)


        self.wait(1)

