import logging

from Controllers.getExcel import getListTopic, getListGroup
from Controllers.getLagMess import getText


def NotInTest():
    try:
        allTopicHere=getListTopic()
        allTopicTest = getText(3)
        res = [x for x in allTopicHere + allTopicTest if x not in allTopicTest ]

        allGroupHere =getListGroup()
        allGroupTest = getText(1)
        ras = [x for x in allGroupHere + allGroupTest if x not in allGroupTest]
        return res,ras
    except Exception as e:
            logging.basicConfig(filename='../static/sche.log', filemode='a+', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(e)
            print("notInTest.py NotInTest expection: ", e)
