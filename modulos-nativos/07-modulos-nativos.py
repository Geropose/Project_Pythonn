# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template
# import smtplib

# plantilla = Path("modulos-nativos/plantilla.html").read_text("utf-8")

# template = Template(plantilla)
# cuerpo = Template.substitute(usuario="Chanchito triste")

# path = Path("modulos-nativos/holamundo.png")
# mimeImage = MIMEImage(path.read_bytes)
# mensaje = MIMEMultipart()
# mensaje["from"] = "Hola Mundo"
# mensaje["to"] = "ultimatepython@holamundo.io"
# mensaje["subject"] = "Esta es una prueba"
# cuerpo = MIMEText(cuerpo, "html")
# mensaje.attach(cuerpo)
# mensaje.attach(mimeImage)

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     # Nos identifica con el servidor SMTP y con el dominio que usa el correo
#     smtp.starttls()
#     # tls - Transport layer security
#     smtp.login("ultimatepython@holamundo.io", "holamundo123")
#     # Primero va el usuario y luego la contraseña
#     smtp.send_message(mensaje)
#     print("Mensaje enviado")
