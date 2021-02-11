import cv2
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]
image = cv2.imread(input_path)
transpose_image = cv2.transpose(image)
cv2.imwrite(output_path, transpose_image)
