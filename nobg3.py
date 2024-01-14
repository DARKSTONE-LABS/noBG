from PIL import Image
import os

def make_background_transparent(image_path, output_folder, sample_size=25):
    image = Image.open(image_path)
    image = image.convert("RGBA")  # Convert to RGBA if necessary
    datas = image.getdata()

    newData = []
    sample = datas[-1]  # Top right pixel color

    for item in datas:
        # Check if the current pixel matches the sample color within the specified sample_size
        if all(abs(item[i] - sample[i]) < sample_size for i in range(3)):
            newData.append((255, 255, 255, 0))  # Fully transparent
        else:
            newData.append(item)

    image.putdata(newData)
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    image.save(output_path, "PNG")

def process_folder(input_folder):
    output_folder = 'SAGAMONKESNOBG'
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.png'):
            image_path = os.path.join(input_folder, file_name)
            make_background_transparent(image_path, output_folder)

input_folder = 'SAGA MONKES'  # Replace with the path to your folder
process_folder(input_folder)
