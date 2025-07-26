from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QFileDialog,
)


class MainWindow(QMainWindow):
    """
    Main application window for the Balatro Modding Tool.
    Provides UI elements for loading and managing Joker mods.
    """
    def __init__(self):
        """
        Initialize the main window, set up UI components and layout.
        """
        super().__init__()
        self.setWindowTitle("Balatro Modding Tool")  # Set window title

        # Main widget and layout
        central_widget = QWidget()  # Central widget for the window
        layout = QVBoxLayout()      # Vertical layout for UI elements

        # Example UI elements
        self.label = QLabel("Welcome! Load a Joker mod to begin.")  # Instruction label
        self.load_button = QPushButton("Load Joker File")            # Button to load Joker file
        self.load_button.clicked.connect(self.load_file)              # Connect button click to load_file method

        # Add UI elements to layout
        layout.addWidget(self.label)
        layout.addWidget(self.load_button)
        central_widget.setLayout(layout)  # Set layout for the central widget
        self.setCentralWidget(central_widget)  # Set central widget for the window

    def load_file(self):
        """
        Open a file dialog to load a Joker mod file.
        Update the label to show the loaded file path.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Joker JSON", "", "JSON Files (*.json)")
        if file_path:
            self.label.setText(f"Loaded: {file_path}")  # Update label with the loaded file path
