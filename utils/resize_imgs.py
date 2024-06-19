import os
from PIL import Image

# Path to the folder containing images
input_folder = 'images/chess'
output_folder = 'images/chess_resized'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Desired size
new_size = (640, 480)

# Process each image in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            # Resize the image
            img_resized = img.resize(new_size, Image.LANCZOS)
            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)
        print(f'Resized and saved {filename} to {output_folder}')

print('All images have been resized.')
