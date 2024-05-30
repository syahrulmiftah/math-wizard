from manim import *

# manim -p -ql polar-arc.py PolarArc
# cd it-gets-better/polar-arc


class PolarArc(MovingCameraScene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-15, 15, 1),
            y_range=(-8, 8, 1),
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(1)

        polar_plane = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_label_font_size=33.6,
            radius_config={"font_size": 33.6},
        )

        self.add(number_plane)

        noZero = 0.000000000001

        def a(theta):
            denominator = np.sin(99 * theta)
            if denominator == 0:
                return None  # or any other special value you prefer
            else:
                return 1 / denominator

        def b(theta):
            return np.tan(2 * theta)

        def c(t): return (np.cos(t) * np.tan(t), np.tan(t) * np.sin(t))

        def d(x): return np.tan(x)

        def g(x): return ((10**6 * np.abs(np.sin(1.4 * x)) + noZero) / 2)

        def h(theta): return 1 + (((np.abs(np.cos(theta * 3))) + (0.25 - (np.abs(np.cos(
            theta * 3 + np.pi / 2)))) * 2) / (2 + np.abs(np.cos(theta * 6 + np.pi / 2)) * 8))

        graph = number_plane.plot_polar_graph(
            h,
            theta_range=[0, 2 * np.pi, 0.05],
            color="#fcfc03",
            use_smoothing=True,
        )
        graph2 = number_plane.plot_parametric_curve(
            c,
            t_range=(0, 6.28, 0.01),
            color="#f00000",
            use_smoothing=True,
        )
        graph3 = number_plane.plot(
            d,
            color="#33FF57",
            discontinuities=np.arange(-np.pi * 3 / 2, 15, np.pi),
            dt=0.1,
        )
        graph4 = polar_plane.plot(
            g,
            x_range=[0, 2 * np.pi],
            color="#fcfc03",
            use_smoothing=True,
            discontinuities=[0],
            dt=0.1
        )

        # self.play(Create(graph), run_time=5)
        # self.add(graph)

        self.play(Create(graph), run_time=5)
        self.wait(1)

# cd it-gets-better/polar-arc

# manim -p -ql polar-arc.py PolarArc
