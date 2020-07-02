# Digit-Recognition

Please download the following MNIST dataset from http://yann.lecun.com/exdb/mnist/
It will be used throughout.

Idea # 1 

After finding the exact structure the sample datasets come in, try to normalize the samples into a 
datatype like a 25 by 25 matrix where each entry is a gray-scale 0 to 1 value of the color of the pixel 
in that slot.  

From this a testing process of an unknown input would simply be finding a probability amplitude, i.e. 
making use of a dot product between input and test sample to see if there is large agreement in pixel 
pigments.  The higher the value, the higher the likelihood the digit is the equal to the sample.  

Now for me to learn about specific learning methods.  

Possible issue: Not everyone's zero will be centered about the same point.  Hopefully this will be handled 
by a large sample base of varied versions of each digit.  Otherwise, need to create some method to 'center'
or 'scale' each input digit before starting. Don't know how easy or possible this is.  

Idea #2 

Create a way of counting crossings.  In a particular raw input, first find which pixels have a gray scale color 
significantly close to 1 (i.e. where the penstroke falls).  Then at each of these 'dark' pixels, look at all neighbor pixels 
(8 for minimal case, 24 for next, etc.) and then either test these 'zoomed' in pictures against some set of test crossings.
Or set a threshold for right/left/up/down neighbors being above a certain gray scale and the diagonal neighbors below some threshold
to 'count' that the curve crossed itself.  

Between number of crossings and position of crossings, a decent guess of digit could be formed.  

Possible issues: Computational complexity.  If there is not a way to normalize the curve width to a pixel, then 
the fact that the curve will bleed over many pixels would require many of these neighbor computations.  Even in the minimal
case of checking 8 nearby pixels, it could easily exceed 25^2 computations of idea 1 (or whatever the array size of the input data size).  
