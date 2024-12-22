from gnewsclient import gnewsclient
from tkinter import *
def news():
  client=gnewsclient.NewsClient(
      language=lang.get(),location=loc.get(),topic=top.get(),max_results=10)
  news_list=client.get_news()
  result_title.set(news_list[0]["title"] + "\n" +
                   news_list[1]["title"] + "\n" +
                   news_list[2]["title"] + "\n" +
                   news_list[3]["title"] + "\n" +
                   news_list[4]["title"] + "\n" +
                   news_list[5]["title"] + "\n" +
                   news_list[6]["title"] + "\n" +
                   news_list[7]["title"] + "\n" +
                   news_list[8]["title"] + "\n" +
                   news_list[9]["title"])

master=Tk()
master.title("NEWS")

master.configure(bg='white')

result_title=StringVar()
result_link=StringVar()

Label(master,text="Choose Language: ", bg='light grey').grid(row=0,sticky=W)
Label(master,text="Choose Location:",bg='light grey').grid(row=1,sticky=W)
Label(master,text="Choose Topic:",bg='light grey').grid(row=2,sticky=W)

lang=Entry(master)
lang.grid(row=0,column=1)

loc=Entry(master)
loc.grid(row=1,column=1)

top=Entry(master)
top.grid(row=2,column=1)

Label(master,text="",textvariable=result_title,bg='light grey').grid(row=3,column=1,sticky=W)

Button(master,text="SHOW",command=news,bg="white").grid(row=1,column=3)

mainloop()