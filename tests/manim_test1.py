from manim import *

class Ex(Scene):
    def construct(self):
        
        ax=Axes((-6,6),(-6,6),6,6)
        curve=ax.plot(lambda x: (x),color=RED,x_range=(-6,6))
        curve2=ax.plot(lambda x: (x*x*x),color=BLUE,x_range=(-3,3))
        self.play(Create(ax),Create(curve),run_time=3)
        curve3=curve.copy()
       # self.add(curve3)
       # self.play(Transform(curve,curve2),run_time=5)
        curves=[]
        tex=Text("")
        self.add(tex)
        for a in range(0,10):
            if a==0:
                cur=ax.plot(lambda x: (a * pow(x,2)),color=RED,x_range=(-6,6))
            else:
                cur=ax.plot(lambda x: (1/a * pow(x,2)),color=RED,x_range=(-6,6))
            
            
            curves.append(cur)
            if a==0:
                self.play(Transform(curve,curves[0]),Transform(tex,Text(str(a))))
            else:
                self.play(Transform(curve,curves[a]),Transform(tex,Text(str(a))))


