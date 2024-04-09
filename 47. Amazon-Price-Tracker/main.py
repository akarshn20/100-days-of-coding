import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8"
}

response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find(class_="a-offscreen")
price_without_currency = price.getText().split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


if price_as_float <= 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login("akarshn3120@gmail.com", "coabnemhwxbkelvt")
        connection.sendmail(
            "akarshn3120@gmail.com",
            "akarshn20@gmail.com",
            f"Subject:Amazon Price Alert\n\n{soup.title.getText()} is now for ${price_as_float}\n{URL}".encode('utf-8')
        )

