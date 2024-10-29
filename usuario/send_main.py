import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Função para enviar e-mail
def enviar_email(destinatario, assunto, mensagem):
    remetente = 'jonatasaraujox9@gmail.com'
    senha = 'gzqx njtm liky shpp'

    # Configurando a mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Corpo do email
    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        # Conectando ao servidor Gmail
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()  # Segurança
        servidor.login(remetente, senha)

        # Enviando o email
        texto = msg.as_string()
        servidor.sendmail(remetente, destinatario, texto)
        servidor.quit()

        return f"Email enviado para {destinatario}"
    except Exception as e:
        return f"Erro ao enviar email: {e}"
        

# Exemplo de uso
def Send_password(destinatario, assunto, mensagem):
   return enviar_email(destinatario, assunto, mensagem)
