import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def main():
    path = input("Enter the path to the image file: \n")
    try:
        image = PIL.Image.open(path)
    except FileNotFoundError:
        print("Unable to find image at:", path)
        return
   
    image = resize(image)
    greyscale_image = to_greyscale(image)
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    # Split the string based on width of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    # Save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

def resize(image, new_width=100):
    old_width, old_height = image.size
    new_height = int(new_width * old_height / old_width)
    return image.resize((new_width, new_height))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        # Normalize pixel intensity to the range [0, 255]
        normalized_intensity = pixel / 255.0
        # Map normalized intensity to the range [0, len(ASCII_CHARS)-1]
        index = int(normalized_intensity * (len(ASCII_CHARS) - 1))
        ascii_str += ASCII_CHARS[index]
    return ascii_str


if __name__ == '__main__':
    main()
