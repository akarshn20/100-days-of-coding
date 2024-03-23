import requests
import smtplib

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "RELIANCE.BSE",
    "outputsize": "full",
    "apikey": "K**************"
}

news_params = {
    "apiKey": "3***************",
    "qInTitle": "Reliance Industries Ltd"
}

response = requests.get(STOCK_ENDPOINT, stock_params)
response.raise_for_status()
print(response.status_code)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
# print(data_list)
y_close = float(data_list[0]['4. close'])

dby_close = float(data_list[1]['4. close'])

difference = abs(y_close - dby_close)
print(difference)
perc_diff = (difference/float(dby_close))*100
print(perc_diff)

if perc_diff > 0:
    news_response = requests.get(NEWS_ENDPOINT, news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    content = ""
    for article in formatted_articles:
        content += article

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login("akarshn3120@gmail.com", "coabnemhwxbkelvt")
        connection.sendmail(
            "akarshn3120@gmail.com",
            "akarshn20@gmail.com",
            f"Subject:Stock News!\n\n{content.encode('utf-8')}"
        )
