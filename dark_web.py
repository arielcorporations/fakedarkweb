import sys
import os
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QPixmap, QIcon

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Dark Web")
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowIcon(QIcon("logo.png"))  # Set the app icon

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.browser = QWebEngineView()
        self.tabs.addTab(self.browser, "Google")
        self.browser.setUrl("https://www.google.com")

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.add_tab_button = QPushButton("+")
        self.add_tab_button.clicked.connect(self.add_new_tab)

        self.info_button = QPushButton()
        self.info_button.setIcon(QIcon("info.png"))  # Set the info icon
        self.info_button.clicked.connect(self.open_info_page)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.url_bar)
        self.layout.addWidget(self.info_button)
        self.layout.addWidget(self.add_tab_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.layout)
        self.main_layout.addWidget(self.tabs)

        self.container = QWidget()
        self.container.setLayout(self.main_layout)

        self.setCentralWidget(self.container)

    def navigate_to_url(self):
        url = self.url_bar.text()
        current_browser = self.tabs.currentWidget()
        if not url.startswith("http://") and not url.startswith("https://"):
            if "." in url:
                url = "http://" + url
            else:
                url = "https://www.google.com/search?q=" + url
        current_browser.setUrl(url)

    def add_new_tab(self):
        new_browser = QWebEngineView()
        self.tabs.addTab(new_browser, "New Tab")
        self.tabs.setCurrentWidget(new_browser)
        new_browser.setUrl("https://www.google.com")

    def close_current_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.browser.setUrl("about:blank")

    def open_info_page(self):
        current_tab_title = self.tabs.tabText(self.tabs.currentIndex())
        if current_tab_title == "New Tab":
            self.load_info_page(self.tabs.currentWidget())
        else:
            new_browser = QWebEngineView()
            self.tabs.addTab(new_browser, "Info")
            self.tabs.setCurrentWidget(new_browser)
            self.load_info_page(new_browser)

    def load_info_page(self, browser):
        info_url = "file:///info.html"  # Update this path to your info.html location
        browser.setUrl(info_url)

    def show_explosion_effect(self):
        # Create a new tab to display the explosion effect
        explosion_browser = QWebEngineView()
        self.tabs.addTab(explosion_browser, "Explosion")
        self.tabs.setCurrentWidget(explosion_browser)
        # Load the HTML file
        explosion_url = "file:///explosion.gif"  # Path to your explosion.html file
        explosion_browser.setUrl(explosion_url)
        # Set a timer to close this tab after the GIF is finished
        QTimer.singleShot(5000, lambda: self.tabs.removeTab(self.tabs.indexOf(explosion_browser)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec())