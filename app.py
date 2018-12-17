import socket
import sys
import threading
import random
import time

readbuffer = ""
MODT = False

print("[----] GO GO GO [----]")

def randomString():
	return ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(0, 8)])

def floodThread(socket, user, text, delay):
	while True:
		socket.send(('PRIVMSG ' + user + ' :' + text + '\r\n').encode())
		time.sleep(delay)
		socket.send(('PRIVMSG ' + user + ' :' + text + '_' + randomString() + '\r\n').encode())
		time.sleep(delay)
try:
    user = "#" + sys.argv[1]
    delay = int(sys.argv[2])
    message = ' '.join(sys.argv[3:])
    print("[-] '" + message + "' to twitch.tv/" + sys.argv[1])
    tokens = open('tokens.txt').read().split('\n')
    for x in tokens:
        s = socket.socket()
        s.connect(('irc.twitch.tv', 6667))
        s.send(('PASS ' + x + '\r\n').encode())
        s.send(('NICK ' + randomString() + '\r\n').encode())
        s.send(('JOIN ' + user + '\r\n').encode())        
        t = threading.Thread(target=floodThread, args=(s, user, message, delay,),)
        t.start()
except Exception as e:
	print("[#] error: " + str(e))
	
while True:
    readbuffer = readbuffer + s.recv(1024).decode()
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()
 
    for line in temp:
        # Checks whether the message is PING because its a method of Twitch to check if you're afk
        if (line[0] == "PING"):
            s.send("PONG :tmi.twitch.tv\r\n")
        else:
            # Splits the given string so we can work with it better
            parts = str.split(line, ":")
 
            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    # Sets the message variable to the actual message sent
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""
                # Sets the username variable to the actual username
                usernamesplit = str.split(parts[1], "!")
                username = usernamesplit[0]
              
					
					
 
        for l in parts:
            if "End of /NAMES list" in l:
                MODT = True