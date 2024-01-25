
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import  QRect
import requests
name = None
class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()


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
        capture_button.clicked.connect(self.display)
        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.connect)



    def display(self):
        if self.download():
            pass


    def download(self):
        global stats
        global name 
        try:
            pok = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.textbox.text()}")
            link = pok.json()["sprites"]["front_default"]
            stats = pok.json()["moves"][0]
            print(stats)
            image = requests.get(link)
            name = self.textbox.text()
            with open(f"pokimage/{self.textbox.text()}.png","wb") as f :
                f.write(image.content)
            self.labelpic.setGeometry(QRect(480, 50, 400, 250))
            self.labelpic.setPixmap(QPixmap(f"pokimage/{name}"))


   
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
        super().__init__()
        self.setFixedSize(850, 500)
        self.labelpok = QLabel("hello world",self)
        self.labelpok.setPixmap(QPixmap(f"pokimage/{name}.png"))
        self.labelpok.setGeometry(QRect(0,0,800,420))
        self.labelpok.setScaledContents(True)

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
