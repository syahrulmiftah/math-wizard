
from manim import *
import math


class ParametricGraphs(MovingCameraScene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-7.5, 7.5, 1),
            y_range=(-4, 4, 1),
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(1)
        self.add(number_plane)
        # self.play(self.camera.frame.animate.scale(1/3).move_to(ORIGIN))

        def graph1(t): return (np.tan(8 * t), np.sin(9 * t))

        trange = (0, 2 * np.pi)

        graph = number_plane.plot_parametric_curve(
            graph1,
            t_range=trange,
            color="#40FC00",
            # use_smoothing=True,
            # use_vectorized=True
        )

        self.camera.frame.save_state()

        # self.play(Create(graph), run_time=10)
        # self.play(self.camera.frame.animate.scale(3).move_to(ORIGIN), rate_func=smooth, run_time=1)

        self.add(graph)
        # self.wait(1)
