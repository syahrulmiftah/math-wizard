from manim import *


class Cluster4(MovingCameraScene):
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
            return 2 * np.exp((np.tan((1/3)*theta) / 2) * np.sin((1/3)*theta))

        def g2(theta):
            return 2 * np.exp((np.tan((2/3)*theta) / 2) * np.sin((2/3)*theta))

        def g3(theta):
            return 2 * np.exp((np.tan((3/5)*theta) / 2) * np.sin((3/5)*theta))

        def g4(theta):
            return 2 * np.exp((np.tan((4/5)*theta) / 2) * np.sin((4/5)*theta))

        def g5(theta):
            return 2 * np.exp((np.tan((5/6)*theta) / 2) * np.sin((5/6)*theta))

        def g6(theta):
            return 2 * np.exp((np.tan((6/5)*theta) / 2) * np.sin((6/5)*theta))

        colorlist = ["#40FC00", "#fcfc03", "#FF9933",
                     "#FF0000", "#336FFF", "#CC33FF", "#33FFFF"]
        functionlist = [g1, g2, g3, g4, g5, g6]
        pi = [6, 6, 10, 10, 12, 10]

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
