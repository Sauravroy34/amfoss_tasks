
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import  QRect
import requests
import os
p1 = 0
poki = []
name = None
class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()

        info = QLabel(self)
        self.w = None  
        self.q = None
        self.setFixedSize(850, 500)
        self.labelpic = QLabel(self)
        self.labelpic.setPixmap(QPixmap("assets/landing.jpg"))

        self.labelpic.setScaledContents(True)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)


 
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.download)
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capt)
        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.connect)
        self.info = QLabel("information",self)
        self.info.setGeometry(480,800,400,250) 


    def capt(self):
        pass




    def download(self):
        global name 
        try:
            pok = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.textbox.text()}")
            link = pok.json()["sprites"]["front_default"]

            name = pok.json()["forms"][0]["name"]
            sp_move = pok.json()["moves"][0]["move"]["name"]
            base_xp = pok.json()["base_experience"]
            weight = pok.json()["weight"]

            image = requests.get(link)
            name = self.textbox.text()
            with open(f"pokimage/{self.textbox.text()}.png","wb") as f :
                f.write(image.content)
            self.labelpic.setGeometry(QRect(480, 50, 400, 250))
            self.labelpic.setPixmap(QPixmap(f"pokimage/{name}"))

            self.info.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
            self.info.setText(f"{name}\n sp_move = {sp_move}\n base_xp = {base_xp}\n weight = {weight}")          
            self.info.setGeometry(480,250,400,250) 

            try:
                for  n,p,file in os.walk("pokimage"):
                    poki.append(file)
                print(poki[0])
            except:
                print("wrong")

            
   
            return True
        except:
            return True

    def connect(self,checked):
        if self.q == None:
            self.q = pok()

            self.q.show()


       
        
        

    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.


class pok(QWidget):

    def __init__(self):
        global p1
        super().__init__()
        self.setFixedSize(850, 500)
        self.what = QLabel(f"{name}",self)
        self.what.setGeometry(400,250,400,250)
        self.what.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")

        self.labelpok = QLabel("hello world",self)
        self.labelpok.setPixmap(QPixmap(f"pokimage/{name}.png"))

        enter_button = QPushButton("Previous", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.prev)

        enter_button = QPushButton("next", self)
        enter_button.setGeometry(640, 300, 160, 43)
        enter_button.clicked.connect(self.next)

        self.labelpok.setGeometry(QRect(0,0,800,420))
        self.labelpok.setScaledContents(True)
    def prev(self):
        global p1
        try:
            self.labelpok.setPixmap(QPixmap(f"pokimage/{poki[0][p1]}"))
            x = str(poki[0][p1].split(".png")[0])
            self.what.setText(x) 
            p1 = p1 - 1
        except:
            p1 = len(poki)
            self.labelpok.setPixmap(QPixmap(f"pokimage/{poki[0][p1]}"))
            x = str(poki[0][p1].split(".png")[0])
            self.what.setText(x)

    def next(self):
        global p1
        try:
            self.labelpok.setPixmap(QPixmap(f"pokimage/{poki[0][p1]}"))
            x = str(poki[0][p1].split(".png")[0])
            self.what.setText(x)
            p1 = p1 + 1
        except:
            p1 = 0
            self.labelpok.setPixmap(QPixmap(f"pokimage/{poki[0][p1]}"))
            x = str(poki[0][p1].split(".png")[0])
            self.what.setText(x)
            

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
