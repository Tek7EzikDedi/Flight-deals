import smtplib
import os
my_email = "fatihharsx4@gmail.com"
password = os.environ["password"]


class NotificationManager:
    def send_email(self, price, cityFrom, cityTo, deep_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Low price alert!\n\nOnly £{price} to fly from {cityFrom} to {cityTo}\n\nlink:{deep_link}".encode("UTF-8"))


