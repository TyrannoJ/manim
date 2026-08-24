from manim import *
import sympy as sp

final_coefficients=[]
final_powers=[]
null_points=[]
extreme_points=[]
turning_points=[]
coefficients=[1,2,7]
powers=[5,3,2]
zeros_x_coords=[[],[],[]]
class Derivatives(Scene):
    
    def construct(self):
        
        self.create_functions()
        highest_x_value=0
        lowest_x_value=0
        for ze in zeros_x_coords:
            for z in ze:
                if z>highest_x_value:
                    highest_x_value=z
                if z<lowest_x_value:
                    lowest_x_value=z
        highest_y_value=0
        lowest_y_value=0
        for ex in extreme_points:
            if ex[1]>highest_y_value:
                highest_y_value=ex[1]
            if ex[1]<lowest_y_value:
                lowest_y_value=ex[1]
        for tu in turning_points:
            if tu[1]>highest_y_value:
                highest_y_value=tu[1]
            if tu[1]<lowest_y_value:
                lowest_y_value=tu[1]
        print(lowest_x_value)
        x_val=round(3*max(highest_x_value,abs(lowest_x_value)))
        y_val=round(4*max(highest_y_value,abs(lowest_y_value)))
        if x_val==0:
            x_val=5
        if y_val==0:
            y_val=5
        print(x_val)
        print(y_val)
        ax=Axes(
            (-x_val,x_val,round(x_val/4)),
            (-y_val,y_val,round(y_val/4)),
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

        #Add functions
        
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
        
        self.add(tex)
        for i in range(0,3):
            coefficients=final_coefficients[i]
            powers=final_powers[i]
            if i==0:
                op=1
            else:
                op=0.5
            cur=ax.plot(lambda x:self.final_function(x,coefficients,powers),color=colors[i],x_range=(-10,10)).set_stroke(opacity=op)
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
            
            solutions=zeros_x_coords[i]
            #self.add(cur,tec)
            
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
                #self.add(points)
            self.play(
                Create(cur),
                Transform(
                        texts[i],
                        tec
                    ),
                
                run_time=3
            )
            self.play(
                Create(points),
            )
            
            
        #Extreme Points
        title=Text("Extreme Points").scale(0.5).to_corner(UR)

        self.wait(2)
        self.add(title)
        
        extremes=VGroup(
            *[Dot(ax.c2p(ex[0], ex[1]), color=colors[0]) for ex in extreme_points]
        )
        extreme_labels=Group(
            *[MathTex(rf"{ex[2]} ({ex[0]} ,{ex[1]})",color=colors[0]).scale(0.5).to_corner(UR).shift(DOWN*(i/2+0.5)) for i,ex in enumerate(extreme_points)]
        )
        for n in null_points:
            self.remove(n)
        self.remove(curves[2])
        self.add(extremes,extreme_labels)

        self.wait(2)

        #Turning Points
        tu=Tex("Turning Points").scale(0.7).to_corner(DR).shift(2.5*UP)
        self.add(tu)
        turns=VGroup(
            *[Dot(ax.c2p(tu[0], tu[1]), color=colors[0]) for tu in turning_points]
        )
        turning_labels=Group(
            *[MathTex(rf"{tu[2]} ({tu[0]} ,{tu[1]})",color=colors[0]).scale(0.5).to_corner(DR).shift(UP*(2-(i/2))) for i,tu in enumerate(turning_points)]
        )
        self.add(curves[2])
        self.remove(curves[1],extremes)
        self.add(turns,turning_labels)
        self.wait(3)


    def create_functions(self):
        for i in range(0,4):
            final_coefficients.append(coefficients.copy())
            final_powers.append(powers.copy())
            solutions=self.zero_points(coefficients,powers,i)
            if solutions:
                for s in solutions:
                    zeros_x_coords[i].append(s)
            for i in range(0,len(powers)):
                coefficients[i],powers[i]=self.make_derivative(coefficients[i],powers[i])
        
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
                extreme_points.append([p.evalf(3),self.final_function(p.evalf(3),final_coefficients[0],final_powers[0])])
        if iteration==2:
            for p in extreme_points:
                value=""
                second_derivative_value=self.final_function(p[0].evalf(3),final_coefficients[2],final_powers[2])
                if second_derivative_value==0:
                    value="TEP"
                if second_derivative_value>0:
                    value="TIP"
                if second_derivative_value<0:
                    value="HOP"
                p.append(value)
            for p in points:
                turning_points.append([p.evalf(3),self.final_function(p.evalf(3),final_coefficients[0],final_powers[0])])
        if iteration==3:
            for p in turning_points:
                value=""
                third_derivative_value=self.final_function(p[0].evalf(3),final_coefficients[3],final_powers[3])
                if third_derivative_value==0:
                    value="?"
                if third_derivative_value>0:
                    value="R-L"
                if third_derivative_value<0:
                    value="L-R"
                p.append(value)
            

        return(points)
    
