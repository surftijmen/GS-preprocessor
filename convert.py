import numpy as np
from PIL import Image

# Step 1: Load your PNG image
image_path = 'blur-input/normal.png'
img = Image.open(image_path)

# Step 2: Crop the image to the largest possible square
width, height = img.size
new_side = min(width, height)

left = (width - new_side) // 2
top = (height - new_side) // 2
right = (width + new_side) // 2
bottom = (height + new_side) // 2

img = img.crop((left, top, right, bottom))

# Step 3: Convert the image to a NumPy array
# If you need a grayscale image, convert it first: img = img.convert('L')
data = np.array(img)

# Step 4: Save the NumPy array to a file
npy_path = 'image.npy'
np.save(npy_path, data)
