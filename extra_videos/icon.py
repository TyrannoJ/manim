from manim import *
config.pixel_width = 512
config.pixel_height = 512
class Icon(Scene):
    def construct(self):
        text=Typst("$f'$").scale(29)
        self.add(text)