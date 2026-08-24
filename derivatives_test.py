from manim import *

class Derivatives(Scene):
    def construct(self):
        coefficient=1
        power=7
        ax=Axes(
            (-3,3),
            (-6,6),
            12,
            6
        )
        self.add(ax)
        curves=[]
        
        tex=MathTex("").to_corner(UL)
        while power>0:
            cur=ax.plot(lambda x: (coefficient*pow(x,power)),color=RED,x_range=(-2,2))
            curves.append(cur)
            self.play(
                Create(cur),
                Transform(
                        tex,
                        MathTex(rf"f(x)={coefficient}*x^{power}").to_corner(UL)
                    ),
                run_time=3
            )
            coefficient,power=self.make_derivative(coefficient,power)
    def make_derivative(self,co,pow):
        co=co*pow
        pow-=1
        return co,pow
