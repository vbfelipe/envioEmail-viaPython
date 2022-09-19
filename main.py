#Importação do módulo SMTPLIP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()

#Corpo do e-mail.
texto = "TEXTO" 

#A senha do seu e-mail microsoft.
senha = "SENHA" 

#Seu e-mail.
msg['From'] = "SEU E-MAIL"

#E-mail do destinatário.
msg['To'] = "DESTINATÁRIO" 

#Assunto do e-mail.
msg['Subject'] = "E-mail enviado via Python!"

msg.attach(MIMEText(texto, 'plain'))

#Endereço do server Microsoft
server = smtplib.SMTP('smtp.office365.com: 587')
server.starttls()
server.login(msg['From'], senha)
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print('Mensagem enviada com sucesso.\n ')