import smtplib
s = smtplib.SMTP("172.30.42.127", 25)
try:
    m = "\nThis is a message"
    s.sendmail("ricmessier@gmail.com", "ric@cloudroy.com", m)
    print("Finished sending message")

except Exception as e:
    print("Unable to send message:", e)
s.quit()