import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


# Amazon Product URL (You can change the product which you want to buy.)
PRODUCT_URL = ""
BUY_PRICE = PRICE  # Type buy price in United States Dollar (USD).

# Edit this section with your own information.

YOUR_SMTP_ADDRESS = "YOUR_SMTP_ADDRESS"
YOUR_EMAIL = "YOUR_EMAIL"
YOUR_PASSWORD = "YOUR_PASSWORD"

# Head over to (http://myhttpheader.com) and replace your "User-Agent" and "Accept-Language".
headers = {
    "User-Agent": "",
    "Accept-Language": ""
}

response = requests.get(url=PRODUCT_URL, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

title = soup.find(id="productTitle").get_text().strip()

# When product goes on sale and the price below to your BUY_PRICE, it sends an E-Mail to you.

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(user=YOUR_EMAIL, password=YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}"
        )