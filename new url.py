from cgitb import text
import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("600x300")
root.title("My URL SHORTENER")
root.configure(bg= "#49A")
url = StringVar()
url_address = StringVar()

def urlshortener():
    url_address = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address)
    url_address.set(url_short)


def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


Label(root, text ="My URL Shortener", font= "popins").pack(pady=20)
Entry(root, textvariable=url).pack(pady=10)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=14)
Entry(root, textvariable=url_address).pack(pady=10)
Button(root, text="Copy URL", command=copyurl).pack(pady=10)

root.mainloop()
