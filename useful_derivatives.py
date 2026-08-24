from manim import *
import sympy as sp
class Derivatives(Scene):
    def construct(self):
        coefficients=[1,2,7]
        powers=[5,3,2]
        coefficient=1
        power=7
        ax=Axes(
            (-10,10,2),
            (-100,100,20),
            13,
            7,
            x_axis_config={
                "include_numbers": True,
                "include_tip": False,
                
                
            },
            y_axis_config={
                "include_numbers": True,
                "include_tip": False,
                
    },
        )
        
        self.add(ax)
        curves=[]
        colors=color_gradient([BLUE,GREEN,RED],3)
        tex=MathTex("f(x)=").to_corner(UL).scale(0.5)
        zeros=[]
        ze=Tex("Zeros").to_corner(UR).scale(0.5)
        zeros.append(ze)
        self.add(ze)
        texts=[]
        texts.append(tex)
        self.add(tex)
        for i in range(0,3):
            cur=ax.plot(lambda x:self.final_function(x,coefficients,powers),color=colors[i],x_range=(-3,3))
            curves.append(cur)
            if i==0:
                text=rf"f(x)="
                for co in zip(coefficients,powers):
                    if co[1]==0:
                        text=text+rf"+{co[0]}"
                    else:
                     text=text+rf"+{co[0]}*x^{co[1]}"
                tec=MathTex(text,color=colors[i]).scale(0.5).to_corner(UL)
                texts.append(tec.copy())
                    
            elif i==1:
                text=rf"f'(x)="
                for co in zip(coefficients,powers):
                    if co[1]==0:
                        text=text+rf"+{co[0]}"
                    if co[1]>0:
                        text=text+rf"+{co[0]}*x^{co[1]}"
                tec=MathTex(text,color=colors[i]).scale(0.5).to_corner(UL).shift(0.5*DOWN)
                texts.append(tec.copy())
                
            elif i==2:
                text=rf"f''(x)="
                for co in zip(coefficients,powers):
                    if co[1]==0:
                        text=text+rf"+{co[0]}"
                    if co[1]>0:
                        text=text+rf"+{co[0]}*x^{co[1]}"
                tec=MathTex(text,color=colors[i]).scale(0.5).to_corner(UL).shift(DOWN)
                texts.append(tec.copy())
            print(self.final_function(2,coefficients,powers))
            #print(self.zero_points(coefficients,powers))
            solutions=self.zero_points(coefficients,powers)
            
            
            self.play(
                Create(cur),
                Transform(
                        texts[i],
                        tec
                    ),
                run_time=3
            )
            if solutions:
                for s in solutions:
                    so=s.evalf(3)
                    ze=Tex(so,color=colors[i]).scale(0.5).to_corner(UR).shift(DOWN*len(zeros)/2)
                    zeros.append(ze)
                    self.add(ze)
                points=VGroup(
                    *[Dot(ax.c2p(sol, 0), color=colors[i]) for sol in solutions]
                )
                self.add(points)
            for i in range(0,len(powers)):
                coefficients[i],powers[i]=self.make_derivative(coefficients[i],powers[i])
        self.wait(3)
        
    def make_derivative(self,co,pow):
        co=co*pow
        pow-=1
        return co,pow
    def final_function(self,x,co,po):
        y=0
        for i in range(0,len(po)):
            if po[i]>=0:
                y=y+co[i]*pow(x,po[i])
        return y
    def zero_points(self,co,po):
        x = sp.Symbol('x')
        a=0
        for i in range(0,len(po)):
            if po[i]>=0:
                a=a+co[i]*x**po[i]
        points=sp.solveset(a,x,domain=sp.S.Reals)
        return(points)
