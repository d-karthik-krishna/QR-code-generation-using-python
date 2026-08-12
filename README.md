QR Code Generator
A simple and lightweight Python script that generates a QR code from any given URL or text input and saves it as an image file on your local machine.

🚀 Features
Interactive Prompt: Asks the user to input a URL at runtime.
Custom Save Location: Allows you to define exactly where the QR code image should be saved.
Instant Generation: Quickly processes the input and provides console feedback upon successful creation.

📋 Prerequisites
Before running this script, ensure you have Python installed on your system. You will also need to install the qrcode library (and Pillow, which handles the image generation).

Open your terminal or command prompt and run the following command:

Bash
pip install qrcode[pil]
💻 How to Use
1. Configure the Save Path
Open the Python script and locate the file_path variable. Update this variable with the exact location and filename where you want to save your QR code.

Example:

Python
file_path = "D:/MyProjects/my_qrcode.png" 
(Make sure to include the .png extension at the end of your file path).

2. Run the Script
Execute the script from your terminal or IDE:

Bash
python QRCodeGen.py
3. Enter your URL
When the terminal prompts you with Enter the url:, paste the link you want to convert into a QR code and press Enter.

4. Check your output
If successful, the terminal will print GENERATED, and your brand new QR code will be waiting for you at the file path you specified!

🛠️ Built With
Python - The core programming language.

qrcode - The Python QR Code image generator library.
