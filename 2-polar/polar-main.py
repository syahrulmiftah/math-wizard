from manim import *

# manim -p -ql polar-main.py PolarArc
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

        colorlist = ['#FF0000', '#FF9933', '#FCFC03',
                     '#40FC00', '#33FFFF', '#336FFF', '#CC33FF']

        mini_text = [
            ["r=\\frac{\\theta}{5}",
             "Let's start with the basics"],
            ["r=5\\cdot\\cos\\left(\\theta\\right)",
             "Step 2, start adding trig functions"],
            ["r=\\arcsin\\left(\\theta\\right)",
             "Now we try inverse functions"],
            ["r=\\arctan\\left(\\theta\\right)",
             "This one is better"],
            ["r=\\tanh\\left(\\theta\\right)",
             "How about hyperbolic function?"],
        ]

        graph_to_plot = [
            lambda theta: theta / 5,
            lambda theta: np.cos(theta) * 5,
            lambda theta: np.arcsin(theta),
            lambda theta: np.arctan(theta),
            lambda theta: np.tanh(theta),
        ]

        pi_range = [12, 1, 1/np.pi, 1/np.pi, 1/np.pi]

        self.plot_polar_graph_sequence(
            graph_to_plot, mini_text, number_plane, colorlist, pi_range)

    def plot_polar_graph_sequence(self, graph_to_plot, mini_text, number_plane, colorlist, pi_range):

        for current_index in range(len(mini_text)):
            equation = MathTex(mini_text[current_index][0]).scale(
                1.25).shift(UP).set_color(YELLOW)

            level = Text(mini_text[current_index][1]).scale(
                0.5).next_to(equation, DOWN*3)

            polar_graph = number_plane.plot_polar_graph(
                graph_to_plot[current_index],
                theta_range=[0, pi_range[current_index] * np.pi, 0.05],
                color=colorlist[current_index % 7],
                use_smoothing=True,
            )

            self.wait(0.25)
            self.play(FadeIn(equation))
            self.play(FadeIn(level, shift=UP))
            self.wait(4)
            self.clear()

            self.camera.frame.scale(1/3).move_to(ORIGIN)
            self.add(number_plane)

            self.play(Create(polar_graph), self.camera.frame.animate.scale(
                3).move_to(ORIGIN),  run_time=5, rate_func=smooth)
            self.wait(4)

            self.clear()
            self.wait(0.25)

    # Usage:


# cd it-gets-better/polar-arc

# manim -p -ql polar-main.py PolarArc
# manim -p polar-main.py PolarArc
