import smtplib

gmail_user = 'kanat.kaba@gmail.com'
gmail_password = 'Aalam287'

sent_from = gmail_user
to = ['daniyar.kanu@gmail.com']
subject = 'OMG Super Important Message'
body = 'Test 2022 Hello!'

email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

#try:
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()
print('Email sent!')
#except:
print('Something went wrong...')
