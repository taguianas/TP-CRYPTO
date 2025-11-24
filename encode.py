from PIL import Image

input_path = r"C:\Users\manag\Desktop\cloud-security-201908120550101.jpg"
output_path = r"C:\Users\manag\Desktop\cloud-security-encoded.png"
message = "Winter is coming and the night is full of fears"

def encode_message(input_image_path, output_image_path, message):
    img = Image.open(input_image_path)
    img = img.convert("RGB")
    pixels = img.load()
    width, height = img.size

    bitstream = ""
    for char in message:
        bitstream += format(ord(char), "08b")
    bitstream += "00000000"  # terminator

    capacity = width * height * 3
    if len(bitstream) > capacity:
        raise ValueError("Message too long for this image.")

    idx = 0
    for y in range(height):
        for x in range(width):
            if idx >= len(bitstream):
                break

            r, g, b = pixels[x, y]

            if idx < len(bitstream):
                r = (r & ~1) | int(bitstream[idx])
                idx += 1
            if idx < len(bitstream):
                g = (g & ~1) | int(bitstream[idx])
                idx += 1
            if idx < len(bitstream):
                b = (b & ~1) | int(bitstream[idx])
                idx += 1

            pixels[x, y] = (r, g, b)
        if idx >= len(bitstream):
            break

    img.save(output_image_path)
encode_message(input_path, output_path, message)
output_path
