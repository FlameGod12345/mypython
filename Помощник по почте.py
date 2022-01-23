import smtplib
a = input('Введите почту(-ы) куда будет отправлено письмо: ')
gmail_user = 'daniyar.kanu@gmail.com'
gmail_password = 'nagibator228'

sent_from = gmail_user
#sent_to = ['daniyar.kanu@gmail.com', 'poeshbebro4ki@gmail.com']
sent_to = []
a.split(',')
sent_to.append(a)
print(sent_to)
email_text = input('Введите текст письма: ')
print(sent_to)
try:
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_password)
    smtpserver.sendmail(sent_from, sent_to, email_text)
    smtpserver.close()
    print('Сообщение отправлено!!!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)
    print('Сообщение не отправлено!!!')
