#!/usr/bin/env python

from lxml import html
import requests
import smtplib


# setup your settings below
login = 'your@email.com'
password = 'YourPassword'
msg = 'Alert!'
receiverMail = 'receiver@mail.com'
website = 'https://websiteadress.com/index.html'
element = '//div[@class="class name"]/text()'
priceLevel = 100


def scrap():
    page = requests.get(website)
    tree = html.fromstring(page.content)
    price = tree.xpath(element)[0]

    if int(price) < priceLevel:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(login, password)
        server.sendmail(login, receiverMail, msg)
        server.quit()
    return


# infinite loop to continuous monitoring price on the website
# ctrl+c to stop running script
while True:
    scrap()
