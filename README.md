# This is a Python Derivative plotter made with manim

## What does it do?

There are two main codes here.
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

## How can you do it yourself 
You can simply install pipx and run this command 
pipx install "git+https://github.com/TyrannoJ/manim#subdirectory=python_project" .
Then you can run render-picture for an image and render-animation for a video.
To Input your function you just type it in this style *coefficient*x*power*+*next-coefficien*x*next-power*...

## How did I build it
I used *manim* to animate and *sympy* for the zero points. I used perplexity and a little GitHub Copilot for research especially for specific manim functions and to write a few little functionalities with syntaxes I didn't know but never more than 2-3 lines and a lot of help on the package structure. I also used it to understand the errors that were output.
This is my first manim project and I'm quite happy with how it turned out and I plan to do more.



## to Do (for future reference)
- maybe make interactive
- make input more user friendly
- accept \- signs for separation
- accept x0 and x1 156m78
- make handle of constants better
- better coeficients

