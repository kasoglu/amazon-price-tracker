# Amazon Price Tracker

An Amazon Price Tracker app helps you to buy which product you want within sale price by sending an E-Mail.

<p align="center">
  <img src="https://i.ibb.co/w749pTp/Screenshot-2021-12-23-at-19-32-42.png" alt="amazon-price-tracker"/>
</p>

# Installing
Download the [Python 3](https://python.org) installer package from the official website and install it, if not installed previously.

* Run the following in the terminal to install the modules to run your program without excussions.
```
pip install bs4
```

```
pip install requests
```

```
pip install smtplib
```

# How to Use?

Download the source code from the repository and run the file just as any other Python script (.py) file.
```
python3 main.py
```

* Note! For the code to work you need to replace all the placeholders with your own details. e.g. ```PRODUCT_URL```, ```PRICE```. 

Follow these instructions below.

1. Find a product on [Amazon](https://www.amazon.com/) that you want to track and get the product URL.
2. In addition to the URL, when you browser tries to load up a page in Amazon, it also passes a bunch of other information. e.g. Which browser you're using, which computer you have etc.


You'll need to pass along some headers in order for the request to return the actual website HTML. At minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header.

3. Head over to [MyHTTPHeader](http://myhttpheader.com) and replace your **"User-Agent"** and **"Accept-Language"** sections as I mentioned in the photo below. 


<p align="center">
  <img src="https://i.ibb.co/MscbWQ7/Screenshot-2021-12-23-at-19-30-00.png" alt="http-header"/>
</p>


4. Also make sure you've got the correct SMTP address for your email provider: (You can use these SMTP Addresses if you're using one of those.)

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com

If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"

Below are steps specific to users sending email from Gmail addresses.

* Make sure you've enabled less secure apps if you are sending from a Gmail account.

* Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha


Check out the link below for more details.

# Documentations

* [MyHTTPHeader](http://myhttpheader.com/)
* [Smtplib Documentation](https://docs.python.org/3/library/smtplib.html)
* [BeautifulSoup Module](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
