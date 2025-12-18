import os
from pathlib import Path
import qrcode

url = input("Enter the URL: ").strip()
name = input("Enter the file name: ").strip()

base_path = Path(r"C:\Users\jeroh\OneDrive\Documentos\QRcode\QRs")
base_path.mkdir(parents=True, exist_ok=True)

file_path = base_path / f"{name}.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code was generated")
os.startfile(file_path)  