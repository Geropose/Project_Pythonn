# # Variables de entorno

# import os
# from sendgrid.helpers.mail import Mail
# from sendgrid import SendGridAPIClient

# apikey = os.environ.get("SENDGRID_API_KEY")
# email = os.environ.get("SENDGRID_EMAIL")

# mensaje = Mail(
#     from_email=email,
#     to_emails=email,
#     subject="Correo de prueba",
#     html_content="Curso de <b> Ultimate python </b>",
# )

# try:
#     apikey = os.environ.get("SENDGRID_API_KEY")
#     sg = SendGridAPIClient(apikey)
#     sg.send(mensaje)
# except Exception as e:
#     print(e)
