import qrcode

url = input("Enter the url: ").strip()
file_path = ""#give your file path here 

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path) #instead of file_path you can directly give your path here 

if img:
    print("GENERATED")
else :
    print("NOT GENERATED")