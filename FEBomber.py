import os
import smtplib
import getpass
import sys
import time

print("            _________________________________________________       ")
print("            |                                               |       ")
print("            |               Email Spammer Tool              |       ")
print("            |                                               |       ")
print("            |                  Version 1.0                  |       ")
print("            =                                               =       ")
print("            |                   by: Fako                    |       ")
print("            |                                               |       ")
print("            |             !ENJOY BOMBING MAILS!             |       ")
print("            |                                               |       ")
print("            _________________________________________________       ")
print("                                                                    ")
print("                                                                    ")

a = raw_input("Podaj Email: ")
b = raw_input("Podaj Haslo: ")
c = raw_input("Podaj Osobe: ")
d = raw_input("Podaj Tytul: ")
e = raw_input("Podaj Wiadomosc: ")
ff = raw_input("Podaj ilosc emaili: ")
smtp_server = 'smtp.gmail.com'
port = 587


print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(a,b)
    for i in range(1, int(ff)+1):
        subject = os.urandom(9)
        msg = 'From: ' + d + '\nSubject: ' + '\n' + e
        server.sendmail(a,c,e)
        print "\rE-mails sent: %i" % i
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print'\n[!] The username or password you entered are incorrect or you dont have turned on lesssecureapps'
    print'\n[!] - https://myaccount.google.com/u/6/lesssecureapps'
    sys.exit()