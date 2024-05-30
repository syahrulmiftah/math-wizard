from manim import *
import math


class ThumbnailPolar(Scene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-30, 30, 1),
            y_range=(-20, 20, 1),
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(1)
        self.add(number_plane)

        # self.camera.frame.shift(UP*3.5).scale(1.1)
        # self.camera.frame.scale(3)

        trange = (0, 2 * np.pi)

        def level1(t): return (np.sin(t) + np.cos(t), np.cos(t))
        def level2(t): return (np.sin(5*t) + np.cos(t), np.cos(t))

        graph = number_plane.plot_parametric_curve(
            level1,
            t_range=trange,
            color="#40FC00",
        )
        graph.set_stroke(width=7)

        self.add(graph)

# 40FC00
# fcfc03
# ff0000
