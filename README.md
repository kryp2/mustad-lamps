# Mustad-lamps 0.1

Flask Web app with api to controll RGB lights on an Arduino based board. This project builds upon project delivery in IDG3750 at NTNU. Mustad lamps main purpose is to provide a user interface in the form of a **website** and at the same time a **restAPI** to control the color of lights.   

# Installation
It's recommended to use a virtual environment like venv or virtualenv

    python3 -m venv env
    source env/bin/activate

When you are in the right environment 

    git clone https://github.com/kryp2/mustad-lamps.git
    pip install -r requirements.txt
    flask start 

