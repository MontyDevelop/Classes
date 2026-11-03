from tkinter import *
import requests
from bs4 import BeautifulSoup

screen=Tk()
screen.geometry("300x300")

url = "https://news.ycombinator.com/"
response = requests.get(url)
def title1():
    soup=BeautifulSoup(response.text,"html.parser")
    title=Label(screen,text=f"{soup.title.text}")
    title.pack()
show_title=Button(screen,text="click to reveal title",command=title1)
show_title.pack()

def news1():
    for i in range(0,5):
        soup = BeautifulSoup(response.text, "html.parser")
        title = Label(screen, text=f"{soup.athing_submission.text}")
        title.pack()
        news=Label(screen,text=f"{soup.news2}")
        news.pack()

show_news=Button(screen,text="click to reveal top 5 news headings",command=news1)
show_news.pack()

screen.mainloop()