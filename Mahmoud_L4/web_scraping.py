# import requests
# from bs4 import BeautifulSoup

# # url = "http://127.0.0.1:5500/Mahmoud_L4/index.html"
# # url = "https://www.amazon.in/Lotto-Strada-Blend-Black-Sneakers/dp/B0FFTFX54M/?_encoding=UTF8&pd_rd_w=nfxVJ&content-id=amzn1.sym.91531c71-2a9c-49db-a0bc-ac5c8ecba877&pf_rd_p=91531c71-2a9c-49db-a0bc-ac5c8ecba877&pf_rd_r=JF3M6Q8WP5VG7399B05E&pd_rd_wg=LL7lp&pd_rd_r=bf2317fd-86d8-4f3b-bad4-1d741ef89746&ref_=pd_hp_d_r_btf_dealz_m1_hw_t1_hxwDSD_sspa_dk_gateway&ie=UTF8&sloctc=1&sp_csd=d2lkZ2V0TmFtZT1zcF9ob21lcGFnZV9ibGVuZGVk&th=1&psc=1"

# # url = "https://en.wikipedia.org/wiki/Main_Page"
# url = "https://news.ycombinator.com/news"

# response = requests.get(url)
# print(response)


# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title.text)
# print(soup)

# print(response)

# rate limit
# how many requests you can send to a website to scrap the data

# reasonable scraps


# data = soup.find_all("a")

# list1 = []

# for i in data:
#     print(i.text.strip())

# for i in data:
#     print(i.get('href'))

# ------------------------------------------------------------------


# ex1: print the title of hackernews web page

# import requests
# from bs4 import BeautifulSoup

# url = "https://news.ycombinator.com/news"

# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")


# # ex2: find all the stories

# news = soup.select(".athing")
# # print(len(news))

# # ex3: print all the news headings

# # for i in news:
# #     heading = i.select_one(".titleline").get_text()
# #     print(heading)

# # ex4:

# # for i in news:
# #     sno = i.select_one(".rank").get_text()
# #     heading = i.select_one(".titleline").get_text()
# #     print(sno, heading)


# ---------------------------------------------------------

import tkinter as tk
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"


def get_page_title():
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    result.delete("1.0", tk.END)
    result.insert(tk.END, soup.title.text)


def get_top_5_news():
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    stories = soup.select(".athing")
    
    result.delete("1.0", tk.END)

    count = 1
    for story in stories[:5]:
        title = story.select_one(".titleline a").get_text()
        result.insert("end", str(count) + ". " + title + "\n\n")
        count = count + 1


# Create window
window = tk.Tk()
window.title("Hacker News Scraper")
window.geometry("600x400")

# Button 1
button1 = tk.Button(window,text="Get Page Title",command=get_page_title)
button1.pack(pady=10)

# Button 2
button2 = tk.Button(window,text="Get Top 5 News",command=get_top_5_news)
button2.pack(pady=10)

# Display results
result = tk.Text(window, height=15, width=65)
result.pack(pady=10)

window.mainloop()
