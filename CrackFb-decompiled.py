# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: <seni>
import os, sys, time, random
G = '\x1b[1;32m'
B = '\x1b[1;34m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
D = '\x1b[1;30m'
R = '\x1b[1;31m'
GD = '\x1b[32m'
print '\x1b[1;33mwaiting... '
time.sleep(2)
os.system('sh me.sh')
os.system('clear')
os.system('clear')
print GD + "\n\n____________                     _    \n|  ___| ___ \\                   | |   \n| |_  | |_/ / ___ _ __ __ _  ___| | __\n|  _| | ___ \\/ __| '__/ _` |/ __| |/ /\n| |   | |_/ / (__| | | (_| | (__|   < \n\\_|   \\____/ \\___|_|  \\__,_|\\___|_|\\_\n%sCoded by: Star\n" % C
try:
    print W + '1).Crack via ID \n2).Crack via Username \nPrees CTRL + z to exit.. '
    print
    user = raw_input('root@Star ~# ')
    if user in ('1', 'Crack via ID', 'crack via id'):
        target = raw_input('ID target >')
        pw = ['akusayangkamu', 'loveyou', 'sayang', 'bajingan', 'hacker123']
        rand = random.choice(pw)
        os.system('sh me.sh')
        os.system('clear')
        os.system('figlet Star | lolcat ')
        print
        print D + 'Connecting to https://m.facebook.com....'
        time.sleep(9)
        print (W + 'Cracking password from ID %s{} %splease wait...' % (B, W)).format(target)
        time.sleep(9)
        print (Y + 'Succsess, %s{} %s[%s{}%s]... ' % (B, W, R, W)).format(target, rand)
        sys.exit()
    if user in ('2', 'Crack via Username', 'crack via username'):
        targetv = raw_input(W + 'Username Target >')
        pwv = ['sayang', 'ahhhCroot', 'kesayangan', 'kamumilikku']
        randv = random.choice(pwv)
        os.system('sh mee.sh')
        os.system('clear')
        print D + 'Connecting to https://m.facebook.com...'
        time.sleep(9)
        print (W + 'Cracking password from account %s{} %splease wait....' % (B, W)).format(targetv)
        time.sleep(9)
        print (Y + 'Succsess, %s{} %s[%s{}%s]' % (B, W, R, W)).format(targetv, randv)
        sys.exit()
except EOFError:
    print 'Mohon Diisi Dengan Benar.'
except KeyboardInterrupt:
    print 'Kok Gajadi Gan?'