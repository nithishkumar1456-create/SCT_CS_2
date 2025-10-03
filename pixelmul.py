from PIL import Image

def encrypt_image(input_path, output_path):
    
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel
            

    img.save(output_path)
    print(f"✅ Encrypted image saved as {output_path}'")


def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel
          

    img.save(output_path)
    print(f"✅ Decrypted image saved as {output_path}")

choice = input("Do you want to Encrypt or Decrypt? (e/d): ").lower()
in_file = input("Enter input image filename: ")
out_file = input("Enter output image filename: ")

if choice == "e":
    encrypt_image(in_file, out_file)
elif choice == "d":
    decrypt_image(in_file, out_file)
else:
    print("❌ Invalid choice! Use 'e' for encrypt or 'd' for decrypt.")
