# This is a Python Derivative plotter made with manim

## What does it do?

There are two main code here.
- useful_derivatives.py
- derivatives_simple.py

With both you can basically do the same
1. Give it a simple polynomial function as a String like "2x4+3x2"
2. It calculates the first and second derivatives of the function
3. It plots all of them
4. It shows you all their zero points
5. It shows you the Extremes and Turning points of the function

The only difference between the two is, that the simple version only shows all that to you while the other one animates it 
[look at the program outputs here](https://tyrannoj.github.io/manim/index.html)

## What do the results mean:
it's pretty self explanatory:
- blue is the main function and it's zeros
- green is the first derivative and it's zeros and in simple mode the extremes
- red is the second derivative and it's zeros and in simple mode the turns
- purple is where the main function is curved to the left
- yellow is where the main function is curved to the right

## How did I build it
I used *manim* to animate any *sympy* for the zero points
This is my first manim project and I'm quite happy with how it turned out



## to Do (for future reference)
- maybe make interactive
- make input more user friendly
