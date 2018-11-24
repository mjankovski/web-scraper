#!/usr/bin/env python

from lxml import html
import requests
import smtplib
import time
import datetime
import random


# setup your settings below
login = 'your email adress'
password = 'email password'
msg = 'Alert!'
receiverMail = 'receiver email address'
website = 'website url'
element = '//div[@class="class name you want to check"]/text()'
priceLevel = 100
notSend = True


def scrap():
    page = requests.get(website)
    tree = html.fromstring(page.content)
    price = tree.xpath(element)[0]
    state = True

    if int(price) < priceLevel:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(login, password)
        server.sendmail(login, receiverMail, msg)
        server.quit()
        state = False

    print(datetime.datetime.now())
    print(price)
    return state


# loop to continuous monitoring price on the website
# ctrl+c to stop script
while notSend:
    notSend = scrap()
    sleepTime = 8 + random.randint(0, 5)
    time.sleep(sleepTime)
