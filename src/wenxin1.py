# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: wenxin1.py
@time: 2018/2/18 上午8:59
"""
from weixin0 import *
import itchat,time,re
from   itchat.content  import *

# @itchat.msg_register([TEXT])
# def text_register(msg):
#
#
#     mag = msg['Text']
#     print type(mag)
    # # match = str(getinfo(str(msg['Text'])))
    #
    # if match:
    #     print type('祝您狗年大吉:https://www.jianshu.com/p/d042ff5f4457')
    #     msgs = getinfo(match)
    #     s = str(msgs.encode("utf-8"))
    #     print s
    #     print type(s)
    #
    #     itchat.send((s),msg['FromUserName'])

@itchat.msg_register(itchat.content.TEXT)
# @itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING])
def text_reply(msg):
    mag = msg['Text']
    print type(mag)
    print type(getinfo(str(msg['Text'].encode("utf-8"))))

    return msg['ActualNickName']+getinfo(str(msg['Text'].encode("utf-8")))+ u'爱撒谎的机器人'




@itchat.msg_register(TEXT, isFriendChat=False, isGroupChat=True,isMpChat=True)
def text_reply(msg):
    if msg.isAt:
        return u'{0}：再次确认您的信息是：{1}我会尽快提醒他回复你的！'.format(msg['ActualNickName'],msg['Text'])

    mag = msg['Text']
    print type(mag)
    print type(getinfo(str(msg['Text'].encode("utf-8"))))

    print msg['ActualNickName']
    return u'@{0}：{1} 来自爱撒谎的机器人'.format(msg['ActualNickName'],getinfo(str(msg['Text'].encode("utf-8"))))
#
# @itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING])
# def other_repsly(msg):
#     itchat.send(('看不见'), msg['FromUserName'])
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    #msg.download(msg['FileName'])   #这个同样是下载文件的方式
    msg['Text'](msg['FileName'])      #下载文件
    #将下载的文件发送给发送者
    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg["FileName"]), msg["FromUserName"])


# @itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True,isMpChat=True)
# def text_reply(msg):
#     if(msg.isAt):    #判断是否有人@自己
#     #如果有人@自己，就发一个消息告诉对方我已经收到了信息
#         return ("我已经收到了来自{0}的消息，实际内容为{1}".format(msg['ActualNickName'],msg['Text']),msg['FromUserName'])



itchat.auto_login(enableCmdQR=True,hotReload=True)
itchat.run()
