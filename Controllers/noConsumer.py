import logging

import requests
from bs4 import BeautifulSoup
from Controllers import getExcel, getLagMess


# Tìm topics không có consummer owners
def topicNoCon(b = getExcel.getListTopic()):
    try:
        global soup
        c = list()
        # get all topics in test link
        a = getLagMess.countTopicDone()
        for i in a:
            d = i.split('/')
            m = d[-3]
            for x in b:
                if m == x:
                    c.append(i)

        # Get partion of topic have not consumer
        listLinkn = list()
        for u in c:

                urln = "http://183.91.14.138:9000" + u
                html_textn = requests.get(urln).text
                soup = BeautifulSoup(html_textn, 'html.parser')
                numPartions = -1
                numLagPartions = list()
                for link in soup.select('td:nth-of-type(5)'):
                    numPartions = numPartions + 1
                    link = str(link)
                    soup2 = BeautifulSoup(link, 'html.parser')
                    tag = soup2.td
                    text = tag.string
                    if text is None:
                        numLagPartions.append(",(*_Partions_*): " + '`'+str(numPartions)+'`')
                if len(numLagPartions) != 0:
                    u = u.split('/')
                    numLagPartions.append(",(*_Topic_*): "+u[4])
                    numLagPartions.append("(*_Group_*): "+u[-3])
                    numLagPartions=numLagPartions[::-1]
                    lagPart = " ".join(numLagPartions)
                    listLinkn.append(lagPart)
                numLagPartions.clear()
        return listLinkn
    except Exception as e:
        logging.basicConfig(filename='../static/noConSumer.log', filemode='a+',
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
        print("noConsumer.py topicNoCon expection", e)

if __name__ == "__main__":
    topicNoCon()


