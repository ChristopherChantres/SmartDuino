# SmartDuino
### _A web LED controller_
![SmartDuino picture](https://i.ibb.co/mJ8rhHv/cpt-project-image.png)


**SmartDuino** is project that allows the connection between an Arduino UNO (running with firmata2) and a Django web server.

## How to start up the project?

**NOTE:** 
- Make sure you have Python installed in your computer.
- Connect the Arduino UNO to your computer.
- Connect pins digital pins _2...13_ to your LEDs  (You can use a breadboard).
![Arduino Diagram](https://i.ibb.co/G5kbfs4/cpt-tinkercad-image.png)
- Connect the ground to every LED .
- Compile & Upload Arduino UNO with the code provided when you start up the Arduino IDE:
	- Files > Examples > Firmata > StandardFirmata

1. Get this repository by cloning it into your desktop:
```
❯git clone https://github.com/ChristopherChantres/SmartDuino.git
```

2. Create a virtual environment and activate it (either Linux&MacOS or Windows):
```python
#Linux or MacOS
❯ python3 -m venv venv
# Activate the environment
$ source venv/bin/activate
# Windows
❯ py -m venv venv
❯ python3 -m venv venv
# Activate the environment
# In cmd.exe
❯ venv\Scripts\activate.bat
# In PowerShell
❯ venv\Scripts\Activate.ps1
```

3. Install the requirements.txt
```python
❯ pip install requirements.txt
```

4. Run the Django server:
```python
❯ python3 manage.py runserver
```

5. Click in the url provided:
```python
❯ http://127.0.0.1:8000/
```

### You can also host the web server in your Local Area Network
1. Get your private ip
2. Update the settings.py file _arduinoWeb > settings.py_ with the following:
- ALLOWED_HOSTS = ['*']
3. Run the server like this:
```python
# We are using the port 8000
❯  python3 manage.py runserver 0.0.0.0:8000
```

4. In your phone or any other device, type your private ip address followed by the port 8000:
```python
 # Example
❯ 10.123.145.167:8000
```
------------
Christopher Chantres&copy;