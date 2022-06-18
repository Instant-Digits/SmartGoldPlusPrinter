1. Set up firm pi 3
   1. download the nood
   2. exract into the memory chip
   3. put it into pi and install it

install packages
sudo needed for globally install, not for in venv
can be install globally or venv
for venv
sudo pip install virtualenv virtualenvwrapper
virtualenv -p python3 venv

install the packegs for printer
sudo pip install Pillow python-printer-escpos

for firebase
sudo pip install pyrebase firebase

give the permition for printer and system
sudo chmod +x printer.py / systemStart.py

Adding to Auto start
sudo vim /etc/rc.local
add line
cd /home/printer && sudo python3 printer.py

    if in venv
        cd /home/printer && sudo python3 systemStart.py

Installing Printers
https://www.youtube.com/watch?v=jK3rFKajb_Q
sudo apt-get install cups -y
sudo usermod -a -G lpadmin pi /// user name
sudo cupsctl --remote-admin --remote-any --share-printers
sudo /etc/init.d/cups restart
ifconfig
visit localhost:631

for windows
to make exe 32 bit C:\Users\Next\AppData\Local\Programs\Python\Python36-32\Scripts\pyinstaller.exe .\main.py
copy the request library to dist/main/
run main.exe
