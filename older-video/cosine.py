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

        curves = [
            lambda t, tracker: (
                (np.cos(tracker.get_value() * t) + 2) * np.cos(t),
                (np.cos(tracker.get_value() * t) + 2) * np.sin(t),
                0
            ),
            lambda t, tracker: (
                (np.cos(tracker.get_value() * t) + 1) * np.cos(t),
                (np.cos(tracker.get_value() * t) + 1) * np.sin(t),
                0
            )
        ]

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
