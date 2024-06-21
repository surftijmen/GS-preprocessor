from PIL import Image
import numpy as np

# Load images
originalImage = Image.open("chair/000.png")
recolouredImage = Image.open("chair/051.png")

# Ensure both images are in RGB mode
originalImage = originalImage.convert("RGBA")         
recolouredImage = recolouredImage.convert("RGBA")

# Get numpy arrays
arrayOriginal = np.array(originalImage)
arrayRecoloured = np.array(recolouredImage)

# Calculate the mean color values of the left image
meanOriginal = np.mean(arrayOriginal, axis=(0, 1))

# Apply the color tint of the left image to the right image
arrayOutput = arrayRecoloured * meanOriginal / np.mean(arrayRecoloured, axis=(0, 1))

# Clip values to valid range and convert to uint8
arrayOutput = np.clip(arrayOutput, 0, 255).astype(np.uint8)

# Convert array back to image
outputImage = Image.fromarray(arrayOutput)

# Save and show the tinted image
path = "output/chair.png"
outputImage.save(path)