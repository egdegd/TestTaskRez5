import cv2
import sys
import numpy as np


input_path = sys.argv[1]
image = cv2.imread(input_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h, w, p = image_rgb.shape
reshape_image = image_rgb.reshape(h * w, p)
color, counts = np.unique(reshape_image, return_counts=True, axis=0)

zip_list = list(zip(counts, color))
list_with_count = list(map(lambda pair: list(np.concatenate(([pair[0]], pair[1]))), zip_list))

sorted_list = sorted(list_with_count, reverse=True)
for color in sorted_list:
    print(f'{color[1]}, {color[2]}, {color[3]}: {color[0]}')
