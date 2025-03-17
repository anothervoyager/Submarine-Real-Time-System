import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtCore import QTimer
#импорт gui интерфейса
from ui_main import Ui_MainWindow
#импорт класса с симуляцией
from simulation import Simulation
from simulation_cell2 import Simulation2
from simulation_cell3 import Simulation3
import pygame

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pygame.mixer.init()
        self.simulation = Simulation(self)
        self.simulation2 = Simulation2(self)
        self.simulation3 = Simulation3(self)

        #подключаем кнопки
        self.ui.button_add_oxygen.clicked.connect(self.button_add_oxygen_is_clicked)
        self.ui.button_cooling.clicked.connect(self.button_cooling_is_clicked)
        self.ui.button_critical_oxygen.clicked.connect(self.button_critical_oxygen_is_clicked)
        self.ui.button_critical_temp.clicked.connect(self.button_critical_temp_is_clicked)
        self.ui.button_easter_egg.clicked.connect(self.easter_egg)

    def play_mp3(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        # Запускаем таймер для проверки воспроизведения
        self.timer_egg = QTimer()
        self.timer_egg.timeout.connect(self.check_playing)
        self.timer_egg.start(100)  # Проверяем каждые 100 мс

    def check_playing(self):
        if not pygame.mixer.music.get_busy():
            self.timer_egg.stop()  # Остановить таймер, если музыка закончила воспроизведение

    def button_add_oxygen_is_clicked(self):
        self.simulation.reset_oxygen_mode()
        self.simulation2.reset_oxygen_mode()
        self.simulation3.reset_oxygen_mode()
        self.simulation.repair_expenses += 500
        self.simulation.expenses += 500
        self.simulation.oxygen_expenses += 500

    def button_cooling_is_clicked(self):
        self.simulation.reset_temperature_mode()
        self.simulation2.reset_temperature_mode()
        self.simulation3.reset_temperature_mode()
        self.simulation.repair_expenses += 240
        self.simulation.expenses += 240
        self.simulation.cooling_expenses += 240
    def button_critical_oxygen_is_clicked(self):
        self.simulation.enable_critical_oxygen()
        self.simulation2.enable_critical_oxygen()
        self.simulation3.enable_critical_oxygen()
    def button_critical_temp_is_clicked(self):
        self.simulation.enable_critical_temperature()
        self.simulation2.enable_critical_temperature()
        self.simulation3.enable_critical_temperature()
    def easter_egg(self):
        mp3_file = "sounds/sonar.mp3"
        self.play_mp3(mp3_file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())