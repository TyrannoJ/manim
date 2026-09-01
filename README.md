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

### in the picture version 
- blue line: main function 
- blue dots: zeros of the main function 
- green line: the first derivative function 
- green dots: extremes of the main function
- red line: second derivative function 
- red dots: turning points of the main function
- purple is where the main function is curved to the left
- yellow is where the main function is curved to the right

### in the animation

- First it animates the main function and it's zeros in blue
- then the first derivative function and it's zeros in green
- then the second derivative function and it's zeros in red
- Afterwards it shows you the extremes in Blue
- And then the turns in Blue and the curvature of the function purple=left yellow=right

## How can you do it yourself 

- for it to work you have to install a latex engine, for example MiKteX from [here](https://miktex.org/download)
- You can simply install pipx and run this command: pipx install "git+https://github.com/TyrannoJ/manim#subdirectory=python_project" 
- Then you can run render-picture for an image and render-animation for a video.
- to Input your function you just type it in the command prompt 
- Input style for functions: *coefficient*x*power*+*next-coefficien*x*next-power*...
- **A few examples:**
1. 2x3 
2. x3-4x2
3. 4.3x4+x
4. -2.5x6-x2+3

## How did I build it
I used *manim* to animate and *sympy* for the zero points, so a big thanks to Grant SAnderson from 3blue1brown. I used perplexity and a little GitHub Copilot for research especially for specific manim functions and to write a few little functionalities with syntaxes I didn't know but never more than 2-3 lines and a lot of help on the package structure. I also used it to understand the errors that were output.
This is my first manim project and I'm quite happy with how it turned out and I plan to do more.



## to Do (for future reference)
- maybe make interactive
- make input more user friendly
- make handle of constants better
- typst color work
- test typst install
- typst in animation


