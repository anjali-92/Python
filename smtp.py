#without proxy

import smtplib

content = "First Email"

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()
mail.ehlo

mail.login('anjalipardeshi92@gmail.com', 'my_password')

mail.sendmail('anjalipardeshi92@gmail.com', 'joinshack92@gmail.com', content )

mail.close()

'''
send_mail('Django App sent mail', 'excited to send email through app ', 'anjalipardeshi92@gmail.com', ['anjalipardeshi92@gmail.com'], fail_silently=False, auth_user='anjalipardeshi92@gmail.com', auth_password='my_password')

'''
