from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import random

qtcreator_file = "design.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class DesignWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DesignWindow, self).__init__()
        self.setupUi(self)
        self.img = None
        self.img_gray = None

        self.gradient = None

        self.Browse.clicked.connect(self.get_image)
        self.Validate.clicked.connect(self.apply_first_derivative)
        self.Validate_2.clicked.connect(self.compute_gradient_edges)
        self.Apply.clicked.connect(self.apply_laplacian)
        self.Apply_2.clicked.connect(self.apply_log)
        self.Apply_3.clicked.connect(self.apply_canny)



    def makeFigure(self, img, label):
        pixmap = self.cvToPixmap(img)
        label.setPixmap(pixmap)
        label.setScaledContents(True)

    def cvToPixmap(self, img_opencv):
        if len(img_opencv.shape) == 2:
            h, w = img_opencv.shape
            q_img = QtGui.QImage(img_opencv.data, w, h, w,QtGui.QImage.Format_Grayscale8)
        else:
            h, w, ch = img_opencv.shape
            q_img = QtGui.QImage(img_opencv.data, w, h, w * ch,QtGui.QImage.Format_RGB888)
        return QPixmap.fromImage(q_img)

    def get_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Choisir une image",
            "",
            "Images (*.jpg *.jpeg *.png)"
        )

        if file_path:
            self.img = cv2.imread(file_path)

            self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            #gray_bgr = cv2.cvtColor(self.img_gray, cv2.COLOR_GRAY2BGR)

            self.makeFigure( self.img_gray, self.GrayImg)

    def apply_first_derivative(self):
        if self.img_gray is None:
            return

        if self.Prewitt.isChecked():
            Hx = np.array([[-1, -1, -1],
                           [0, 0, 0],
                           [1, 1, 1]])
            Hy = np.array([[-1, 0, 1],
                           [-1, 0, 1],
                           [-1, 0, 1]])
        elif self.Sobel.isChecked():
            Hx = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])
            Hy = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])
        else:
            return

        gx = cv2.filter2D(self.img_gray, cv2.CV_64F, Hx)
        gy = cv2.filter2D(self.img_gray, cv2.CV_64F, Hy)

        mag = np.sqrt(gx**2 + gy**2)
        self.gradient = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX
                                      ).astype(np.uint8)

        self.makeFigure(self.gradient, self.FilteredImg)

    def compute_gradient_edges(self):
        if self.gradient is None:
            return

        try:
            t1 = int(self.Seuil1.text().strip())
            t2 = int(self.Seuil2.text().strip())

        except:
            t1, t2 = 100, 255

        print(t1,t2)

        _, binary = cv2.threshold(self.gradient, t1, t2, cv2.THRESH_BINARY)

        self.makeFigure(binary, self.SegmentedImg)

    def apply_laplacian(self):
        if self.img_gray is None:
            return

        lap = cv2.Laplacian(self.img_gray, cv2.CV_64F)
        lap = cv2.convertScaleAbs(lap)

        self.makeFigure(lap, self.LaplacienImg)

    def apply_log(self):
        if self.img_gray is None:
            return

        blur = cv2.GaussianBlur(self.img_gray, (5, 5), 0)
        log = cv2.Laplacian(blur, cv2.CV_64F)
        log = cv2.convertScaleAbs(log)

        self.makeFigure(log, self.LoGImg)

    def apply_canny(self):
        if self.img_gray is None:
            return

        edges = cv2.Canny(self.img_gray, 100, 200)

        self.makeFigure(edges, self.CannyImg)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignWindow()
    window.show()
    sys.exit(app.exec_())
