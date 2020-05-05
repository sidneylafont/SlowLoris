# Slow Loris

A Slow Loris a Denial of Service attack invented by Robert "RSnake" Hansen, which attacks a website by gaining control 
of as many sockets as possible and continuing to control those sockets by every once in a while sending a small random 
message to the socket to show the website the socket is still in use so that no one else can visit that website. Amazingly a Slow Loris attack uses very 
little bandwidth and does not effect other ports or services, meaning the local machine can run this attack while still
operating normally (the computer still has the bandwidth to play games, watch youtube, etc.).

to use this Slow Loris script:

        $ cd SlowLoris
        $ python SlowLorisScript.py ip-address port number-of-sockets time-inbetween-sending-keep-alive-headers

# Example

For example to attack examplewebsite.com on port 80 maintaining 200 sockets and sending keep alive 
headers every 20 seconds:

        $ cd SlowLoris
        $ python SlowLorisScript.py www.examplewebsite.com 80 200 20

# Packages

- socket
- time
- sys
- random

![pre1.jpg](/images/slowLorisImage.png)