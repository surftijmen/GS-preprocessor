from PIL import Image
import os

# Define the input and output directories
input_dir = 'chair'
output_dir = 'chair1'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each PNG file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        image_path = os.path.join(input_dir, filename)
        img = Image.open(image_path)

        # Get image dimensions
        width, height = img.size
        new_side = min(width, height)

        # Calculate cropping coordinates to make the image square
        left = (width - new_side) // 2
        top = (height - new_side) // 2
        right = (width + new_side) // 2
        bottom = (height + new_side) // 2

        # Crop the image to a square
        img = img.crop((left, top, right, bottom))

        # Remove 10% from the right and 10% from the bottom
        remove_percentage = 0.10
        new_width = int(img.width * (1 - remove_percentage))
        new_height = int(img.height * (1 - remove_percentage))

        # Ensure the new dimensions are the same to keep it square
        new_side = min(new_width, new_height)

        # Calculate new cropping coordinates
        left = 0
        top = 0
        right = left + new_side
        bottom = top + new_side

        # Crop the image again to get the final result
        img = img.crop((left, top, right, bottom))

        # Save the cropped image to the output directory
        output_path = os.path.join(output_dir, filename)
        img.save(output_path)

print("Processing complete.")
