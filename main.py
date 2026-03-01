import sys
import PyQt6.QtWidgets as Widgets
import random

from PyQt6.QtCore import Qt

# [ Main Window Functions ]
# backend functions for the MainWindow class
class MainWindowFunctions:
        def getRandomOctet(self) -> tuple[int, int, int, int]: 
                result = []
                for i in range(4):
                        randomResult = random.randint(0, 255)
                        result.append(randomResult)

                return tuple(result[0:4])
        
        # IP Builder
        # Takes a list of octets and builds an IP address string
        # Example:
        # octets = [192, 168, 1, 1]
        # returns 192.168.1.1
        def ipBuilder(self, octets: list[int]) -> str:
                result = str()
                for index, octet in enumerate(octets):
                        if index != 3:
                                result += f'{octet}.'
                        else:
                                result += f'{octet}'
                return result
        

        # [ Randomize Button Function ]
        def randomize(self, MainWindow):
                        MainWindow.octet1, MainWindow.octet2, MainWindow.octet3, MainWindow.octet4 = self.getRandomOctet()
                        MainWindow.subnetMask = random.randint(1, 32)
                        MainWindow.refreshUI()
        
        # [ Calculate Button Function ]
        # Network Address 
        # Broadcast Address
        # Subnet Mask
        def calculate(self, MainWindow):
                octets = [MainWindow.octet1, MainWindow.octet2, MainWindow.octet3, MainWindow.octet4]
                networkAddress= str()
                broadcastAddress = str()
                subnetMaskResult = str()

                # Subnet Mask
                octetSubLevelArr = [128, 192, 224, 240, 248, 252, 254, 255]
                octetLevel = MainWindow.subnetMask // 8
                octetLevels = []
                octetSubLevel = MainWindow.subnetMask % 8


                for i in range(4):
                        if i < octetLevel:
                                octetLevels.append(255)
                        elif i == octetLevel:
                                octetLevels.append(octetSubLevelArr[octetSubLevel - 1])
                        else:
                                octetLevels.append(0)
                MainWindow.subnetMaskResult = self.ipBuilder(octetLevels)
                print(f'Subnet Mask: {MainWindow.subnetMaskResult}')

                # Network Address
                networkAddressOctets = []
                MainWindow.networkAddress = ''
                for i in range(4):
                        if octetLevels[i] == 255:
                                networkAddressOctets.append(octets[i])
                        else:
                                networkAddressOctets.append(octets[i] & octetLevels[i])
                MainWindow.networkAddress = self.ipBuilder(networkAddressOctets)
                print(f'Network Address: {MainWindow.networkAddress}')

                # Broadcast Address
                broadcastAddressOctets = []
                MainWindow.broadcastAddress = ''
                for i in range(4):
                        if octetLevels[i] == 255:
                                broadcastAddressOctets.append(octets[i])
                        else:
                                broadcastAddressOctets.append(octets[i] | (255 - octetLevels[i]))
                MainWindow.broadcastAddress = self.ipBuilder(broadcastAddressOctets)
                print(f'Broadcast Address: {MainWindow.broadcastAddress}')

                
                MainWindow.refreshUI()

# [ Main Window ]
# UI Elements
class MainWindow(Widgets.QWidget):

        def __init__(self):
              super().__init__()
              self.functions = MainWindowFunctions()
        
              # Initialize the main window
              self.setWindowTitle("Subnet Trainer")
              self.setLayout(Widgets.QVBoxLayout())
              
              # Children of the main window
              self.UIVariables()
              self.InitializeUI()
        
        def InitializeUI(self):
                self.UI()

        def UIVariables(self):
                self.octet1, self.octet2, self.octet3, self.octet4 = self.functions.getRandomOctet()
                self.subnetMask = random.randint(1, 32)
                self.networkAddress = str()
                self.broadcastAddress = str()
                self.subnetMaskResult = str()

        def UI(self):
                # Header Display
                label = Widgets.QLabel("Welcome to the Subnet Trainer!")
                label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                self.layout().addWidget(label)

                # Subnet Display
                ipAddressLabel = Widgets.QLabel(f"ip address: {self.octet1}.{self.octet2}.{self.octet3}.{self.octet4}/{self.subnetMask}")
                ipAddressLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
                self.layout().addWidget(ipAddressLabel)

                # Network Address
                networkAddressLabel = Widgets.QLabel(f'Network Address: {self.networkAddress}')
                networkAddressLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
                self.layout().addWidget(networkAddressLabel)

                # Broadcast Address
                broadcastAddressLabel = Widgets.QLabel(f'Broadcast Address: {self.broadcastAddress}')
                broadcastAddressLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
                self.layout().addWidget(broadcastAddressLabel)

                # Mask Display
                subnetMaskLabel = Widgets.QLabel(f'Subnet Mask: {self.subnetMaskResult}')
                subnetMaskLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
                self.layout().addWidget(subnetMaskLabel)

                # Buttons Layout
                HButtonLayout = Widgets.QHBoxLayout()
                
                # [Random Button]
                randomButton = Widgets.QPushButton('Randomize')
                randomButton.clicked.connect(lambda: self.functions.randomize(self))

                # [Calculate Button]
                calculateButton = Widgets.QPushButton("Calculate")
                calculateButton.clicked.connect(lambda: self.functions.calculate(self))

                HButtonLayout.addWidget(randomButton)
                HButtonLayout.addWidget(calculateButton)
                self.layout().addLayout(HButtonLayout)

        

        # [Layouts]
        def clearLayout(self, layout):
                while layout.count():
                        child = layout.takeAt(0)
                        widget = child.widget()
                        if widget:
                                widget.deleteLater()
                        elif child.layout():
                                self.clearLayout(child.layout())

        def refreshUI(self):
                self.clearLayout(self.layout())
                self.InitializeUI()

def main():
        app = Widgets.QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(app.exec())