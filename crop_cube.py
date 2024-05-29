from PIL import Image
import os

# Define the input and output directories
input_dir = 'blur-input'
output_dir = 'output'

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

        # Now crop the middle 800x800 pixels
        final_side = 800
        left = (new_side - final_side) // 2
        top = (new_side - final_side) // 2
        right = (new_side + final_side) // 2
        bottom = (new_side + final_side) // 2

        # Ensure the image is at least 800x800 before cropping
        if new_side >= final_side:
            img = img.crop((left, top, right, bottom))
        else:
            print(f"Image {filename} is smaller than 800x800 and cannot be cropped further.")

        # Save the cropped image to the output directory
        output_path = os.path.join(output_dir, filename)
        img.save(output_path)

print("Processing complete.")
