from PIL import Image
import numpy as np

# Load images
originalImage = Image.open("color-input/original.png")
recolouredImage = Image.open("color-input/color.png")

# Ensure both images are in RGB mode
originalImage = originalImage.convert("RGB")
recolouredImage = recolouredImage.convert("RGB")

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
path = "output/outputColor.png"
outputImage.save(path)