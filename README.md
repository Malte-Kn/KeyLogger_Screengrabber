# KeyLogger_Screengrabber
Keyloggers written in Python with additional functionality
## Overview
In this project we created two keyloggers with different functionalities and exfiltration.
The keyloggers are equipped with quality-of-life features for better readability of the generated logs.
Additionally, we added a screengrabber to capture the affected screen every couple of seconds.
This project is designed to archive better understanding of tools used in the field of cybersecurity and educational only.

## Standard Keylogger
The standard keylogger can be found in the keylogger.py it simply records all keystrokes in a log.
Special keys such as "space","tab" and "enter" are translated to achieve better readability in the logs.
Furthermore, are we tracking the time between keystrokes and creating a separation when no key is pressed for some period of time.
For the same period of time, we will create a screenshot of the affected user.
The logs and screenshots are saved in different files.

## HTTP Keylogger
The HTTP keylogger has the same functionalities as the standard keylogger; however, instead of saving the logs and screenshots, we exfiltrate them via HTTP requests to a specific server.
For the normal logs, every X amount of seconds, the last keys are sent in a GET request after being base64 encoded.
The pictures are sent via POST request to the server.
We provided a simple Flask web server to track the keystrokes and screenshots, but a simple Python http-server can do the trick.
