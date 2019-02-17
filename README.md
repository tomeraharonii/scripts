# Nagish
A software which makes it easy for the hearing and speech impaired to speak on the phone

# The Components:
* Web interface and signup form (HTML/CSS)
* app.py is a Flask apllication to serve webpage and bot endpoints (Python)
* phone.py interacts with the Twilio API to get phone calls recordings and convert speech-to-text and text-to-speech in real time using google translate API. (Python)

# Flow:
* Users sign up on our webpage by using their Facebook profile.
* They are then given an auto-generated twilio phone number which is linked to their FB account.
* Any call recieved to this number will be directed stright to their fb messenger window and the input voice will be converted to text. Whereas everything that is typed in the fb messenger window will be converted to voice and heard on the phone.

# What it does:
Nagish is just as simple as placing a regular phone call. It connects people together by allowing one side to "talk" and "hear" using a textual messenger window instead of an actual phone while the other side speaks and hears as they would on a regular phone call. Nagish converts text to speech and speech to text in real time.

# Dependecies:
* Before running it is important to make some installations:
- pip3 install twilio
- pip install Flask
- pip install requests
- pip install pymessanger.bot
- pip install six

# How to run:
* Nagish must run on a public address. For testing purposes, we reccomend using ngrok to make a personal computer work as a web server.
* Once the server is set, we can run the flask app by typing python3 app.py. Then from another terminal we must also run python3 phone.py.
* To interact with a FB messanger, app.py must also have a private key of a FB page, and, some setup is also needed on the FB developers platform (providing the server address)
* Once everything is running, a user just need to sign up on our website, and call that phone number. The call will go directly to the fb messenger.
