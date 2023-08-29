import requests
import datetime as dt
import smtplib

#it was supposed to be done with Twillio but nahh idc
MY_EMAIL="maciejkrefft03@gmail.com"
PASSWORD="mwwnsttuqrcshaxu"

STOCK_APIKEY="M3M8JRLY9KV7J08G"
NEWS_APIKEY="32ada34ae94b4251a33508f9dec9d1ce"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = f"https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params={
    "apikey":STOCK_APIKEY,
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME
}

stock_prices_reponse=requests.get(STOCK_ENDPOINT,stock_params)
stock_prices_reponse.raise_for_status()
stock_prices_data=stock_prices_reponse.json()["Time Series (Daily)"]
stock_prices_data_list=[value for (key,value) in stock_prices_data.items()]

yesterday_data=stock_prices_data_list[0]
yesterday_closing_price=float(yesterday_data["4. close"])

twodays_ago_data=stock_prices_data_list[1]
twodays_ago_closing_price=float(twodays_ago_data["4. close"])

difference=round(yesterday_closing_price - twodays_ago_closing_price)
difference_abs=round(abs(yesterday_closing_price - twodays_ago_closing_price),2)
diff_percent=round((difference_abs / yesterday_closing_price * 100),2)

news_params={
    "apiKey":NEWS_APIKEY,
    "qInTitle":COMPANY_NAME
}

emoji=None
if(difference>=0):
    emoji="🔺"
else:
    emoji="🔻"

if(diff_percent>5):
    news_reponse=requests.get(NEWS_ENDPOINT,news_params)
    news_reponse.raise_for_status()
    news_data=news_reponse.json()["articles"]
    news_data_sliced=news_data[:3]


    formatted_articles=[f"{STOCK_NAME}: {emoji}{diff_percent}%\nHeadline: {article['title']}. \nBrief:\n{article['description']}." for article in news_data_sliced]

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        
        subject="Stock info for today"
        content="\n\n\n".join(formatted_articles)
        msg = f"Subject:{subject}\n\n{content}"
        msg_bytes = msg.encode("utf-8")
        
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=msg_bytes)