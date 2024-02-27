from PIL import Image
import os
import argparse

def compress_and_replace(input_folder, output_folder, target_quality=85):
    for root, dirs, files in os.walk(input_folder):
        print(files)
        for file in files:
            print(file)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_folder, file)

                # Compress the image
                compress_image(input_path, output_path, target_quality)

def compress_image(input_path, output_path, target_quality):
    with Image.open(input_path) as img:
        # Save the image with the specified compression quality
        img.save(output_path, quality=target_quality)

def main():
    parser = argparse.ArgumentParser(description='Compress images in a specified folder.')
    parser.add_argument('input_folder', help='Path to the input folder containing images.')
    parser.add_argument('output_folder', help='Path to the output folder for compressed images.')
    parser.add_argument('--quality', type=int, default=70, help='Compression quality (0 to 100).')

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder
    target_quality = args.quality

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    compress_and_replace(input_folder, output_folder, target_quality)

if __name__ == "__main__":
    main()
