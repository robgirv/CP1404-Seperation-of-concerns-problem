"""
CP1404 Seminar 08 - Group Task
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from product import Product


class ShoppingApp(App):
    """Main Program - Kivy program to shop."""

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        # Iteration 1 - Manual Data
        self.products = [Product("Cheese", 12.50), Product("Laptop", 912.95), Product("Plant", 4.75)]

    def build(self):
        """Build the Kivy GUI."""
        Window.size = 1000, 800
        self.title = "CP1404 Meetup"
        self.root = Builder.load_file("layout.kv")

    def create_widgets(self):
        for product in self.products:
            temp_button = Button(text=str(product))
            temp_button.bind(on_press=self.press_entry)
            temp_button.product = product
            self.root.ids.entries_box.add_widget(temp_button)
