
# Infinite DDOS

Infinite DDOS is a DDOS tool created with Python that utilizes stresser.su's free ddos plan to infinitly use it and keep targets offline for as long as you want, the tool can currently only take down websites however it is still very powerful and could take down some big websites.

## How to Use:

### Step One:
Create an account on https://stresser.su/, this is the website that has a free to use plan that is powerful enough to take down alot of websites.

### Step Two:
We now need to get our Cookies (🍪 Yummm..) from the site which will allow us to use the site in our program without us having to do anything, remember cookies are a way to access your account so don't share them with anyone, heres how to get your cookies:

![App Screenshot](https://raw.githubusercontent.com/NotKatsu/Infinite-DDOS/main/images/Untitled.png)

Once you get to this stage just right click and click on "Copy Value".

### Step Three
Now we can give the script our Cookie, we can do this by opening `stresser.py` then scroll to the bottom and put your cookie in cookie="" as shown below.

```python
stresser_object: object = Stresser(cookie="COOKIE GOES HERE.")
```

### Step Four:
You can now open `stresser.py` it will ask you for a website URL so just put your site and then it will ask you for a method, if you don't know the method just put https.

### Errors:
If you get an error that says you can only run one attack at a time this is because you recently just stopped another attack, please wait a few minutes until that finishes.

If the script gives you another error its most likely because your Cookie expired, just replace the Cookie and start the script again.

## Read Me:
Please do NOT use this tool for any malicious purposes and this tool is only here to be used on your own websites, if people start using this on websites that isn't theres ill take it down, this tool was made to show how easy it is for anyone to take even large websites down. By using the tool you accept full responsibilty for whatever may happen to you if you use it in a way that was not intended.
