import socket

# These are required
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'hazard_knight'
token = 'oauth:33yrdii4lajvw1fzlann7sedpvpxo8'


print("Enter channel name: ")
# Channel name  format is '#name'
fileName = input()
channel = '#' + fileName
print("Connecting...")
sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))
print("Connected to host!")

resp = sock.recv(2048).decode('utf-8')

resp

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler(fileName +  '.log', encoding='utf-8')])

logging.info(resp)

from emoji import demojize

end = 1

while(end != 4):
    
    while True:

        sock.settimeout(75)

        try:
            resp = sock.recv(4096).decode('utf-8')

            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))
    
            elif len(resp) > 0:
                logging.info(demojize(resp))

            # These never execute
            #if not resp: break
            #if(resp == 0): break
            #if(resp == -1): break
        except socket.timeout:
            print("Message lost")
            break

    print("Attempting to collect messages again...")
    end += 1


sock.close()
print("Socket closed")
