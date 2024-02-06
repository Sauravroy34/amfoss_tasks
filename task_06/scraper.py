import requests
import bs4
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
def check():
    try:
        req = requests.get("https://www.espncricinfo.com/live-cricket-score")

    except:
        return("please try again later")
    soup = bs4.BeautifulSoup(req.text,"lxml")
    score = soup.find("div", class_= "ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1")
    team1 = soup.find("p",class_ = "ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3")
    team2 = soup.find("p",class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")
    stuff = soup.find("span",class_="ds-text-tight-xs ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block !ds-inline")
    result = soup.find("p",class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")


    for i in stuff:
        s =(i.getText())
    for i in team1:
        m = team1.getText()
    for i in team2:
        l = team2.getText()

    for i in score:
        p =(i.getText())

    for i in result:
        q =(i.getText())

    return s +  "\n" + l + "\n" +m +"\n" + p +"\n" + q + "\n" + dt_string



def intro():
    l= ("hi am crickery your cricket bot ")
    s =("!help for help \n !liverscore to get livescore \n !csv to get csv file ")
    return l +"\n" + s