# waveshare-create-font
Create proportional fonts for Waveshare E-Paper displays for use with C/C++ applications

Waveshare provides a good sample application in Python to create any size proportional fonts but the sample application for C/C++ has very limited fonts in bitmap files that are non-proportional. This repository includes a Python program to create any size proportional font files that can be read and displayed in a C/C++ application.

For each font size a set of two files is created using two Python programs. One file has the bitmap information for each character and the other contains the width of each proportionally spaced character. So when characters are displayed the C/C++ program reads offsets into each file for the character being displayed and draws them on the e-paper display. The Python program uses the PIL library and freefont files to generate the character bitmaps and widths. 

The Python programs print the text information contained in the font files to the command line so output can be piped to the appropriate output file. This repository contains the proportional font files for 18, 24, 32 and 64 point sizes.
