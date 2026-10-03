from manim import *
import math
class Mesopotamia(Scene):
    def construct(self):
        img = ImageMobject(r"C:\Users\juliu\Downloads\YBC-7289-OBV-REV.jpg")
        img.width = 10  # or img.height = 3, etc.
        img.shift(RIGHT*0.2+UP*0.5)
        #img.rotate(math.radians(-1.5))
        points=[
            3.4*UP,
            3.4*RIGHT,
            3.4*DOWN,
            3.4*LEFT,
            3.4*UP
        ]
        numbers1=Typst("30",font_size=70).rotate(math.radians(45)).shift(2.1*UP+2.6*LEFT)
        numbers2=VGroup(
            Typst("1;",font_size=70).shift(LEFT*1.8),
            Typst("24,",font_size=70).shift(LEFT*0.9),
            Typst("51,",font_size=70).shift(RIGHT*0.8),
            Typst("10",font_size=70).shift(RIGHT*1.7)
            ).rotate(math.radians(5))
        numbers3=VGroup(
            Typst("42;",font_size=70).shift(LEFT*0.9),
            Typst("25, ",font_size=70).shift(RIGHT*0.8),
            Typst("35",font_size=70).shift(RIGHT*2)
        ).rotate(math.radians(15)).shift(DOWN*1.1)
        line=VMobject(stroke_width=5)
        line.set_points_as_corners(points)
        diagonal1=Line(3.4*DOWN,3.4*UP,stroke_width=5)
        diagonal2=Line(3.4*LEFT,3.4*RIGHT,stroke_width=5)
        new_numbers1=Typst("30",font_size=60).rotate(math.radians(45)).shift(1.6*UP+2.2*LEFT)
        new_numbers2=Typst("1,4142129",font_size=60).rotate(math.radians(5))
        new_numbers3=Typst("42,426",font_size=60).rotate(math.radians(15)).shift(DOWN*1.1)
        kathete1=Typst("s",font_size=60).shift(1.6*UP+2.2*LEFT)
        kathete2=Typst("s",font_size=60).shift(1.6*DOWN+2.2*LEFT)
        hypotenuse=Typst("d",font_size=60).shift(0.2*RIGHT)
        arc=Arc(radius=0.8,start_angle=math.radians(-45),angle=math.radians(90)).shift(3.4*LEFT)
        point=Dot(3*LEFT,0.04)
        
        picture=VGroup(
            line,
            diagonal1,
            diagonal2,
            numbers1,
            numbers2,
            numbers3,
            new_numbers2,
            new_numbers1,
            new_numbers3,
            kathete1,
            kathete2,
            hypotenuse,
            arc,
            point
            
            
        )
        self.add(
            img,
            line,
            diagonal1,
            diagonal2,
            numbers1,
            numbers2,
            numbers3
            )
        picture.shift(RIGHT*3)
        calculation1=[]
        calculation1.append(Typst("$30$",font_size=40).to_corner(UL))
        calculation1.append(Typst("$=30 * 60^0$",font_size=40).next_to(calculation1[0],RIGHT))
        calculation1.append(Typst("$=30$",font_size=40).next_to(calculation1[1],RIGHT))
        calculation2=[]
        calculation2.append(Typst("$1;24,51,10$",font_size=40).to_corner(UL).align_to(calculation1[0],LEFT))
        calculation2.append(Typst("$= 1*60^0 + 24/(60^1) + 51/(60^2) + 10/(60^3)$",font_size=33).next_to(calculation2[0],DOWN).align_to(calculation1[0],LEFT))
        calculation2.append(Typst("$= 1,4142129$",font_size=40).next_to(calculation2[1],DOWN).align_to(calculation1[0],LEFT))
        calculation3=[]
        calculation3.append(Typst("$42;25,35$",font_size=40).to_corner(UL).align_to(calculation1[0],LEFT))
        calculation3.append(Typst("$= 42*60^0 + 24/(60^1) + 35/(60^2)$",font_size=37).next_to(calculation2[0],DOWN).align_to(calculation1[0],LEFT))
        calculation3.append(Typst("$= 42,426$",font_size=40).next_to(calculation2[1],DOWN).align_to(calculation1[0],LEFT))
        
        # self.add(
        #     calculation1[0],
        #     calculation1[1],
        #     calculation1[2],
        #     # calculation2[0],
        #     # calculation2[1],
        #     # calculation2[2],
        #     calculation3[0],
        #     calculation3[1],
        #     calculation3[2]
        #     )
        self.play(FadeOut(img))
        self.play(Transform(numbers1,calculation1[0]))
        self.play(Create(calculation1[1]))
        self.play(Create(calculation1[2]))
        self.play(ReplacementTransform(calculation1[2],new_numbers1))
        self.play(FadeOut(numbers1,calculation1[1]))

        self.play(Transform(numbers2,calculation2[0]))
        self.play(Create(calculation2[1]))
        self.play(Create(calculation2[2]))
        self.play(ReplacementTransform(calculation2[2],new_numbers2))
        self.play(FadeOut(numbers2,calculation2[1]))

        self.play(Transform(numbers3,calculation3[0]))
        self.play(Create(calculation3[1]))
        self.play(Create(calculation3[2]))
        self.play(ReplacementTransform(calculation3[2],new_numbers3))
        self.play(FadeOut(numbers3,calculation3[1]))

        
        self.play(
            new_numbers1.set_opacity(0.15).animate(),
            new_numbers2.set_opacity(0.15).animate(),
            new_numbers3.set_opacity(0.15).animate(),
            FadeOut(diagonal2)
        )
        
        
                    
        
        self.play(
            Create(kathete1),
            Create(kathete2),
            Create(hypotenuse),
            Create(arc),
            Create(point)
        )
        self.wait(3)
        # self.play(
        #     FadeOut(img),
        #     FadeIn(
        #         line,
        #         diagonal1,
        #         diagonal2
        #     ),
        #     run_time=5
        # )