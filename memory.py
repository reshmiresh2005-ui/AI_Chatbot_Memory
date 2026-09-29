class ChatMemory:

    def __init__(self, max_messages=6):
        self.max_messages = max_messages
        self.history = []

    def add_message(self, message):
        self.history.append(message)

        # Sliding window / FIFO
        if len(self.history) > self.max_messages:
            self.history.pop(0)

    def show_memory(self):
        print("\n--- Current Memory ---")

        for message in self.history:
            print(message)

        print("----------------------\n")