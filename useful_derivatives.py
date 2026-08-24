from manim import *

class Derivatives(Scene):
    def construct(self):
        coefficients=[1,2,2]
        powers=[5,3,3]
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
        colors=color_gradient([BLUE,RED],3)
        tex=MathTex("f(x)=").to_corner(UL).scale(0.5)
        texts=[]
        texts.append(tex)
        self.add(tex)
        for i in range(0,3):
            cur=ax.plot(lambda x:self.final_function(x,coefficients,powers),color=colors[i],x_range=(-2,2))
            curves.append(cur)
            if i==0:
                text=rf"f(x)="
                for co in zip(coefficients,powers):

                    text=text+rf"+{co[0]}*x^{co[1]}"
                tec=MathTex(text).scale(0.5).to_corner(UL)
                texts.append(tec.copy())
                    
            elif i==1:
                text=rf"f'(x)="
                for co in zip(coefficients,powers):

                    text=text+rf"+{co[0]}*x^{co[1]}"
                tec=MathTex(text).scale(0.5).to_corner(UL).shift(0.5*DOWN)
                texts.append(tec.copy())
                
            elif i==2:
                text=rf"f''(x)="
                for co in zip(coefficients,powers):

                    text=text+rf"+{co[0]}*x^{co[1]}"
                tec=MathTex(text).scale(0.5).to_corner(UL).shift(DOWN)
                texts.append(tec.copy())
                
            self.play(
                Create(cur),
                Transform(
                        texts[i],
                        tec
                    ),
                run_time=3
            )
            for i in range(0,len(powers)):
                coefficients[i],powers[i]=self.make_derivative(coefficients[i],powers[i])
        
        
    def make_derivative(self,co,pow):
        co=co*pow
        pow-=1
        return co,pow
    def final_function(self,x,co,po):
        y=0
        for i in range(0,len(po)):
            
            y=y+co[i]*pow(x,po[i])
        return y