import email
import imaplib
from bs4 import BeautifulSoup
import datetime

# USER = "bachana3435@gmail.com"
# PASSWORD = "ummagumma3435"

USER = "nemferry@gmail.com"
PASSWORD = "Oliver2019!"
def get_link():

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user=USER,password=PASSWORD)
    mail.select('"Blogabet"')
    result,data = mail.uid('search','(UNSEEN)','(FROM {0})'.format("no-reply@blogabet.com"))
    item_list = data[0].split()
    if len(item_list) > 0:
        # for id in item_list:
        result2, email_data = mail.uid('fetch', item_list[-1], '(RFC822)')
        raw_email = email_data[0][1].decode('utf-8')
        email_message = email.message_from_string(raw_email)
            # print(email_message)
            # print(f"{email_message['Subject']} ")
        mail.logout()
        soup = BeautifulSoup(email_message.get_payload(), 'lxml')
        tags = soup.find_all('a', attrs={"target": "_blank"})
        return tags[1]['href']

# print(dir(email_message))
# print(email_message['To'])
# print(email_message['From'])
# print(email_message['Subject'])
# print(email_message.get_payload())
# html = email_message.get_payload()

# print(get_link())






#
# import email
# import imaplib
# import webbrowser
# import base64
# import requests
# from bs4 import BeautifulSoup
# import datetime
#
# date = (datetime.date.today() - datetime.timedelta(5)).strftime("%d-%b-%Y")
# print(date)
#
# def get_link():
#     # USER = "bachana3435@gmail.com"
#     # PASSWORD = "ummagumma3435"
#     # USER = "nemferry@gmail.com"
#     # PASSWORD = "Oliver2019!"
#     mail = imaplib.IMAP4_SSL("imap.gmail.com")
#     mail.login(user='bachana3435@gmail.com',password='ummagumma3435')
#     # print(mail.list())
#     mail.select('INBOX')
#     # typ,data = mail.recent()
#     # print(data)
#     result,data = mail.search(None,'(SINCE {0})'.format(date),'ALL')
#     print(data[0].split(" "))
#
#     # inbox_item_list = data[0].split()
#     # print(len(inbox_item_list))
#     # print(inbox_item_list)
#     # #
#     # latest_email_id = inbox_item_list[-1]
#     # result2, email_data = mail.uid('fetch', latest_email_id, '(RFC822)')
#     # print(email_data)
#     # raw_email = email_data[0][1]
#     # email_message = email.message_from_string(raw_email)
#     # print(email_message['Subject'])
#     # # print(email_message.get_payload())
#     # soup = BeautifulSoup(email_message.get_payload(), 'lxml')
#     # tags = soup.find_all('a', attrs={"target": "_blank"})
#     # # print(tags[1]['href'])
#     # return tags[1]['href']
#     return
#         # for el in tags:
#         #     print(el['href'])
#
#
#
# #     email_message = email.message_from_string(raw_email)
# #     print(email_message['From'])
#
# # most_recent = inbox_item_list[-1]
# # oldest = inbox_item_list[0]
# # result2,email_data = mail.uid('fetch',most_recent,'(RFC822)')
# # raw_email = email_data[0][1].decode("utf-8")
# # email_message = email.message_from_string(raw_email)
#
# # print(dir(email_message))
# # print(email_message['To'])
# # print(email_message['From'])
# # print(email_message['Subject'])
# # print(email_message.get_payload())
# # html = email_message.get_payload()
#
# #
# # import os
# # with open('rend.html','w') as f:
# #     f.write(html)
# # filename = 'file:///'+os.getcwd()+'/' + 'rend.html'
# #
# # webbrowser.open(url=filename)
# print(get_link())