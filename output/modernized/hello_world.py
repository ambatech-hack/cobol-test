class HelloWorld:
    """Legacy system program to display 'Hello, World!' and a counter."""

    def __init__(self):
        self.message = "Hello, World!"
        self.counter = 0

    def main_logic(self):
        """Displays the message and calls the display_counter method."""
        print(self.message)
        self.display_counter()

    def display_counter(self):
        """Increments the counter and displays its value."""
        # 
        self.counter += 1
        print(f"Counter: {self.counter}")


if __name__ == "__main__":
    try:
        hello_world = HelloWorld()
        hello_world.main_logic()
    except Exception as e:
        print(f"Error: {e}")