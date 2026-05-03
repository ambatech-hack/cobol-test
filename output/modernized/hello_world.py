class HelloWorld:
    """Legacy system program"""

    def __init__(self):
        self.message = "Hello, World!"
        self.counter = 0

    def display_message(self):
        """Displays the message"""
        print(self.message)

    def increment_counter(self):
        """Increments the counter and displays it"""
        self.counter += 1
        print(f"Counter: {self.counter}")


if __name__ == "__main__":
    try:
        app = HelloWorld()
        app.display_message()
        app.increment_counter()
    except Exception as e:
        print(f"Error: {e}")