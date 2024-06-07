from PIL import Image
import numpy as np

def encryptImage(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")
    data = np.array(img)
    # Adding key value to each pixel for encryption
    encrypted_data = (data + key) % 256
    # Convert array back into image
    encrypted_img = Image.fromarray(np.uint8(encrypted_data))
    encrypted_img.save("Encrypted_image.png")
    print("Image encrypted and saved as Encrypted_image.png")

def decryptImage(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    img = img.convert("RGB")
    data = np.array(img)
    # Reverse encryption operation
    decrypt_data = (data - key) % 256
    decrypt_img = Image.fromarray(np.uint8(decrypt_data))
    decrypt_img.save("Decrypted_image.png")
    print("Image decrypted and saved as Decrypted_image.png")

def main():
    image_path = r"C:\Users\IMxGIRISH\OneDrive\Desktop\CS_Internship\fruits.png"
    key = 50

    encryptImage(image_path, key)
    decryptImage("Encrypted_image.png", key)

if __name__ == "__main__":
    main()
