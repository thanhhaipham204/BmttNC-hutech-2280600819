import sys
from PIL import Image

def decode_image(encoded_image_path):
    try:
        img = Image.open(encoded_image_path).convert("RGB")
    except Exception as e:
        print(f"Error opening image: {e}")
        return ""

    width, height = img.size
    binary_message = ""

    # Trích xuất bit cuối từ mỗi kênh màu của từng pixel
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):  # R, G, B
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Chuyển đổi chuỗi nhị phân thành thông điệp
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\0':  # Kết thúc thông điệp khi gặp dấu '\0'
            break
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    if decoded_message:
        print("Decoded message:", decoded_message)
    else:
        print("No message found or failed to decode.")

if __name__ == "__main__":
    main()