from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

from pytube import YouTube

from ..const import DOWNLOAD_LOGO

class Home(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.url = QLineEdit(self)
        self.url.setPlaceholderText("URL")
        self.url.setToolTip("Enter the url of the video.")
        
        self.download_button = QPushButton("Download", self)
        self.download_button.setToolTip("Click to download the video.")
        self.download_button.clicked.connect(self.download)

        self.root = QVBoxLayout()
        self.root.addWidget(self.url)
        self.root.addWidget(self.download_button)

        self.setWindowTitle("Youtube Downloader")
        self.setGeometry(400, 400, 400, 150)
        self.setWindowIcon(QIcon(DOWNLOAD_LOGO))
        self.setLayout(self.root)
        self.show()

    def download(self):
        yt = YouTube(self.url.text())
        yt.streams.filter(file_extension="mp4").get_by_resolution("720p").download("./output/")
        self.url.clear()