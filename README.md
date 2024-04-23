This was a simple tool developed for the University of Manchester VLSI Design Art Competition Coursework.

The idea is simple, using the command line interface of L-Edit we can draw 'pixels' using the Tcl command
```
rect -layer {layer} -llx {lower left x} - lly {lower left y} -urx {upper right x} - ury {upper right y}
```

Therefore, if we create a script that can take in an image, rasterize in terms of the colours that are available according to the different layers of L-Edit, then we are in business. This script generates those Tcl scripts containing everything.

# To use

After cloning into a directory:

```
pip install -r requirements.txt
python main.py
```

The program will ask for an image file path **relative to the directory that main.py** is in.

Then, the script will show a preview of the image, for which it is possible to adjust the brightness / contrast of - although this has to be changed by editing the 'brightness' and 'contrast' variables in the script.

Then the script will rasterise the image according to the 'output_size' and w,h variables.

Output_size determines the size of the output image, and w,h determines how many 'pixels' are used for the drawing. 

Finally, the script will ask for an output file name of the generated Tcl script. This will generate in the same directory that main.py is in.

To run this Tcl file in l-edit:

```
$source [path/to/tcl/file]
```