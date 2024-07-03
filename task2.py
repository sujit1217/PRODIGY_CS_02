from PIL import Image
from tkinter import Tk, filedialog, Button, Label
import os
import random

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    random.seed(key)
    random.shuffle(pixels)
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(pixels)
    encrypted_image_path = os.path.join(script_dir, "encrypted_image.png")
    encrypted_image.save(encrypted_image_path)
    return encrypted_image_path

def decrypt_image(image_path, key):
    encrypted_image = Image.open(image_path)
    pixels = list(encrypted_image.getdata())
    random.seed(key)
    index_order = list(range(len(pixels)))
    random.shuffle(index_order)
    original_pixels = [None] * len(pixels)
    for i, index in enumerate(index_order):
        original_pixels[index] = pixels[i]
    decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
    decrypted_image.putdata(original_pixels)
    decrypted_image_path = os.path.join(script_dir, "decrypted_image.png")
    decrypted_image.save(decrypted_image_path)
    return decrypted_image_path

def encrypt_action():
    file_path = filedialog.askopenfilename()
    if file_path:
        encrypted_image_path = encrypt_image(file_path, 1234)
        Label(root, text=f"Image encrypted and saved as {encrypted_image_path}").pack()

def decrypt_action():
    file_path = filedialog.askopenfilename()
    if file_path:
        decrypted_image_path = decrypt_image(file_path, 1234)
        Label(root, text=f"Image decrypted and saved as {decrypted_image_path}").pack()

root = Tk()
root.title("Image Encryption Tool")

Label(root, text="Select an image to encrypt or decrypt:").pack()

Button(root, text="Encrypt Image", command=encrypt_action).pack()
Button(root, text="Decrypt Image", command=decrypt_action).pack()

root.mainloop()
