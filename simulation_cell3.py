# simulation.py

import random
from PySide6.QtCore import QObject, QTimer
from PySide6.QtWidgets import QVBoxLayout, QMessageBox
import pyqtgraph as pg
import pygame

class Simulation3(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        pygame.mixer.init()
        self.temperature_cell_1 = 20.0
        self.oxygen_room_1 = 20.0
        temp_high_duration = 10
        oxygen_low_duration = 10
        # Параметры для временных изменений
        self.temp_high_duration = temp_high_duration  # Время, в течение которого температура будет высокой
        self.oxygen_low_duration = oxygen_low_duration  # Время, в течение которого уровень кислорода будет низким

        # Состояние флагов
        self.high_temp_mode = False
        self.low_oxygen_mode = False
        self.allow_critical_states = False  # Флаг для разрешения критических состояний
        self.is_audio_on_3 = False

        # Таймер для разрешения критических состояний
        self.start_timer = QTimer()
        self.start_timer.setSingleShot(True)
        self.start_timer.timeout.connect(self.enable_critical_states)
        self.start_timer.start(5000)  # 5 секунд задержки

        # Создаем таймер для обновления симуляции
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)
        self.timer.start(1000)  # обновление каждые 1000 мс

        # Таймеры для отдельных состояний
        self.temp_timer = QTimer()
        self.temp_timer.setSingleShot(True)
        self.oxygen_timer = QTimer()
        self.oxygen_timer.setSingleShot(True)

        # таймер до запекания экипажа
        # Инициализация таймера
        self.timer_critical_temperature = QTimer()
        self.timer_critical_temperature.setSingleShot(True)  # Таймер сработает один раз
        self.timer_critical_temperature.timeout.connect(self.check_temperature)  # Подключаем сигнал таймера к функции

        # Запускаем таймер
        self.timer_critical_temperature.start(15000)  # 15000 миллисекунд = 15 секунд

        # таймер до удушья экипажа
        self.timer_critical_oxygen = QTimer()
        self.timer_critical_oxygen.setSingleShot(True)  # Таймер сработает один раз
        self.timer_critical_oxygen.timeout.connect(self.check_oxygen)  # Подключаем сигнал таймера к функции

        # Запускаем таймер
        self.timer_critical_oxygen.start(15000)  # 15000 миллисекунд = 15 секунд

        # Соединяем таймеры с методами
        #self.temp_timer.timeout.connect(self.reset_temperature_mode)
        #self.oxygen_timer.timeout.connect(self.reset_oxygen_mode)

        # Создание графика 1 в QWidget
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('#6f6866')
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.main_window.ui.widget_graphic_3.setLayout(layout)


        self.data = {
            'temperature_cell_1': [],
            'oxygen_room_1': []
        }

    def check_temperature(self):
        if self.temperature_cell_1 >=40:
            self.show_warning_dialog()

    def check_oxygen(self):
        if self.oxygen_room_1 <=17:
            self.show_warning_dialog()

    def show_warning_dialog(self):
        """Показывает предупреждение в виде диалогового окна."""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("Экипаж погиб.")
        msg_box.setWindowTitle("Предупреждение")
        msg_box.setStandardButtons(QMessageBox.Ok)
        response = msg_box.exec()
        if response == QMessageBox.Ok:
            print("Game Over!")
            self.main_window.close()

    #Проигрывание mp3 для тревоги
    def play_audio_3(self, file_path):
        """Проигрывает MP3 файл."""
        if self.is_audio_on_3:
            pygame.mixer.music.stop()  # Останавливаем, если что-то уже играет

        pygame.mixer.music.load(file_path)  # Загружаем файл
        pygame.mixer.music.play()  # Начинаем воспроизведение
        self.is_audio_on_3 = True  # Устанавливаем, что аудио на данный момент играет

    def stop_audio_3(self):
        """Останавливает воспроизведение"""
        pygame.mixer.music.stop()  # Останавливаем воспроизведение
        self.is_audio_on_3 = False  # Устанавливаем, что аудио не играет

    def update_graph(self):
        self.plot_widget.clear()
        self.plot_widget.setBackground('#6f6866')

        x = range(len(self.data['temperature_cell_1']))

        # Добавляем графики
        cell_1_temperature_plot = self.plot_widget.plot(x, self.data['temperature_cell_1'], pen='b',
                                                        name='Текущая температура (°С)')
        cell_1_oxygen_level_plot = self.plot_widget.plot(x, self.data['oxygen_room_1'], pen='r',
                                                         name='Уровень кислорода (%)')

        # Настройка графика
        self.plot_widget.setTitle("Температура и уровень кислорода в отсеке 3", color='w')  # Цвет заголовка
        self.plot_widget.setLabel('left', 'Значение', color='w')  # Цвет текста оси Y
        self.plot_widget.setLabel('bottom', 'Время (сек)', color='w')  # Цвет текста оси X

        # Изменение цвета осей
        self.plot_widget.getAxis('left').setPen(pg.mkPen('w'))  # Цвет оси Y
        self.plot_widget.getAxis('bottom').setPen(pg.mkPen('w'))  # Цвет оси X

        # Установка цвета меток осей (значений)
        self.plot_widget.getAxis('left').setTextPen(pg.mkPen('w'))  # Цвет меток оси Y
        self.plot_widget.getAxis('bottom').setTextPen(pg.mkPen('w'))  # Цвет меток оси X

        # Создание легенды
        legend = pg.LegendItem()  # Создаем легенду
        legend.setParentItem(self.plot_widget.graphicsItem())  # Привязываем легенду к графику
        legend.addItem(cell_1_temperature_plot, '<span style="color: white;">Текущая температура (°С)</span>')
        legend.addItem(cell_1_oxygen_level_plot, '<span style="color: white;">Уровень кислорода (%)</span>')

        # Устанавливаем Z-значение для видимости легенды
        legend.setZValue(10)

        # Устанавливаем позицию легенды (смещение вправо на 10 пикселей)
        legend.setPos(150, 50)  # Измените эти значения по своему усмотрению

    def update_ui(self):
        # Например, если у вас есть QLabel для отображения температуры:
        self.main_window.ui.label_temperature_3.setText(str(f"{self.temperature_cell_1:.2f}"))
        self.main_window.ui.label_oxygen_3.setText(str(f"{self.oxygen_room_1:.2f}"))

    def enable_critical_states(self):
        self.allow_critical_states = True  # Разрешаем критические состояния

    def cell_one_simulation(self):
        # Плавные колебания температуры в обычном режиме
        if not self.high_temp_mode:
            fluctuation = random.uniform(-0.1, 0.1)
            self.temperature_cell_1 += fluctuation
            self.temperature_cell_1 = max(15.0, min(self.temperature_cell_1, 30.0))

        # Проверяем возможность перехода в режим высокой температуры
        if not self.high_temp_mode and self.allow_critical_states and random.random() < 0.1:
            self.high_temp_mode = True

        # Обновляем состояние при высокой температуре
        if self.high_temp_mode:
            if self.temperature_cell_1 < 40.0:
                self.temperature_cell_1 += 0.5
            else:
                self.temperature_cell_1 = 40.0
                self.temp_timer.start(self.temp_high_duration * 1000)

        # Проверяем возможность перехода в режим низкого уровня кислорода
        if not self.low_oxygen_mode and self.allow_critical_states and random.random() < 0.1:
            self.low_oxygen_mode = True
            # Мы не устанавливаем значение кислорода здесь, так как снижение будет плавным
            self.oxygen_timer.start(self.oxygen_low_duration * 1000)

        # Обновляем состояние при низком уровне кислорода
        if self.low_oxygen_mode:
            if self.oxygen_room_1 > 15.0:
                self.oxygen_room_1 -= 0.1  # Плавное снижение уровня кислорода
            else:
                self.oxygen_room_1 = 15.0  # Ограничиваем до 15

                # Обновление интерфейса
            self.update_ui()
        self.data['temperature_cell_1'].append(self.temperature_cell_1)
        self.data['oxygen_room_1'].append(self.oxygen_room_1)
            # Выводим текущее состояние в консоль
        print(f'Temperature: {self.temperature_cell_1:.2f} °C, Oxygen Level: {self.oxygen_room_1:.2f} %')

    def alarm_check_cell_1(self):
        if (self.oxygen_room_1 <= 17) or (self.temperature_cell_1 >= 38):
            self.main_window.ui.button_cell_3.setStyleSheet("background-color: rgba(217, 4, 41, 0.29); color: white; border-radius: 0px;")
            self.play_audio_3('sounds/alarm3.mp3')
        else:
            self.main_window.ui.button_cell_3.setStyleSheet("background-color: rgba(0, 166, 251, 0.42); color: white; border-radius: 0px;")
            if self.is_audio_on_3:
                self.stop_audio_3()

    #класс симуляции
    def update_simulation(self):
        self.cell_one_simulation()
        self.update_ui()
        self.alarm_check_cell_1()
        self.update_graph()

    def reset_temperature_mode(self):
        self.high_temp_mode = False  # Выключаем режим высокой температуры
        self.temperature_cell_1 = random.uniform(20.0, 30.0)  # Вернуться к норме
        print(f'Temperature reset to: {self.temperature_cell_1:.2f} °C')
        if self.is_audio_on_3:
            self.stop_audio_3()


    def reset_oxygen_mode(self):
        self.low_oxygen_mode = False  # Выключаем режим низкого уровня кислорода
        self.oxygen_room_1 = random.uniform(20.0, 21.0)  # Вернуться к норме
        self.main_window.ui.button_cell_1.setStyleSheet("background-color: rgba(0, 166, 251, 0.42); color: white; border-radius: 0px;")
        print(f'Oxygen level reset to: {self.oxygen_room_1:.2f} %')
        if self.is_audio_on_3:
            self.stop_audio_3()

    def enable_critical_oxygen(self):
        self.allow_critical_states = True
        self.low_oxygen_mode = True

    def enable_critical_temperature(self):
        self.allow_critical_states = True
        self.high_temp_mode = True
