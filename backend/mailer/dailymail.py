import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def daily_user_mail(recipient, subject, message):
    """
    Send a notification via email.

    :param recipient: The recipient's email address.
    :param subject: The subject of the email.
    :param message: The content of the email.
    """
    # Your email and password (you should use environment variables for security)
    sender_email = 'madmoviepotato@gmail.com'
    sender_password = 'kmmb zbdk cveq gzuz'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server (in this case, Gmail's SMTP server)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient, msg.as_string())

        # Close the SMTP server
        server.quit()

        print(f"Email notification sent to {recipient} with subject: {subject}")
    except Exception as e:
        print(f"Error sending email notification to {recipient}: {e}")




def format_booking_list(bookings_list):
    # Create an HTML representation of the bookings list
    booking_items = ""
    for booking in bookings_list:
        booking_items += f"""
            <li>
                <strong>Booking ID:</strong> {booking['_id']}<br>
                <strong>Movie Name:</strong> {booking['movie name']}<br>
                <strong>Tag:</strong> {booking['tag']}<br>
                <strong>Rating:</strong> {booking['rating']}<br>
                <strong>Ticket Count:</strong> {booking['ticket_count']}<br>
                <strong>Date:</strong> {booking['date']}<br>
            </li>
        """

    # Create the HTML content for the email with added styling and icons
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            h2 {{
                color: #FF5733;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin-bottom: 20px;
                border: 1px solid #E6E6E6;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                background-color: #F5F5F5;
            }}
        </style>
    </head>
    <body>
        <h2>Monthly Entertainment Report</h2>
        <p>Dear User,</p>
        <p>Here is your monthly entertainment report. Enjoy!</p>
        <ul>
            {booking_items}
        </ul>
        <p>Thank you for using our service!</p>
    </body>
    </html>
    """
    return html_content  

def monthly_user_mail(recipient, subject, bookings_list):
    # Your email and password (you should use environment variables for security)
    sender_email = 'madmoviepotato@gmail.com'
    sender_password = 'kmmb zbdk cveq gzuz'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject

    # Convert the list to HTML format
    html_content = format_booking_list(bookings_list)

    # Attach the HTML message to the email
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Connect to the SMTP server (in this case, Gmail's SMTP server)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient, msg.as_string())

        # Close the SMTP server
        server.quit()

        print(f"Email notification sent to {recipient} with subject: {subject}")
    except Exception as e:
        print(f"Error sending email notification to {recipient}: {e}")