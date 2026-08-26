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
        colors=color_gradient([BLUE,RED],power)
        tex=MathTex("").to_corner(UL)
        i=0
        while power>0:
            cur=ax.plot(lambda x: (coefficient*pow(x,power)),color=colors[i],x_range=(-2,2))
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
            i+=1
    def make_derivative(self,co,pow):
        co=co*pow
        pow-=1
        return co,pow
