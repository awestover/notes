
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("cat.jpg")
data = np.array(img)

print(data.shape)

def find_closest_palette_color(oldpixel):
    multiplier = 64
    return np.round(oldpixel/multiplier) * multiplier

for y in range(data.shape[0]):
    for x in range(data.shape[1]):
        oldpixel = data[y, x,:]
        newpixel = find_closest_palette_color(oldpixel)
        data[y,x,:] = newpixel
        quantization_error = oldpixel - newpixel
            
        if y < data.shape[0]-1 and 0 < x < data.shape[1]-1:
            # spread out the quantization error below and to the right
            data[y, x + 1,:]     = data[y, x + 1,:]     + quantization_error * 7 / 16
            data[y + 1, x - 1,:] = data[y + 1, x - 1,:] + quantization_error * 3 / 16
            data[y + 1, x,:]     = data[y + 1, x,:]     + quantization_error * 5 / 16
            data[y + 1, x + 1,:] = data[y + 1, x + 1,:] + quantization_error * 1 / 16

plt.imshow(data)
plt.show()

