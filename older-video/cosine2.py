from manim import *


class CosineUpdater(MovingCameraScene):
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

        tracker = ValueTracker(0)

        t_range = [0, 2 * np.pi]

        curve = always_redraw(lambda: ParametricFunction(
            lambda t: number_plane.polar_to_point(np.cos(t * tracker) + 2, t),
            color="#FF0000",
            t_range=t_range,
        ))

        for curve in curves:
            self.plot_polar_with_tracker(curve, start=2, end=2.5)

    def plot_polar_with_tracker(self, curve, start, end):
        tracker = ValueTracker(start)
        trange = (-7.5, 7.5, 0.1)

        graph = ParametricFunction(
            lambda t: curve(t, tracker),
            color="#00FF66",
            t_range=trange
        )

        self.add(graph)

        graph.add_updater(lambda g: g.become(
            ParametricFunction(
                lambda t: curve(t, tracker),
                color="#00FF66",
                t_range=trange
            )
        ))

        self.play(tracker.animate.set_value(end), run_time=5)


# manim -p -ql cosine.py CosineUpdater
# manim -p cosine.py CosineUpdater
