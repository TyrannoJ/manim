from manim import *
import sympy as sp

functions=[]
null_points=[]
extreme_points=[]
turning_points=[]

class Derivatives(Scene):
    
    def construct(self):
        coefficients=[1,2,7]
        powers=[5,3,2]
        
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
        ze=Tex("Zeros").scale(0.7).to_corner(DL).shift(2.5*UP)
        zeros.append(ze)
        self.add(ze)
        texts=[]
        texts.append(tex)
        
        #self.add(tex)
        for i in range(0,3):
            functions.append(coefficients.copy())
            functions.append(powers.copy())
            if i==0:
                op=1
            else:
                op=0.5
            cur=ax.plot(lambda x:self.final_function(x,coefficients,powers),color=colors[i],x_range=(-3,3)).set_stroke(opacity=op)
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
           # print(self.final_function(2,coefficients,powers))
            #print(self.zero_points(coefficients,powers))
            solutions=self.zero_points(coefficients,powers,i)
            
            self.add(cur,tec)
            #self.play(
                #Create(cur),
                #Transform(
                        #texts[i],
                        #tec
                    #),
                #run_time=3
            #)
            if solutions:
                for s in solutions:
                    so=s.evalf(3)
                    ze=Tex(so,color=colors[i]).scale(0.5).to_corner(DL).shift(UP*(2.5-(len(zeros)/2)))
                    zeros.append(ze)
                    self.add(ze)
                points=VGroup(
                    *[Dot(ax.c2p(sol, 0), color=colors[i]) for sol in solutions]
                )
                null_points.append(points)
                self.add(points)
            
            for i in range(0,len(powers)):
                coefficients[i],powers[i]=self.make_derivative(coefficients[i],powers[i])
        
        title=Text("Extreme Points").scale(0.5).to_corner(UR)
        
        self.add(title)
        
        extremes=VGroup(
            *[Dot(ax.c2p(ex[0], ex[1]), color=BLUE) for ex in extreme_points]
        )
        extreme_labels=Group(
            *[MathTex(rf"{ex[2]} ({ex[0]} ,{ex[1]})",color=BLUE).scale(0.5).to_corner(UR).shift(DOWN*(i/2+0.5)) for i,ex in enumerate(extreme_points)]
        )
        for n in null_points:
            self.remove(n)
        self.remove(curves[2])
        self.add(extremes,extreme_labels)
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
    def zero_points(self,co,po,iteration):
        x = sp.Symbol('x')
        a=0
        for i in range(0,len(po)):
            if po[i]>=0:
                a=a+co[i]*x**po[i]
        
        points=sp.solveset(a,x,domain=sp.S.Reals)
        if iteration==1 and points:
            
            for p in points:
                extreme_points.append([p.evalf(3),self.final_function(p.evalf(3),functions[0],functions[1])])
        if iteration==2:
            for p in extreme_points:
                value=""
                second_derivative_value=self.final_function(p[0].evalf(3),functions[4],functions[5])
                if second_derivative_value==0:
                    value="TEP"
                if second_derivative_value>0:
                    value="TIP"
                if second_derivative_value<0:
                    value="HOP"
                p.append(value)

        return(points)
    
