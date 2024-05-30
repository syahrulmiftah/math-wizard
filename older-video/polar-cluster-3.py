from manim import *


class Cluster3(MovingCameraScene):
    def construct(self):
        self.background_color = None
        number_plane = NumberPlane(
            x_range=(-30, 30, 1),
            y_range=(-15, 15, 1),
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(1)

        def g1(theta):
            return 5 * np.sin(theta / 5)

        def g2(theta):
            return 5 * np.sin(theta / 4)

        def g3(theta):
            return 5 * np.sin(3 * theta / 7)

        def g4(theta):
            return 5 * np.sin(2 * theta / 5)

        def g5(theta):
            return 5 * np.sin(5 * theta / 9)

        def g6(theta):
            return 5 * np.sin(3 * theta / 4)

        colorlist = ["#40FC00", "#fcfc03", "#FF9933",
                     "#FF0000", "#336FFF", "#CC33FF", "#33FFFF"]
        functionlist = [g1, g2, g3, g4, g5, g6]
        pi = [5, 8, 7, 10, 12, 12]

        for i in range(len(functionlist)):
            self.add(number_plane)
            self.camera.frame.scale(2/3)
            graph = number_plane.plot_polar_graph(
                functionlist[i],
                theta_range=[0,  pi[i] * np.pi, 0.1],
                color=colorlist[i],
                use_smoothing=True
            )
            self.play(self.camera.frame.animate.scale(3).move_to(
                ORIGIN), Create(graph), run_time=10, rate_func=rate_functions.ease_in_out_sine)
            self.wait(1)
            self.clear()
            self.camera.frame.scale(1/2)

# 40FC00     green
# fcfc03     yellow
# FF0066     red
# 336FFF     blue
# CC33FF     magenta
# 33FFFF     cyan
# FF9933     orange
