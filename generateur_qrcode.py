import qrcode

def generateur_qrcode(lien):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(lien)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

    print("Le QR code a été généré avec succès !")

# Remplacez "ton_lien" par le lien que tu veux utiliser
generateur_qrcode("ton_lien")
