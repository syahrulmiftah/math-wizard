from manim import *


class Cluster1(MovingCameraScene):
    def construct(self):
        self.background_color = None
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

        self.camera.frame.scale(1/3)

        def g1(theta):
            return theta / 8

        def g2(theta):
            return (theta - np.sin(9 * theta)) / 5

        def g3(theta):
            return (theta - np.sin(np.tan(3 * theta))) / 5

        def g4(theta):
            return (theta - np.sin(theta**2)) / 5

        graph = number_plane.plot_polar_graph(
            g4,
            theta_range=[0,  10 * np.pi, 0.1],
            color="#FF0066",
            use_smoothing=True
        )
        # graph.set_stroke(width=5)

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(3).move_to(
            ORIGIN), Create(graph), run_time=20, rate_func=linear)
        self.wait(1)

# 40FC00     green
# fcfc03     yellow
# FF0066     red
# 336FFF     blue
# CC33FF     magenta
# 33FFFF     cyan
# FF9933     orange
