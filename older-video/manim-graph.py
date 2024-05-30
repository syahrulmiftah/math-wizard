from manim import *

# manim -p -ql manim-graph.py ManimUpdater
# manim -p manim-graph.py ManimUpdater


class ManimUpdater(MovingCameraScene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-7.5, 7.5, 1),
            y_range=(-4.5, 4.5, 1),
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(1)

        self.add(number_plane)

        graph_tracker = ValueTracker(0)

        range_tracker = ValueTracker(1)

        equation_tracker = ValueTracker(1)

        to_plot = always_redraw(lambda: ParametricFunction(
            lambda t: number_plane.polar_to_point(
                np.sin(t * graph_tracker.get_value()), t),
            color="#FF0000",
            t_range=[0, range_tracker.get_value() * np.pi],
        ))

        to_plot2 = always_redraw(lambda: ParametricFunction(
            lambda t: number_plane.polar_to_point(
                np.arccos(np.cos(t - graph_tracker.get_value())), t),
            color="#FF0000",
            t_range=[0, 2 * np.pi],
        ))

        equation = always_redraw(MathTex("r=\\arccos\left(\cos\left(\\theta\\right)\\right)"))

        self.play(Create(to_plot2, run_time=3))
        self.wait(1)
        self.play(graph_tracker.animate.set_value(1), run_time=3)
        # self.play(range_tracker.animate.set_value(12), run_time=5)
        self.wait(1)

# manim -p -ql manim-graph.py ManimUpdater
# manim -p manim-graph.py ManimUpdater
