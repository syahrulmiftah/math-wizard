from manim import *


class Cluster1(MovingCameraScene):
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
            return theta / 5

        def g2(theta):
            return (theta - np.sin(9 * theta)) / 5

        def g3(theta):
            return (theta - np.sin(theta**2)) / 5

        colorlist = ["#40FC00", "#fcfc03", "#FF0000",
                     "#FF9933", "#336FFF", "#CC33FF", "#33FFFF"]
        functionlist = [g3]
        pi = [12, 12, 12]

        for i in range(len(functionlist)):
            self.add(number_plane)
            self.camera.frame.scale(2/3)
            graph = number_plane.plot_polar_graph(
                functionlist[0],
                theta_range=[0,  pi[0] * np.pi, 0.1],
                color=colorlist[2],
                use_smoothing=True
            )
            self.play(self.camera.frame.animate.scale(3).move_to(
                ORIGIN), Create(graph), run_time=20, rate_func=rate_functions.ease_in_out_sine)
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
