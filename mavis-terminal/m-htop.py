# Englisch | Peharge: This source code is released under the MIT License.
#
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private and commercial purposes.
# However, it is recommended to modify the code only if you have sufficient programming knowledge,
# as changes could cause unintended errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required for functionality.
# It is strongly recommended to perform installation and configuration in an isolated environment
# (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other issues
# that may arise directly or indirectly from the use, modification, or redistribution of the code.
#
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
#
# Nutzungsrechte:
# Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
# Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
# Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
# da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
#
# Abhängigkeiten und zusätzliche Frameworks:
# Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
# Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
# Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
# um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
#
# Haftungsausschluss:
# Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
# Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
# die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
#
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

# Français | Peharge: Ce code source est publié sous la licence MIT.
#
# Droits d'utilisation:
# Le code source peut être copié, édité et adapté aux besoins individuels.
# Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
# Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
# car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
#
# Dépendances et frameworks supplémentaires:
# Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
# Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
# Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
# pour éviter d'éventuels conflits avec les installations de logiciels existantes.
#
# Clause de non-responsabilité:
# L'utilisation du code est entièrement à vos propres risques.
# Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
# pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
#
# Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

import sys
import os
import psutil
import subprocess
from collections import deque

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QFrame, QLabel, QProgressBar,
    QTableWidget, QTableWidgetItem, QHeaderView, QScrollArea, QLineEdit, QPushButton, QMenu, QMessageBox, QComboBox, QPlainTextEdit
)
from PyQt6.QtCore import QTimer, Qt, QPoint
from PyQt6.QtGui import QIcon, QPainter

# For charts (requires PyQt6.QtCharts)
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis


class AdvancedSystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS System Monitor")
        self.setGeometry(100, 100, 1200, 750)
        self.setStyleSheet(self.get_stylesheet())

        # Dynamically set the application icon
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)

        # Mode selector: Overview, CPU Chart, RAM Chart, SSD Chart, System Info
        mode_layout = QHBoxLayout()
        self.mode_selector = QComboBox()
        self.mode_selector.addItems([
            "Overview",
            "CPU diagram",
            "RAM diagram",
            "SSD diagram",
            "System Info"
        ])
        self.mode_selector.currentIndexChanged.connect(self.switch_mode)
        mode_layout.addWidget(QLabel("Mode:"))
        mode_layout.addWidget(self.mode_selector)
        mode_layout.addStretch()
        main_layout.addLayout(mode_layout)

        # Stacked widget to switch between views
        self.stacked_widget = QStackedWidget()
        self.overview_widget = self.create_overview_widget()
        self.cpu_chart_widget = self.create_cpu_chart_widget()
        self.ram_chart_widget = self.create_ram_chart_widget()
        self.ssd_chart_widget = self.create_ssd_chart_widget()
        self.system_info_widget = self.create_system_info_widget()

        self.stacked_widget.addWidget(self.overview_widget)    # index 0
        self.stacked_widget.addWidget(self.cpu_chart_widget)     # index 1
        self.stacked_widget.addWidget(self.ram_chart_widget)     # index 2
        self.stacked_widget.addWidget(self.ssd_chart_widget)     # index 3
        self.stacked_widget.addWidget(self.system_info_widget)   # index 4

        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

        # Timer for updates (every second)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)

        # Process filter list
        self.all_processes = []

        # Chart history queues (max 60 seconds)
        self.cpu_usage_history = deque(maxlen=60)
        self.ram_usage_history = deque(maxlen=60)
        self.ssd_usage_history = deque(maxlen=60)

    def get_stylesheet(self):
        # A modern dark mode stylesheet with accent colors
        return """
        QWidget {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
            color: #FFFFFF;
            font-family: 'Roboto', sans-serif;
            font-size: 14px;
        }
        
        QFrame.metricCard {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
            border: 1px solid #566573;
            border-radius: 12px;
            padding: 10px;
        }
        
        QFrame.metricCard:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
            border: 1px solid #778899;
        }
        
        QLabel.title {
            font-size: 16px;
            font-weight: bold;
            background: none;
        }
        
        QProgressBar {
            background-color: #222;
            border: none;
            height: 20px;
            border-radius: 10px;
        }
        
        QProgressBar::chunk {
            border-radius: 10px;
        }
        
        QLineEdit {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
            border: 1px solid #778899;
            border-radius: 5px;
            padding: 5px;
            color: #FFFFFF;
        }
        
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
            border: none;
            border-radius: 5px;
            padding: 5px 10px;
            color: #FFFFFF;
        }
        
        QPushButton:hover {
            background-color: #1c2833;
        }
        
        QTableWidget {
            background-color: #222;
            gridline-color: #566573;
        }
        
        QHeaderView::section {
            background-color: #2c3e50;
            padding: 4px;
            border: 1px solid #566573;
        }
        
        QScrollArea {
            border: none;
            background-color: transparent;
        }
        
        QScrollBar:vertical {
            background-color: transparent;  /* Hintergrund (Schiene) in transparent */
            width: 10px;
            border-radius: 5px;
        }
        
        QScrollBar::handle:vertical {
            background-color: #ffffff;  /* Schieber (Block) in Weiß */
            min-height: 20px;
            border-radius: 5px;
        }
        
        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            background: transparent;
        }
        
        QScrollBar::up-arrow:vertical,
        QScrollBar::down-arrow:vertical {
            background: transparent;
        }
        
        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {
            background: transparent;
        }
        
        QScrollBar:horizontal {
            background-color: transparent;  /* Auch der horizontale Balken in transparent */
            height: 10px;
            border-radius: 5px;
        }
        
        QScrollBar::handle:horizontal {
            background-color: #ffffff;
            min-width: 20px;
            border-radius: 5px;
        }
        
        QScrollBar::add-line:horizontal,
        QScrollBar::sub-line:horizontal {
            background: transparent;
        }
        
        QScrollBar::left-arrow:horizontal,
        QScrollBar::right-arrow:horizontal {
            background: transparent;
        }
        
        QScrollBar::add-page:horizontal,
        QScrollBar::sub-page:horizontal {
            background: transparent;
        }
        """

    def create_metric_card(self, title, color):
        """Creates a card widget for showing a metric with a label and a progress bar."""
        card = QFrame()
        card.setObjectName("metricCard")
        card.setProperty("class", "metricCard")
        layout = QVBoxLayout()
        layout.setSpacing(5)

        label = QLabel(title + ":")
        label.setObjectName("title")
        label.setProperty("class", "title")
        layout.addWidget(label)

        progress = QProgressBar()
        progress.setStyleSheet(f"QProgressBar::chunk {{ background-color: {color}; }}")
        layout.addWidget(progress)

        # Detail label for numeric values
        detail = QLabel("0")
        layout.addWidget(detail)

        card.setLayout(layout)

        # Save references depending on the metric title
        if title.startswith("CPU"):
            self.cpu_progress = progress
            self.cpu_detail = detail
        elif title.startswith("Memory"):
            self.mem_progress = progress
            self.mem_detail = detail
        elif title.startswith("Disk"):
            self.disk_progress = progress
            self.disk_detail = detail
        elif title.startswith("Network"):
            self.net_detail = detail

        return card

    def create_overview_widget(self):
        """Creates the overview screen with metrics, process filter, and process table."""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)

        # Upper metric cards
        metrics_layout = QHBoxLayout()
        metrics_layout.setSpacing(20)
        self.cpu_card = self.create_metric_card("CPU Usage", "#94bfff")
        self.mem_card = self.create_metric_card("Memory Usage", "#94bfff")
        self.disk_card = self.create_metric_card("Disk Usage", "#ffcc00")
        self.net_card = self.create_metric_card("Network", "#7ed321")
        metrics_layout.addWidget(self.cpu_card)
        metrics_layout.addWidget(self.mem_card)
        metrics_layout.addWidget(self.disk_card)
        metrics_layout.addWidget(self.net_card)
        layout.addLayout(metrics_layout)

        # Process filter bar
        filter_layout = QHBoxLayout()
        self.filter_input = QLineEdit()
        self.filter_input.setPlaceholderText("Filter process name...")
        self.filter_input.textChanged.connect(self.filter_processes)
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.update_metrics)
        filter_layout.addWidget(self.filter_input)
        filter_layout.addWidget(refresh_button)
        layout.addLayout(filter_layout)

        # Process table in a scroll area
        self.process_table = QTableWidget()
        self.process_table.setColumnCount(4)
        self.process_table.setHorizontalHeaderLabels(["PID", "Name", "CPU %", "Mem %"])
        self.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.process_table.setSortingEnabled(True)
        self.process_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.process_table.customContextMenuRequested.connect(self.process_table_menu)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.process_table)
        layout.addWidget(scroll_area)

        widget.setLayout(layout)
        return widget

    def create_cpu_chart_widget(self):
        """Creates the CPU chart view, displaying CPU usage over the past 60 seconds,
        with white text and a transparent background."""
        from PyQt6.QtGui import QBrush, QColor
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.cpu_series = QLineSeries()
        chart = QChart()
        chart.addSeries(self.cpu_series)
        chart.setTitle("CPU usage (last 60 seconds)")
        chart.legend().hide()

        # Set transparent background for the chart and plot area
        chart.setBackgroundVisible(False)
        chart.setPlotAreaBackgroundBrush(QBrush(Qt.GlobalColor.transparent))

        # Set the title brush to white
        chart.setTitleBrush(QBrush(QColor("white")))
        font_title = chart.titleFont()
        font_title.setPointSize(14)
        chart.setTitleFont(font_title)

        # X-Axis configuration with white labels and white title
        self.axis_x_cpu = QValueAxis()
        self.axis_x_cpu.setRange(0, 60)
        self.axis_x_cpu.setLabelFormat("%d")
        self.axis_x_cpu.setTitleText("seconds")
        self.axis_x_cpu.setLabelsColor(QColor("white"))
        self.axis_x_cpu.setTitleBrush(QBrush(QColor("white")))

        # Y-Axis configuration with white labels and white title
        self.axis_y_cpu = QValueAxis()
        self.axis_y_cpu.setRange(0, 100)
        self.axis_y_cpu.setTitleText("CPU %")
        self.axis_y_cpu.setLabelsColor(QColor("white"))
        self.axis_y_cpu.setTitleBrush(QBrush(QColor("white")))

        chart.addAxis(self.axis_x_cpu, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(self.axis_y_cpu, Qt.AlignmentFlag.AlignLeft)
        self.cpu_series.attachAxis(self.axis_x_cpu)
        self.cpu_series.attachAxis(self.axis_y_cpu)

        self.cpu_chart_view = QChartView(chart)
        self.cpu_chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Set the chart view background transparent
        self.cpu_chart_view.setStyleSheet("background: transparent;")
        layout.addWidget(self.cpu_chart_view)
        widget.setLayout(layout)
        return widget

    def create_ram_chart_widget(self):
        """Creates the RAM chart view, displaying RAM usage over the past 60 seconds,
        with white text and a transparent background."""
        from PyQt6.QtGui import QBrush, QColor
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.ram_series = QLineSeries()
        chart = QChart()
        chart.addSeries(self.ram_series)
        chart.setTitle("RAM usage (last 60 seconds)")
        chart.legend().hide()

        # Set transparent background for the chart and plot area
        chart.setBackgroundVisible(False)
        chart.setPlotAreaBackgroundBrush(QBrush(Qt.GlobalColor.transparent))

        # Set the title brush to white
        chart.setTitleBrush(QBrush(QColor("white")))
        font_title = chart.titleFont()
        font_title.setPointSize(14)
        chart.setTitleFont(font_title)

        # X-Axis configuration with white labels and white title
        self.axis_x_ram = QValueAxis()
        self.axis_x_ram.setRange(0, 60)
        self.axis_x_ram.setLabelFormat("%d")
        self.axis_x_ram.setTitleText("seconds")
        self.axis_x_ram.setLabelsColor(QColor("white"))
        self.axis_x_ram.setTitleBrush(QBrush(QColor("white")))

        # Y-Axis configuration with white labels and white title
        self.axis_y_ram = QValueAxis()
        self.axis_y_ram.setRange(0, 100)
        self.axis_y_ram.setTitleText("RAM %")
        self.axis_y_ram.setLabelsColor(QColor("white"))
        self.axis_y_ram.setTitleBrush(QBrush(QColor("white")))

        chart.addAxis(self.axis_x_ram, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(self.axis_y_ram, Qt.AlignmentFlag.AlignLeft)
        self.ram_series.attachAxis(self.axis_x_ram)
        self.ram_series.attachAxis(self.axis_y_ram)

        self.ram_chart_view = QChartView(chart)
        self.ram_chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Set the chart view background transparent
        self.ram_chart_view.setStyleSheet("background: transparent;")
        layout.addWidget(self.ram_chart_view)
        widget.setLayout(layout)
        return widget

    def create_ssd_chart_widget(self):
        """Creates the SSD chart view (using disk usage as SSD usage) over the past 60 seconds,
        with white text and a transparent background."""
        from PyQt6.QtGui import QBrush, QColor
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.ssd_series = QLineSeries()
        chart = QChart()
        chart.addSeries(self.ssd_series)
        chart.setTitle("SSD usage (last 60 seconds)")
        chart.legend().hide()

        # Set transparent background for the chart and plot area.
        chart.setBackgroundVisible(False)
        chart.setPlotAreaBackgroundBrush(QBrush(Qt.GlobalColor.transparent))

        # Set title color to white.
        chart.setTitleBrush(QBrush(QColor("white")))
        font_title = chart.titleFont()
        font_title.setPointSize(14)
        chart.setTitleFont(font_title)

        # X-Axis configuration with white labels and title.
        self.axis_x_ssd = QValueAxis()
        self.axis_x_ssd.setRange(0, 60)
        self.axis_x_ssd.setLabelFormat("%d")
        self.axis_x_ssd.setTitleText("seconds")
        self.axis_x_ssd.setLabelsColor(QColor("white"))
        self.axis_x_ssd.setTitleBrush(QBrush(QColor("white")))

        # Y-Axis configuration with white labels and title.
        self.axis_y_ssd = QValueAxis()
        self.axis_y_ssd.setRange(0, 100)
        self.axis_y_ssd.setTitleText("SSD %")
        self.axis_y_ssd.setLabelsColor(QColor("white"))
        self.axis_y_ssd.setTitleBrush(QBrush(QColor("white")))

        chart.addAxis(self.axis_x_ssd, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(self.axis_y_ssd, Qt.AlignmentFlag.AlignLeft)
        self.ssd_series.attachAxis(self.axis_x_ssd)
        self.ssd_series.attachAxis(self.axis_y_ssd)

        self.ssd_chart_view = QChartView(chart)
        self.ssd_chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Set the chart view background to be transparent.
        self.ssd_chart_view.setStyleSheet("background: transparent;")
        layout.addWidget(self.ssd_chart_view)
        widget.setLayout(layout)
        return widget

    def create_system_info_widget(self):
        """Creates the System Info view, displaying detailed hardware information."""
        widget = QWidget()
        layout = QVBoxLayout()

        self.info_text = QPlainTextEdit()
        self.info_text.setReadOnly(True)
        self.info_text.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626); color: #fff; border: none;")
        layout.addWidget(self.info_text)
        widget.setLayout(layout)
        self.update_system_info()  # Update system info upon initialization
        return widget

    def switch_mode(self, index):
        """Switches the active mode in the stacked widget."""
        self.stacked_widget.setCurrentIndex(index)
        if index == 1:
            self.update_cpu_chart()
        elif index == 2:
            self.update_ram_chart()
        elif index == 3:
            self.update_ssd_chart()
        elif index == 4:
            self.update_system_info()

    def update_metrics(self):
        """Updates all metrics and charts every second."""
        # CPU metrics
        cpu_usage = psutil.cpu_percent()
        self.cpu_progress.setValue(int(cpu_usage))
        self.cpu_detail.setText(f"{cpu_usage:.1f}%")
        self.cpu_usage_history.append(cpu_usage)

        # Memory metrics
        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        used_mem = mem.used / 1024**3
        total_mem = mem.total / 1024**3
        self.mem_progress.setValue(int(mem_percent))
        self.mem_detail.setText(f"{used_mem:.2f}GB / {total_mem:.2f}GB ({mem_percent}%)")
        self.ram_usage_history.append(mem_percent)

        # Disk metrics (considered SSD usage)
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        used_disk = disk.used / 1024**3
        total_disk = disk.total / 1024**3
        self.disk_progress.setValue(int(disk_percent))
        self.disk_detail.setText(f"{used_disk:.2f}GB / {total_disk:.2f}GB ({disk_percent}%)")
        self.ssd_usage_history.append(disk_percent)

        # Network metrics
        net = psutil.net_io_counters()
        self.net_detail.setText(f"Sent {net.bytes_sent/1024**2:.2f}MB / Recv {net.bytes_recv/1024**2:.2f}MB")

        # Update process list
        self.all_processes = list(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']))
        self.populate_process_table(self.all_processes)

        # Update current view charts/info
        current_mode = self.stacked_widget.currentIndex()
        if current_mode == 1:
            self.update_cpu_chart()
        elif current_mode == 2:
            self.update_ram_chart()
        elif current_mode == 3:
            self.update_ssd_chart()
        elif current_mode == 4:
            self.update_system_info()

    def update_cpu_chart(self):
        """Updates the CPU chart data."""
        self.cpu_series.clear()
        n = len(self.cpu_usage_history)
        start = 60 - n
        for i, usage in enumerate(self.cpu_usage_history):
            self.cpu_series.append(start + i, usage)

    def update_ram_chart(self):
        """Updates the RAM chart data."""
        self.ram_series.clear()
        n = len(self.ram_usage_history)
        start = 60 - n
        for i, usage in enumerate(self.ram_usage_history):
            self.ram_series.append(start + i, usage)

    def update_ssd_chart(self):
        """Updates the SSD chart data."""
        self.ssd_series.clear()
        n = len(self.ssd_usage_history)
        start = 60 - n
        for i, usage in enumerate(self.ssd_usage_history):
            self.ssd_series.append(start + i, usage)

    def populate_process_table(self, process_list):
        """Populates the process table with the top 20 processes by CPU usage."""
        sorted_procs = sorted(process_list, key=lambda p: p.info.get('cpu_percent', 0), reverse=True)[:20]
        self.process_table.setRowCount(len(sorted_procs))
        for row, proc in enumerate(sorted_procs):
            pid_item = QTableWidgetItem(str(proc.info.get('pid')))
            name_item = QTableWidgetItem(proc.info.get('name') or "N/A")
            cpu_item = QTableWidgetItem(f"{proc.info.get('cpu_percent', 0)}%")
            mem_item = QTableWidgetItem(f"{proc.info.get('memory_percent', 0):.2f}%")
            for item in (pid_item, cpu_item, mem_item):
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.process_table.setItem(row, 0, pid_item)
            self.process_table.setItem(row, 1, name_item)
            self.process_table.setItem(row, 2, cpu_item)
            self.process_table.setItem(row, 3, mem_item)

    def filter_processes(self):
        """Filters the processes based on the user's input in the filter box."""
        filter_text = self.filter_input.text().lower()
        filtered = self.all_processes if not filter_text else [
            p for p in self.all_processes if filter_text in (p.info.get('name') or "").lower()
        ]
        self.populate_process_table(filtered)

    def process_table_menu(self, pos: QPoint):
        """Shows a context menu for killing a process."""
        index = self.process_table.indexAt(pos)
        if not index.isValid():
            return
        menu = QMenu()
        kill_action = menu.addAction("Kill Process")
        action = menu.exec(self.process_table.viewport().mapToGlobal(pos))
        if action == kill_action:
            pid_item = self.process_table.item(index.row(), 0)
            if pid_item:
                pid = int(pid_item.text())
                self.kill_process(pid)

    def kill_process(self, pid):
        """Attempts to terminate a process and shows a result message box."""
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait(3)
            QMessageBox.information(self, "Success", f"Process {pid} was terminated.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error terminating process {pid}:\n{str(e)}")
        self.update_metrics()

    def update_system_info(self):
        """Gathers and displays detailed system information (RAM, SSD, Graphics) using WMIC."""
        info = []

        # RAM Information via WMIC (Windows-specific)
        try:
            ram_output = subprocess.check_output(["wmic", "MemoryChip", "get", "BankLabel,Capacity,Speed"], shell=True)
            ram_text = ram_output.decode("utf-8", errors="ignore").strip()
            info.append("RAM Information:")
            info.append(ram_text)
        except Exception as e:
            info.append("RAM Information: N/A (" + str(e) + ")")

        info.append("\n" + "-" * 50 + "\n")

        # Disk drive (SSD) Information via WMIC
        try:
            disk_output = subprocess.check_output(["wmic", "diskdrive", "get", "Model,MediaType,InterfaceType"], shell=True)
            disk_text = disk_output.decode("utf-8", errors="ignore").strip()
            info.append("SSD / DiskDrive Information:")
            info.append(disk_text)
        except Exception as e:
            info.append("DiskDrive Information: N/A (" + str(e) + ")")

        info.append("\n" + "-" * 50 + "\n")

        # Graphics Information via WMIC
        try:
            gfx_output = subprocess.check_output(["wmic", "path", "win32_VideoController", "get", "Name,AdapterRAM,DriverVersion"], shell=True)
            gfx_text = gfx_output.decode("utf-8", errors="ignore").strip()
            info.append("Graphics Information:")
            info.append(gfx_text)
        except Exception as e:
            info.append("Graphics Information: N/A (" + str(e) + ")")

        self.info_text.setPlainText("\n".join(info))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedSystemMonitor()
    window.show()
    sys.exit(app.exec())
