# Mandala Art

This repository uses Python turtle to generate beautiful and intricate Mandalas. Some examples can be seen in Images/. To generate your own mandalas please clone this repository to your working directory. 

Requirements:
* turtle
* numpy
* math
* random
* colorsys

To install turtle:
       pip install turtle

To import the mandala package use:
       
       from mandala_art import mandala

There are three ways to generate mandalas:

1. generate(color_scheme = 'colorful', bgcolor = 'black',<br>
             screensize = 550, fcolor = bright_color_gen(),<br>
             color1 = bright_color_gen(), color2 = bright_color_gen(),<br>
             animate = True)<br>
This generates a single Mandala.
             
* color_scheme: This can take values 'colorful', 'b&w', 'sepia', 'monochrome' and 'bicolor'. Capitalised keywords are also allowed.
* bgcolor: This is the background color of the canvas. It can take keywords 'black', 'red', 'blue' and 'green', or a tuple of (r,g,b) values.  Capitalised keywords are also allowed.
* screensize: This is the size of screen which is is square in shape.
* fcolor: This works with monochrome, specifies the color of the mandala. Must be a tuple of (r,g,b) values.
* color1: This works with bicolor. Specifies one of the colors of the mandala. Must be a tuple of (r,g,b) values.
* color2: This works with bicolor. Specifies the second color of the mandala. Must be a tuple of (r,g,b) values.
* animate: If set to True this shows the animation for drawing the mandala. If set to False only in image is shown on the screen without animation.

Usage:

       mandala.generate()


2. multiple(num_mandalas=10, screensize = 550)<br>
This generates mandalas one after the other and is always animated.

* num_mandalas: The number of Mandalas to be generated. Must be an integer.
* screensize: This is the size of screen which is is square in shape.
             
             
Usage:

       mandala.multiple()
              
              
3. custom(l1, color11, color12, l2, color21, color22,<br>
           l3, color31, color32, l4, color41, color42,<br>
           bgcolor=(0,0,0), screensize = 550, animate = True)<br>
           
 This generates a custom Mandala. To see different layer options refer to the folder Layer_Images/
           
* l{i}: This is the choice of the i-th layer. Takes values from 1-4, 1-2, 1-3 and 1-2 for layers 1 to 4 respectively.
* color1{i}: This is the first color of the i-th layer. Must be a tuple of (r,g,b) values.
* color2{i}: This is the first color of the i-th layer. Must be a tuple of (r,g,b) values.
* bgcolor: This is the background color of the canvas. It takes a tuple of (r,g,b) values.
* screensize: This is the size of screen which is is square in shape.
* animate: If set to True this shows the animation for drawing the mandala. If set to False only in image is shown on the screen without animation.

Usage:

       mandala.custom(l1, color11, color12, l2, color21, color22,
                      l3, color31, color32, l4, color41, color42)
