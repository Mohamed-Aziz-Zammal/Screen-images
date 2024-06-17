import pyautogui
import smtplib
from email.message import EmailMessage

# Take a screenshot
screenshot = pyautogui.screenshot("mail.png")

# Create the email message
msg = EmailMessage()
msg['Subject'] = 'Subject of the Email'
msg['From'] = 'your-email@gmail.com'
msg['To'] = 'recipient-email@gmail.com'
msg.set_content('Here is the screenshot.')

# Read the screenshot file and add it as an attachment
with open("mail.png", "rb") as f:
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)

# Set up the SMTP connection and send the email
conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()
conn.login("your-email@gmail.com", "your-password")
conn.send_message(msg)
conn.quit()
