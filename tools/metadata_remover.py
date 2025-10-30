from PIL import Image
import os

def remove_metadata(image_path):
    try:
        image = Image.open(image_path)
        data = list(image.getdata())
        clean_image = Image.new(image.mode, image.size)
        clean_image.putdata(data)
        clean_image.save("cleaned_" + os.path.basename(image_path))
        print(f"Metadata removed: cleaned_{os.path.basename(image_path)} created.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    path = input("Enter image path: ").strip()
    remove_metadata(path)
