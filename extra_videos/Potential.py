from manim import *

class Potential(Scene):
    def construct(self):
        vertical_size=4
        horizontal_size=6
        points=[
            
            4.5*LEFT+1.5*UP,
            1.5*LEFT+1.5*UP,
            1.5*LEFT,
            1.5*RIGHT,
            1.5*RIGHT+1.5*DOWN,
            4.5*RIGHT+1.5*DOWN,
            4.5*RIGHT+3*DOWN,
            4.5*LEFT+3*DOWN,
            4.5*LEFT+1.5*UP,
            
            ]
        line = VMobject(color=WHITE, stroke_width=6).set_z_index(-2)
        line.set_points_as_corners(points)
        
        title=Text("Das elektrische Potenzial").to_corner(UL)
        
        #self.camera.frame_width*=2
        #self.camera.frame_height*=2
        rectangles=VGroup(
            Rectangle(stroke_width=6,fill_color=BLACK,fill_opacity=1).stretch_to_fit_width(0.8).stretch_to_fit_height(1.4) for i in range(0,3)
        )
        rectangles[0].shift(1.5*LEFT+0.75*UP)
        rectangles[1].shift(1.5*RIGHT+0.75*DOWN)
        rectangles[2].shift(4.5*RIGHT+2.25*DOWN)
        texts=VGroup(
            Text("R"+str(i+1),font_size=30) for i in range(0,3)
        )
        
        for i in range(0,3):
            texts[i].move_to(rectangles[i])
            texts[i]
        minus=Dot(4.5*LEFT+3*DOWN,0.2,color=BLUE)
        plus=Dot(4.5*LEFT+1.5*UP,0.2,color=RED)
        power=Rectangle(stroke_width=6,fill_color=BLACK,fill_opacity=1).stretch_to_fit_width(0.5).stretch_to_fit_height(4.3).shift(4.5*LEFT+0.75*DOWN).set_z_index(-1)
        plus_sign=Text("+",font_size=35).move_to(plus).set_z_index(1)
        minus_sign=Text("-",font_size=35).move_to(minus).set_z_index(1)
        netzgeraet=Text("Netzgerät",font_size=30).move_to(power).rotate(PI/2)
        letters=["A","B","C","D"]
        points=VGroup(
            Text(letters[i],font_size=30) for i in range(0,4)
        )
        potentials=VGroup(
            Typst(rf"$phi_{letters[i]}={8*(3-i)}V$",font_size=35) for i in range(0,4)
        )
        points[0].next_to(rectangles[0],UP) #.shift(1.5*LEFT+1.75*UP)
        points[1].next_to(rectangles[1],UP)
        points[2].next_to(rectangles[2],UP)
        points[3].next_to(rectangles[2],DOWN)

        potentials[0].next_to(points[0],RIGHT)
        potentials[1].next_to(points[1],RIGHT)
        potentials[2].next_to(points[2],RIGHT)
        potentials[3].next_to(points[3],RIGHT)
        
        potential_plus=Typst(rf"$phi_+=24V$",font_size=35)
        potential_minus=Typst(rf"$phi_-=0V$",font_size=35)
        potential_minus.next_to(minus,DOWN)
        potential_plus.next_to(plus,UP)
        explanation=Typst('$ "Höhe" h  hat(=) "Potenzial" phi$').to_corner(UR)
        explanation2=Typst("$[phi] = 1V$").next_to(explanation,DOWN)
        explanation3=Typst("$Delta phi = U$").next_to(explanation2,DOWN)
        
        electron=Dot(4.5*LEFT+1.5*UP,0.2,color=BLUE).set_z_index(2)
        arrow=DoubleArrow(UP*1.5+LEFT*0.5,DOWN*1.5+LEFT*0.5,color=PURPLE,buff=0)
        dashline=DashedLine(LEFT*0.5+DOWN*1.5,RIGHT*4.5+DOWN*1.5)
        dashline2=DashedLine(LEFT*1.5+1.5*UP,LEFT*0.5+1.5*UP)
        calculation=Typst('$U_"AC"= Delta phi =phi_A-phi_C=24V-8V=16V$',color=PURPLE,font_size=40).to_corner(UL)
        direction=Arrow(LEFT*0.75+0.25*UP,RIGHT*0.75+0.25*UP,color=BLUE)
        arrow_explanation=Typst("$Delta phi$",color=PURPLE,font_size=35).shift(UP*0.5)
        explanation4=Typst("Stromrichtung",font_size=30,color=BLUE).next_to(direction,UP)

        
        self.add(
            line,
            rectangles,
            texts,
            minus,
            plus,
            power,
            plus_sign,
            minus_sign,
            netzgeraet,
            points
            
        )
        self.play(
            Write(title),
            
            run_time=2
            )

        self.play(
            Write(explanation),
            run_time=3
            
        )
        self.play(
            Write(explanation2),
            run_time=3
        )
        self.play(
            Write(potential_plus),
            Write(potential_minus),
            run_time=4
        )
        self.play(
            
            Write(potentials),
            run_time=5
        )
        
        
        self.play(
            FadeOut(title),
            Write(explanation3),
            run_time=3
        )
        self.play(
            Create(dashline),
            Create(dashline2),
            Create(arrow),
            Write(arrow_explanation),
            run_time=3

        )
        self.play(
            Write(calculation),
            run_time=5
        )
        self.play(
            FadeOut(dashline,dashline2,arrow,arrow_explanation),
            Create(direction),
            Write(explanation4)
        )
        self.add(electron)
        self.play(MoveAlongPath(electron,line,rate_func=linear),run_time=5)

        
        
        