import qrcode
features=qrcode.QRCode(version=1,box_size=30,border=4)
features.add_data("https://github.com/Ajay10-S/Ajay_fold_pro")
features.make(fit=True)
aj=features.make_image(fill_color="black",back_color="white")
aj.save("image1.png")
