# Libreria que sirve para gestionar el envio de correos electronicos
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from os import environ
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enviar_email(destinatario, asunto, cuerpo):
    email_emisor = environ.get('CORREO_EMISOR')
    password_emisor = environ.get('PASSWORD_EMISOR')

    # ahora creamos el cuerpo del email
    cuerpo_del_correo = MIMEText(cuerpo, 'plain')

    correo = MIMEMultipart()
    correo['Subject'] = asunto
    correo['To'] = destinatario
    correo.attach(cuerpo_del_correo)

    try:
        # Procedemos con el envio
        manejador_correo = SMTP('smtp.gmail.com', 587)
        manejador_correo.starttls()
        manejador_correo.login(email_emisor, password_emisor)
        manejador_correo.sendmail(from_addr=email_emisor, to_addrs=destinatario, msg=correo.as_string())
        manejador_correo.quit()
        logging.info('Correo enviado exitosamente')
    except Exception as e:
        logging.error(f'Error al enviar el correo: {e}')
