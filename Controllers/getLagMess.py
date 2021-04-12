import requests
from bs4 import BeautifulSoup
from Controllers import getExcel
import logging

topicInExcelFile = getExcel.getListTopic() # Get Topic names that is in excel file

def getNumTopics():
    try:
        url = 'http://183.91.14.138:9000/clusters/Test'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        listLink33 = str(soup.select('td:nth-of-type(2) a'))
        soup33 = BeautifulSoup(listLink33, 'html.parser')
        listLink33 = ((soup33.get_text()).strip(']')).strip("[")
        return listLink33
    except Exception as e:
        logging.basicConfig(filename='../static/getLagMess.log', filemode='a+',
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
        print("getLagMess getNumTopics expection: ", e)




# get all link in Test link
def countTopicDone():
    try:
        url = 'http://183.91.14.138:9000/clusters/Test/consumers'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        listLink = list()
        for link in soup.select('td:nth-of-type(3) a'):
            listLink.append(link.get('href'))
        return listLink
    except Exception as e:
        logging.basicConfig(filename='../static/getLagMess.log', filemode='a+',
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
        print("getLagMess.py countTopicDone exception: ", e)


# Get text
def getText(stt):
    try:
        url = 'http://183.91.14.138:9000/clusters/Test/consumers'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        stt = str("td:nth-of-type("+str(stt)+") a")
        listLink2 = list()
        for link in soup.select(stt):
            listLink2.append(link)
        html_doc = str(listLink2)
        soup2 = BeautifulSoup(html_doc, 'html.parser')
        txtIn = soup2.get_text()
        txtIn = txtIn.rstrip(']')
        txtIn = txtIn.lstrip('[')
        txtIn = txtIn.split(',')
        txtInRemoveSpace = list()
        for ele in txtIn:
            txtInRemoveSpace.append(ele.strip())
        return txtInRemoveSpace
    except Exception as e:
        logging.basicConfig(filename='getLagMess.log', filemode='a+', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
        print("getLagMess.py getText exception: ", e)


# The function find all lag messages in the topics
def countMesLag(numLagMessNeedCheck=0):
    try:
        listTdElementInTestLink = list()
        url = 'http://183.91.14.138:9000/clusters/Test/consumers'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        numLagMessNeedCheck = ' ' + str(numLagMessNeedCheck)+' lag'
        # Get all td that is in " Topics it consumes from " column
        for link in soup.select('td:nth-of-type(3)'):
            listTdElementInTestLink.append(link)

        # Get text in a element html
        aElementInTestLink = list()
        for i in listTdElementInTestLink:
            i = str(i)
            soup2 = BeautifulSoup(i, 'html.parser')  # change every a element in lis to get text
            tags = soup2.find_all('td')
            textLinkInTest = tags[0].text
            href = tags[0].herf
            aElementInTestLink.append(textLinkInTest)

        # divide string at "\n"
        listTextLinkInTest = list()
        for txt in aElementInTestLink:
            trt = txt.splitlines()
            listTextLinkInTest.extend(trt)

        # remove space in list
        reMoveSpace = list()
        for ele in listTextLinkInTest:
            if ele.strip():
                reMoveSpace.append(ele)

        # Concatenate 2 next to items in a list reMoveSpace
        getGroupForLagTopic = countTopicDone()
        conTowStrings = list()
        for i in topicInExcelFile:
            a = i + ':'
            for j in range(len(reMoveSpace)):
                if a == reMoveSpace[j]:
                    for g in getGroupForLagTopic:
                        sCut = g.split('/')
                        if sCut[-3] == i:
                            txt = str('(*_Group:_*) ' + sCut[4] + ' ,(*_topic:_*) ' + reMoveSpace[j] + reMoveSpace[j + 1])
                            if (txt.find(numLagMessNeedCheck)) == -1:
                                conTowStrings.append(txt)
                        sCut.clear()
                j = j + 2
        conTowStrings = sorted(conTowStrings)
        lagMessage = list()
        for i in conTowStrings:
            if i not in lagMessage:
                lagMessage.append(i)
        return lagMessage
    except Exception as e:
        logging.basicConfig(filename='../static/getLagMess.log', filemode='a+', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
        print("getLagMess.py countMesLag exception:", e)

if __name__ == '__main__':
    countTopicDone()
    countMesLag()

