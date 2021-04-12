# __________________import labraries____________________
import logging

import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from Controllers import getLagMess, increaseLagMess, format, noConsumer
from Controllers.format import breakLine
from datetime import datetime

def botDo():
    try:
        now = datetime.now()
        current_time = str(now.strftime("%H:%M"))
        current_time = "* _______ *" + '*' + current_time + '*' + "* _______ *"
        print(current_time)
        env_path = Path('.') / '.env'
        load_dotenv(dotenv_path=env_path)
        client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

        numOfTopic = str(getLagMess.getNumTopics())

        allLagMess = getLagMess.countMesLag()

        lagTopic = format.strokeRedNumLagMess(allLagMess)

        incLagMess = 1
        alertOverLagMess = increaseLagMess.alertOverMess(incLagMess, allLagMess)

        numberOverLagMess = str(len(alertOverLagMess))

        lagTopicStr = breakLine(lagTopic)

        alertOverLagMess = breakLine(alertOverLagMess)

        numOfTopicLag = str(len(lagTopic))

        incLagMess = str(incLagMess)

        if int(numOfTopicLag) > 0:
            client.chat_postMessage(channel="#sendnotify",
                                    blocks=[
                                        {
                                            "type": "section",
                                            "text": {
                                                "type": "mrkdwn",
                                                "text": current_time
                                            }
                                        },
                                        {
                                            "type": "section",
                                            "text": {
                                                "type": "mrkdwn",
                                                "text": "* ___Số lượng Topic hiện tại có trong Test:* " + numOfTopic + " topics"
                                            }
                                        },
                                        {
                                            "type": "section",
                                            "text": {
                                                "type": "mrkdwn",
                                                "text": "* ___Topic hiện tại có tin nhắn treo là:* " + numOfTopicLag + " topics " + '\n' + lagTopicStr + '\n' + "* ___Topic lệch " + incLagMess + " tin nhắn:* " + numberOverLagMess + " topics" + "\n" + alertOverLagMess
                                            }
                                        },
                                    ]
                                    )
            current_time2 = ' '
            print("____sent lag messages done____")
        else:
            current_time2 = current_time
            print("___Không có mess bị lag___")
        numLagPart = noConsumer.topicNoCon()
        if int(len(numLagPart)) > 0:
            numLagPart = str(breakLine(numLagPart))
            client.chat_postMessage(channel="#sendnotify",
                                    blocks=[
                                        {
                                            "type": "section",
                                            "text": {
                                                "type": "mrkdwn",
                                                "text": current_time2
                                            }
                                        },
                                        {
                                            "type": "section",
                                            "text": {
                                                "type": "mrkdwn",
                                                "text": "* ___Topics không có owner :* " + numLagPart + " topics"
                                            }
                                        },
                                    ]
                                    )
            print("____sent lag partions done____")
        else:
            print("___Không có partion bị lag___")

    except Exception as e:
        logging.basicConfig(filename='../static/bot.log', filemode='a+',
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
        print("expection rồi bạn ơi: ", e)

if __name__ == "__main__":
    botDo()