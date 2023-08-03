# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'encryptionvqIsCl.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(425, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(425, 300))
        MainWindow.setMaximumSize(QSize(425, 300))
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 0, 411, 271))
        self.encryption_page = QWidget()
        self.encryption_page.setObjectName(u"encryption_page")
        self.encrypt_text_box = QPlainTextEdit(self.encryption_page)
        self.encrypt_text_box.setObjectName(u"encrypt_text_box")
        self.encrypt_text_box.setGeometry(QRect(10, 30, 381, 91))
        self.label = QLabel(self.encryption_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 91, 16))
        self.encrypt_start = QPushButton(self.encryption_page)
        self.encrypt_start.setObjectName(u"encrypt_start")
        self.encrypt_start.setGeometry(QRect(310, 130, 75, 41))
        self.decrypt_start = QPushButton(self.encryption_page)
        self.decrypt_start.setObjectName(u"decrypt_start")
        self.decrypt_start.setGeometry(QRect(220, 130, 81, 41))
        self.decrypted_text = QPlainTextEdit(self.encryption_page)
        self.decrypted_text.setObjectName(u"decrypted_text")
        self.decrypted_text.setGeometry(QRect(10, 180, 381, 91))
        self.decrypted_text.setReadOnly(True)
        self.label_2 = QLabel(self.encryption_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 160, 91, 16))
        self.stackedWidget.addWidget(self.encryption_page)
        self.decryption_page = QWidget()
        self.decryption_page.setObjectName(u"decryption_page")
        self.stackedWidget.addWidget(self.decryption_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 425, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Text RSA Encryption", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Text to encrypt:", None))
        self.encrypt_start.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decrypt_start.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Decrypted text:", None))
    # retranslateUi

