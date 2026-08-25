from manim import *
import sympy as sp
import numpy as np
final_coefficients=[]
final_powers=[]
null_points=[]
extreme_points=[]
turning_points=[]

zeros_x_coords=[[],[],[]]
class Derivatives(Scene):
    
    def construct(self):
        coefficients=[]
        powers=[]
        accepted=False
        while accepted==False:
            accepted=True
            func=str(input())
            fu=func.split("+")
            
            for f in fu:
                has_x=False
                coefficient=""
                power=""
                for a in f:
                    
                    if 47<ord(a)<58 or a=="-" or a==".":
                        if has_x != True:
                            coefficient=coefficient+a
                        else:
                            power=power+a
                    else:
                        has_x=True
                try:

                    coefficients.append(float(coefficient))
                    powers.append(int(power))
                except:
                    accepted=False
                    print("Invalid Input")
                    
                    
                
        
        self.create_functions(coefficients,powers)
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
        
        for i,(co,po) in enumerate(zip(final_coefficients,final_powers)):
            if i !=3:
                y=self.final_function(0,co,po)
                if y<lowest_y_value:
                    lowest_y_value=y
                if y>highest_y_value:
                    highest_y_value=y
        
        x_val=round(1.5*max(highest_x_value,abs(lowest_x_value)))
        y_val=round(2*max(highest_y_value,abs(lowest_y_value)))
        if x_val==0:
            x_val=5
        if y_val==0:
            y_val=5
        x_step=round(x_val/4)
        if x_step==0:
            x_step=1
        y_step=round(y_val/4)
        if y_step==0:
            y_step=1
        ax=Axes(
            (-x_val,x_val,x_step),
            (-y_val,y_val,y_step),
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
        texts=[]
        zeros=[]
        ze=Tex("Zeros").scale(0.7).to_corner(DL).shift(2.5*UP)
        zeros.append(ze)
        self.add(ze)
        hiding_rects=VGroup(
            Rectangle(stroke_width=0,fill_color=BLACK,fill_opacity=0.5) for i in range(0,4)
        )
        hiding_rects[0].to_corner(UL)
        hiding_rects[1].to_corner(DL)
        hiding_rects[2].to_corner(UR)
        hiding_rects[3].to_corner(DR)
        
        
        for i in range(0,3):
            coefficients=final_coefficients[i]
            powers=final_powers[i]
            if i==0:
                op=1
            else:
                op=0.5
            
            ranges=[]
            in_frame=False
            current_lower_boundary=0
            current_upper_boundary=0
            cur=[]
            for x in np.arange(float(-x_val),float(x_val),0.1):
                            
                if abs(self.final_function(x,coefficients,powers))<abs(y_val):
                    if not in_frame:
                        current_lower_boundary=x-0.1
                    in_frame=True
                else:
                    if in_frame:
                        current_upper_boundary=x+0.1
                        ranges.append([current_lower_boundary,current_upper_boundary])
                    in_frame=False
            for r in ranges:
                cur.append(ax.plot(lambda x:self.final_function(x,coefficients,powers),color=colors[i],x_range=(r[0],r[1])).set_stroke(opacity=op).set_z_index(-2))
            #print(self.final_function(0.5,coefficients,powers))
            tec:MathTex
            curves.append(cur)
            if i==0:
                text=rf"f(x)="
            elif i==1:
                text=rf"f'(x)="
            elif i==2:
                text=rf"f''(x)="
            for j,co in enumerate(zip(coefficients,powers)):
                if j==0 or str(co[0])[0]=="-" or co[1]<0:
                    pass
                else:
                    text+="+"
                if co[1]==0:
                    text=text+rf"{co[0]}"
                elif co[1]==1:
                    text=text+rf"{co[0]}*x"
                elif co[1]<0:
                    text=text
                else:
                    text=text+rf"{co[0]}*x^{{{co[1]}}}"
            if i==0:
                tec=MathTex(text,color=colors[i]).scale(0.5).to_corner(UL)
                texts.append(tec.copy())
            elif i==1:
                tec=MathTex(text,color=colors[i]).scale(0.5).to_corner(UL).shift(0.5*DOWN)
                texts.append(tec.copy())
            elif i==2:
                tec=MathTex(text,color=colors[i]).scale(0.5).to_corner(UL).shift(DOWN)
                
                texts.append(tec.copy())
            
            
                
                
                
            
            hiding_rects[0].stretch_to_fit_height(i*0.5+0.5)
            hiding_rects[0].stretch_to_fit_width(tec.get_width())
            hiding_rects[0].move_to(tec.get_center())
            hiding_rects[0].align_to(tec,DOWN).set_z_index(-1)
           # print(self.final_function(2,coefficients,powers))
            #print(self.zero_points(coefficients,powers))
            
            solutions=zeros_x_coords[i]
            #self.add(cur,tec)
           
            current_zeros=[]
            if solutions:
                for s in solutions:
                    so=s.evalf(3)
                    ze=Tex(str(so),color=colors[i]).scale(0.5).to_corner(DL).shift(RIGHT*(len(current_zeros)))
                    zeros.append(ze)
                    current_zeros.append(ze)
                    #self.add(ze)
                points=VGroup(
                    *[Dot(ax.c2p(sol, 0), color=colors[i]) for sol in solutions]
                )
                null_points.append(points)
                
            zero_v_group=VGroup(*current_zeros).shift(UP*(2.5-(0.5*i+0.5)))
            hiding_rects[1].stretch_to_fit_height(i*0.5+1)
            hiding_rects[1].stretch_to_fit_width(zero_v_group.get_width())
            hiding_rects[1].move_to(zero_v_group.get_center())
            hiding_rects[1].align_to(zero_v_group,DOWN).set_z_index(-1)
            self.add(
                VGroup(*cur),
                texts[i],
                points,
                zero_v_group
            )
            
            
        #Extreme Points
        title=Tex("Extreme Points").scale(0.7).to_corner(UR)

        
        
        
        extremes=VGroup(
            *[Dot(ax.c2p(ex[0], ex[1]), color=colors[1]) for ex in extreme_points]
        )
        extreme_labels=VGroup(
            *[MathTex(rf"{ex[2]} ({ex[0]} ,{ex[1]})",color=colors[1]).scale(0.5).to_corner(UR).shift(DOWN*(i/2+0.5)) for i,ex in enumerate(extreme_points)]
        )
        hiding_rects[2].stretch_to_fit_height(len(extreme_labels)*0.5+0.5)
        hiding_rects[2].stretch_to_fit_width(extreme_labels.get_width())
        hiding_rects[2].move_to(extreme_labels.get_center())
        hiding_rects[2].align_to(extreme_labels,DOWN).set_z_index(-1)
        #for n in null_points:
            #self.remove(n)
        #self.remove(curves[2])
        #self.add(extremes,extreme_labels)
        
        
        tu=Tex("Turning Points").scale(0.7).to_corner(DR).shift(2.5*UP)
        
        #Turning Points
        
        
        turns=VGroup(
            *[Dot(ax.c2p(tu[0], tu[1]), color=colors[2]) for tu in turning_points]
        )
        turning_labels=VGroup(
            *[MathTex(rf"{tu[2]} ({tu[0]} ,{tu[1]})",color=colors[2],tex_to_color_map={"R":YELLOW,"L":PURPLE}).scale(0.5).to_corner(DR).shift(UP*(2-(i/2))) for i,tu in enumerate(turning_points)]
        )
        hiding_rects[3].stretch_to_fit_height(len(turning_labels)*0.5+0.5)
        hiding_rects[3].stretch_to_fit_width(turning_labels.get_width())
        hiding_rects[3].move_to(turning_labels.get_center())
        hiding_rects[3].align_to(turning_labels,DOWN).set_z_index(-1)
        #self.add(curves[2])
        #self.remove(curves[1],extremes)
        #self.add(turns,turning_labels)
        show_curves=[]
        for i in range(0,len(turning_points)):
            
            if turning_points[i][2][0]=="R":
                col=YELLOW
            else:
                col=PURPLE
            if i==0:
                cur=ax.plot(lambda x:self.final_function(x,final_coefficients[0],final_powers[0]),color=col,x_range=(-x_val,turning_points[i][0])).set_z_index(-2)
            else:
                cur=ax.plot(lambda x:self.final_function(x,final_coefficients[0],final_powers[0]),color=col,x_range=(turning_points[i-1][0],turning_points[i][0])).set_z_index(-2)
            show_curves.append(cur)
        
        if turning_points !=[]:
            if turning_points[len(turning_points)-1][2][2]=="R":
                col=YELLOW
            else:
                col=PURPLE
            cur=ax.plot(lambda x:self.final_function(x,final_coefficients[0],final_powers[0]),color=col,x_range=(turning_points[len(turning_points)-1][0],x_val)).set_z_index(-2)
            show_curves.append(cur)
        if len(null_points) >=2:
            self.remove(
                null_points[1],
                
            )
            if len(null_points)>=3:
                self.remove(
                    
                    null_points[2]
                )
        self.add(
            title,
            VGroup(*extreme_labels),
            VGroup(*extremes),
            tu,
            VGroup(*turning_labels),
            VGroup(*turns),
            VGroup(*show_curves),
            hiding_rects,


        )
        self.wait(3)


    def create_functions(self,coefficients,powers):
        for i in range(0,4):
            final_coefficients.append(coefficients.copy())
            final_powers.append(powers.copy())
            solutions=self.zero_points(coefficients,powers,i)
            if i !=3:
                if solutions:
                    try:
                        for s in solutions:
                            
                            
                            #print(s)
                            zeros_x_coords[i].append(s)
                            
                    except:
                        print("weird shit")
                    zeros_x_coords[i].sort()
                for i in range(0,len(powers)):
                    coefficients[i],powers[i]=self.make_derivative(coefficients[i],powers[i])
        
    def make_derivative(self,co,pow):
        co=round(co*pow,3)
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
                extreme_points.append([p.evalf(3),self.final_function(p.evalf(3),final_coefficients[0],final_powers[0]).evalf(3)])
            extreme_points.sort(key=lambda item: item[0])
        if iteration==2:
            for p in extreme_points:
                value=""
                second_derivative_value=self.final_function(p[0],final_coefficients[2],final_powers[2])
                
                if second_derivative_value==0:
                    value="TEP"
                if second_derivative_value>0:
                    value="TIP"
                if second_derivative_value<0:
                    value="HOP"
                p.append(value)
            if points:
                
                for p in points:
                    
                    turning_points.append([p.evalf(3),self.final_function(p.evalf(3),final_coefficients[0],final_powers[0]).evalf(3)])
                turning_points.sort(key=lambda item: item[0])
        if iteration==3:
            for i,p in enumerate(turning_points):
                value=""
                third_derivative_value=self.final_function(p[0],final_coefficients[3],final_powers[3])
                
                if third_derivative_value==0:
                    left_value=self.final_function(p[0].evalf(3)-0.01,final_coefficients[2],final_powers[2])
                    right_value=self.final_function(p[0].evalf(3)+0.01,final_coefficients[2],final_powers[2])
                    
                    value=""
                    if left_value>0:
                        value=value+"L-"
                    else:
                        value=value+"R-"

                    if right_value>0:
                        value=value+"L"
                    else:
                        value=value+"R"
                if third_derivative_value>0:
                    value="R-L"
                if third_derivative_value<0:
                    value="L-R"
                p.append(value)
            

        return(points)
    
