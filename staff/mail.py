def code_mail(sender_email, receiver_email, password, code):
  import smtplib, ssl
  from email.mime.text import MIMEText
  from email.mime.multipart import MIMEMultipart

  port = 465

  message = MIMEMultipart("alternative")
  message["Subject"] = "Cotización exitosa"
  message["From"] = sender_email
  message["To"] = receiver_email

  text = """\
    """
  html = f"""\
  <html>
    <body>
      <p> Visita nuestra página <br>
        <a href="https://www.homeworkcrafter.com">www.homeworkcrafter.com</a><br>
        Puedes consultar tu pedido con el código: Tzallas se la come.
      </p>
    </body>
  </html>
  """
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")

  message.attach(part1)
  message.attach(part2)


  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
        sender_email, receiver_email, message.as_string()
        )
    



