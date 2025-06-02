from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from bot_core import BotCore

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tibia 7.4 Bot")
        self.setGeometry(100, 100, 800, 600)
        self.bot = BotCore()
        self._setup_ui()

    def _setup_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Tibia 7.4 Bot Interface")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        # Cavebot buttons
        self.cavebot_start_btn = QPushButton("Start Cavebot")
        self.cavebot_start_btn.clicked.connect(self.start_cavebot)
        layout.addWidget(self.cavebot_start_btn)

        self.cavebot_stop_btn = QPushButton("Stop Cavebot")
        self.cavebot_stop_btn.clicked.connect(self.stop_cavebot)
        layout.addWidget(self.cavebot_stop_btn)

        # Healing buttons
        self.healing_start_btn = QPushButton("Start Healing")
        self.healing_start_btn.clicked.connect(self.start_healing)
        layout.addWidget(self.healing_start_btn)

        self.healing_stop_btn = QPushButton("Stop Healing")
        self.healing_stop_btn.clicked.connect(self.stop_healing)
        layout.addWidget(self.healing_stop_btn)

        # Placeholder buttons for other features
        # Rune maker buttons
        self.rune_maker_start_btn = QPushButton("Start Rune Maker")
        self.rune_maker_start_btn.clicked.connect(self.start_rune_maker)
        layout.addWidget(self.rune_maker_start_btn)

        self.rune_maker_stop_btn = QPushButton("Stop Rune Maker")
        self.rune_maker_stop_btn.clicked.connect(self.stop_rune_maker)
        layout.addWidget(self.rune_maker_stop_btn)

        # Hotkey buttons
        self.hotkey_start_btn = QPushButton("Start Hotkey")
        self.hotkey_start_btn.clicked.connect(self.start_hotkey)
        layout.addWidget(self.hotkey_start_btn)

        self.hotkey_stop_btn = QPushButton("Stop Hotkey")
        self.hotkey_stop_btn.clicked.connect(self.stop_hotkey)
        layout.addWidget(self.hotkey_stop_btn)

        # Auto target buttons
        self.auto_target_follow_btn = QPushButton("Start Auto Target (Follow)")
        self.auto_target_follow_btn.clicked.connect(self.start_auto_target_follow)
        layout.addWidget(self.auto_target_follow_btn)

        self.auto_target_distance_btn = QPushButton("Start Auto Target (Keep Distance)")
        self.auto_target_distance_btn.clicked.connect(self.start_auto_target_distance)
        layout.addWidget(self.auto_target_distance_btn)

        self.auto_target_stop_btn = QPushButton("Stop Auto Target")
        self.auto_target_stop_btn.clicked.connect(self.stop_auto_target)
        layout.addWidget(self.auto_target_stop_btn)

        # Settings button
        layout.addWidget(QPushButton("Settings"))

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_cavebot(self):
        self.bot.start_cavebot()

    def stop_cavebot(self):
        self.bot.stop_cavebot()

    def start_healing(self):
        self.bot.start_healing()

    def stop_healing(self):
        self.bot.stop_healing()

    def start_rune_maker(self):
        self.bot.start_rune_maker()

    def stop_rune_maker(self):
        self.bot.stop_rune_maker()

    def start_hotkey(self):
        self.bot.start_hotkey()

    def stop_hotkey(self):
        self.bot.stop_hotkey()

    def start_auto_target_follow(self):
        self.bot.start_auto_target(follow_monster=True)

    def start_auto_target_distance(self):
        self.bot.start_auto_target(follow_monster=False)

    def stop_auto_target(self):
        self.bot.stop_auto_target()

    def start_healing(self):
        self.bot.start_healing()

    def stop_healing(self):
        self.bot.stop_healing()
