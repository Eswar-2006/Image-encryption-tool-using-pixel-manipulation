from PIL import Image

def swap_pixels(img):
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width // 2):
            # Swap pixel (x, y) with pixel (width - 1 - x, y)
            opposite_x = width - 1 - x
            pixels[x, y], pixels[opposite_x, y] = pixels[opposite_x, y], pixels[x, y]
    return img

def shift_pixels(img, shift):
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Shift each color channel and wrap around 256
            r = (r + shift) % 256
            g = (g + shift) % 256
            b = (b + shift) % 256
            pixels[x, y] = (r, g, b)
    return img

def main():
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    operation = input("Choose operation - swap or shift: ").strip().lower()

    img = Image.open(input_path).convert('RGB')

    if operation == 'swap':
        img = swap_pixels(img)
    elif operation == 'shift':
        while True:
            try:
                shift = int(input("Enter shift value (integer 0-255): "))
                if 0 <= shift <= 255:
                    break
                else:
                    print("Shift must be between 0 and 255.")
            except ValueError:
                print("Please enter a valid integer.")
        img = shift_pixels(img, shift)
    else:
        print("Invalid operation selected.")
        return

    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    main()