import qrcode
import os

print("QR CODE GENERATOR\n")

img = input("Enter the URL: ")
image = qrcode.make(img)

name = input("What do you want to name the QR Code: ")
file_name = (name+".png")


output_path = "C:\\Users\\kevin\\OneDrive\\Documents\\Executables\\1.0 - QR Code"
image.save(os.path.join(output_path, file_name))