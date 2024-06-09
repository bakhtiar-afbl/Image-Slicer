from PIL import Image
import os

def slice_image(image_path, output_dir):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Calculate the middle point
    middle = width // 2

    # Slice the image into two parts
    left_img = img.crop((0, 0, middle, height))
    right_img = img.crop((middle, 0, width, height))

    # Get the base name of the original image file
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)

    # Save the left part
    left_img_path = os.path.join(output_dir, f"{name}_left{ext}")
    left_img.save(left_img_path)

    # Save the right part
    right_img_path = os.path.join(output_dir, f"{name}_right{ext}")
    right_img.save(right_img_path)

    print(f"Saved {left_img_path} and {right_img_path}")

def process_directory(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        # Construct full file path
        file_path = os.path.join(input_dir, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Slice the image and save the parts
            slice_image(file_path, output_dir)

# Example usage
input_directory = "C:\\Users\\ABC\\Desktop\\ClubData\\Gulshan Club\\Original\\1"
output_directory = "C:\\Users\\ABC\\Desktop\\ClubData\\Gulshan Club\\Original\\1\\new"
process_directory(input_directory, output_directory)
