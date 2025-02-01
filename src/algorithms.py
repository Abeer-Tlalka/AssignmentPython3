# 1. Write a Python script to solve a Sudoku puzzle.
# 2. Create a Python program to implement the binary search algorithm.

# 3. Write a program to perform matrix multiplication using NumPy.
# 4. Develop a program to send an email using the smtplib library.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    '''
    Function to send an email using SMTP
    :param sender_email: Your email address
    :param sender_password: Your email password or app password
    :param recipient_email: Recipient's email address
    :param subject: Subject of the email
    :param message: Message content of the email
    :return: None
    '''
    
    # Set up the SMTP server (Gmail SMTP used here)
    smtp_server = "smtp.gmail.com"  # Use your email provider's SMTP server
    smtp_port = 587  # Gmail uses 587 for TLS

    try:
        # Create an SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade connection to secure TLS
        
        # Login to the email account
        server.login(sender_email, sender_password)
        
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)

    finally:
        # Close the SMTP connection
        server.quit()

#TEST THE SEND EMAIL FUNCTION

# send_email("teachtouchsce@gmail.com", "Teachtouchsce20232024", "abeer.altlalka@gmail.com", "Test", "this is a test email")




# 5. Write a Python script to scrape headlines from a news website using BeautifulSoup.
# 6. Create a Python program to encrypt and decrypt text using a simple Caesar cipher.
# 7. Write a program to generate QR codes using the qrcode library.
import qrcode

def generate_qr(data, filename="qrcode.png"):
    '''
    Function to generate a QR code and save it as an image
    :param data: The data to encode in the QR code
    :param filename: The name of the file to save the QR code image
    :return: None
    '''
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size around the QR code
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill="black", back_color="white")

    # Save the image to a file
    img.save(filename)

    print(f"QR Code saved as {filename}")

# Example Usage
# generate_qr("https://www.google.com", "google_qr.png")


# 8. Implement a program to perform multithreading for downloading multiple files simultaneously.