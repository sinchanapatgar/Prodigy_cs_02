🖼️ PRODIGY_CS_02 – Pixel Manipulation for Image Encryption
Prodigy Infotech Cybersecurity Internship – Task 02
📌 Overview
A Python GUI application that encrypts and decrypts images using pixel-level XOR manipulation. Each pixel's RGB values are XORed with a secret key, making the image unreadable without the correct key.
🖥️ Features
🔒 Encrypt any image (PNG, JPG, BMP, GIF)
🔓 Decrypt encrypted images using the same key
XOR key selection from 0 to 255
Live image preview before and after processing
Saves output image automatically to disk
Dark-themed GUI built with Tkinter
🧠 How It Works
For every pixel in the image, each RGB channel is XORed with the key:
Encrypted_pixel = Original_pixel XOR Key
Decrypted_pixel = Encrypted_pixel XOR Key  (XOR is its own inverse)
Example with key = 42:
Original pixel:   (120, 200, 55)
Encrypted pixel:  (120^42, 200^42, 55^42) = (82, 234, 29)
Decrypted pixel:  (82^42, 234^42, 29^42)  = (120, 200, 55) ✅
🚀 How to Run
Prerequisites
Python 3.8+
Install Pillow:
pip install Pillow
Run the Program
python PRODIGY_CS_02.py
🖼️ Usage
Click Browse Image to select an image file
Set the XOR Key (0–255) — remember this to decrypt later!
Click ENCRYPT IMAGE to encrypt
To decrypt, load the encrypted image and use the same key
Click DECRYPT IMAGE
📁 File Structure
PRODIGY_CS_02/
├── PRODIGY_CS_02.py   # Main program
├── requirements.txt   # Dependencies
└── README.md          # Documentation
🛠️ Tech Stack
Tool
Purpose
Python 3
Core language
tkinter
GUI framework
Pillow (PIL)
Image processing
⚠️ Important Notes
Use the exact same key for both encryption and decryption
The encrypted image will look like random noise — this is expected
Output file is saved in the same folder as the original image
