import cv2 as cv
import numpy as np

# in BGR
COLOUR_POLY = [0,0,255]
COLOUR_METAL1 = [255, 0, 0]
COLOUR_METAL2 = [0, 255, 0]
COLOUR_METAL3 = [0, 255, 255]
COLOUR_METAL4 = [119,0, 179]
COLOUR_VIA1 = [255, 51, 255]
COLOUR_VIA2 = [255, 255, 77]
COLOUR_VIA3 = [0, 128, 255]
COLOUR_POLY2 = [34, 0, 51]
CONTACT = [0, 230, 230]

colour_list = [COLOUR_POLY, COLOUR_METAL1, COLOUR_METAL2, COLOUR_METAL3, COLOUR_METAL4, COLOUR_VIA1, COLOUR_VIA2, COLOUR_VIA3, COLOUR_POLY2, CONTACT]

layer_names = ["Poly", "Metal1", "Metal2", "Metal3", "Metal4", "Via1", "Via2", "Via3", "Poly2", "Contact"]

def closest(color):
    colors = np.array(colour_list)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    layer_name = layer_names[int(index_of_smallest[0].tolist()[0])]
    return (smallest_distance, layer_name)
        
output_size = (300, 250)

name = input("Enter the name of the input image file: ")

image = cv.imread(f"inputs/{name}")
w, h = (125, 100)

brightness = 2.8
contrast = 20

image2 = cv.convertScaleAbs(image, alpha=brightness, beta=contrast) 

temp = cv.resize(image2, (w, h), interpolation=cv.INTER_LINEAR)
output = cv.resize(temp, output_size, interpolation=cv.INTER_NEAREST)

cv.imshow("Image", output)

cv.waitKey(0)

array = []

output_image = np.zeros((output_size[1], output_size[0], 3), dtype=np.uint8)

output_str = ""

for i in range(h):
    for j in range(w):
        try:
            startY=int(i*output_size[1]/h)
            endY=int((i+1)*output_size[1]/h)
            startX = int(j*output_size[0]/w)
            endX = int((j+1)*output_size[0]/w)
            
            image = output[startY:endY, startX:endX]
            avg_color_per_row = np.average(image, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            closest_col = list((closest(avg_color)))
            closest_col_val = [int(i) for i in closest_col[0][0]]
            closest_col_layer = (closest_col[1])
            cv.rectangle(output_image, (startX, startY), (endX, endY), tuple(closest_col_val), -1) 

            output_str += f"rect -layer {closest_col_layer} -llx {startX} -lly -{startY} -urx {endX} -ury -{endY};"
        except:
            pass
        
    
cv.imshow("Processed", output_image)
cv.waitKey(0)

output = input("Output file name: ")
with open (f'outputs/{output}.tcl', 'w') as f:
    f.write(output_str)

print("Outputted")