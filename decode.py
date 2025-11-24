from PIL import Image

def decode_message(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()
    width, height = img.size

    bits = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bits += str(r & 1)
            bits += str(g & 1)
            bits += str(b & 1)
    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if byte == "00000000":   # fin du message
            break
        message += chr(int(byte, 2))

    return message
encoded_image = encoded_image = r"C:\Users\manag\Desktop\cloud-security-encoded.png"

msg = decode_message(encoded_image)
print("Message décodé :", msg)

