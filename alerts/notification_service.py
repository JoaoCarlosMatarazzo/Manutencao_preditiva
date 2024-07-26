import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#notificação por email
def send_email_notification(subject, body, to_emails):
    from_email = 'your_email@example.com'
    from_password = 'your_password'
    
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = ", ".join(to_emails)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587) 
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_emails, message.as_string())
        server.quit()
        
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

def main():
    subject = "Maintenance Alert"
    body = "Alert: Maintenance needed for one or more machines! Please check the system for details."
    to_emails = ["recipient1@example.com", "recipient2@example.com"]
    
    send_email_notification(subject, body, to_emails)

if __name__ == "__main__":
    main()
