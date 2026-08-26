from manim import *

class Try(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait()