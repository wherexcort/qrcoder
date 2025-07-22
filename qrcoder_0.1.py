import qrcode
import os
from colorama import Fore, Style

print(Fore.RED + """

 ██████╗ ██████╗  ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔═══██╗██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██║   ██║██████╔╝██║     ██║   ██║██║  ██║█████╗  ██████╔╝
██║▄▄ ██║██╔══██╗██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
 ╚══▀▀═╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝      

""" + Style.RESET_ALL)

url = input("url ~ ")

print("select theme qrcode image:")
print("  1. white (clasic)")
print("  2. black")
choice = input("~ ")

if choice == "2":
    fill_color = "white"
    back_color = "black"
else:
    fill_color = "black"
    back_color = "white"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color=fill_color, back_color=back_color)

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = "qrcode.png"
filepath = os.path.join(script_dir, filename)

img.save(filepath)
print(f"✓")
