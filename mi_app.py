import sys
from PyQt6.QtWidgets import QApplication, QDialog
from interfaz import Ui_Dialog

class MiVentana(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 
        self.num1 = 0
        self.op = ""

        #  NÚMEROS (AJUSTÁ SEGÚN TUS NOMBRES)
        self.ui.pushButton_16.clicked.connect(lambda: self.agregar("1"))
        self.ui.pushButton_18.clicked.connect(lambda: self.agregar("5"))
        self.ui.pushButton_19.clicked.connect(lambda: self.agregar("2"))
        self.ui.pushButton_20.clicked.connect(lambda: self.agregar("0"))
        self.ui.pushButton_8.clicked.connect(lambda: self.agregar("3"))
        self.ui.pushButton_4.clicked.connect(lambda: self.agregar("7"))
        self.ui.pushButton_7.clicked.connect(lambda: self.agregar("6"))
        self.ui.pushButton_5.clicked.connect(lambda: self.agregar("9"))
        self.ui.pushButton_3.clicked.connect(lambda: self.agregar("8"))
        self.ui.pushButton_15.clicked.connect(lambda: self.agregar("4"))
        self.ui.pushButton_9.clicked.connect(lambda: self.agregar(","))
     
    

        #  OPERACIONES 
        self.ui.pushButton_11.clicked.connect(lambda: self.operacion("+"))
        self.ui.pushButton_10.clicked.connect(lambda: self.operacion("-"))
        self.ui.pushButton_6.clicked.connect(lambda: self.operacion("*"))
        self.ui.pushButton_13.clicked.connect(lambda: self.operacion("/"))

        
        self.ui.pushButton_12.clicked.connect(self.resultado)

        #  BORRAR
        self.ui.pushButton_22.clicked.connect(self.borrar)

    #  AGREGAR NÚMERO
    def agregar(self, numero):
        texto = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(texto + numero)

    # ➕ GUARDAR OPERACIÓN
    def operacion(self, op):
        self.num1 = float(self.ui.lineEdit.text())
        self.op = op
        self.ui.lineEdit.clear()

    # 🟰 RESULTADO
    def resultado(self):
        num2 = float(self.ui.lineEdit.text())

        if self.op == "+":
            res = self.num1 + num2
        elif self.op == "-":
            res = self.num1 - num2
        elif self.op == "*":
            res = self.num1 * num2
        elif self.op == "/":
            res = self.num1 / num2

        self.ui.lineEdit.setText(str(res))

    # 🧹 BORRAR
    def borrar(self):
        self.ui.lineEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())