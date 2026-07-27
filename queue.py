from queue import Queue
import random


class Client:
    def __init__(self, request_id, name):
        self.request_id = request_id
        self.name = name
        self.operations = random.randint(1, 5)


class Bank:
    def __init__(self):
        self.clients = Queue()
        self.next_request_id = 1

    def generate_request(self, name):
        names = ["Alice", "Bob", "Charlie", "David", "Eve"]
        name = random.choice(names)

        client = Client(
            request_id=self.next_request_id,
            name=name
        )

        self.next_request_id +=1
        self.clients.put(client)

        print (
            f"Request #{client.request_id} generated for {client.name} with {client.operations} operations."
        )

    def process_request(self):
        if not self.clients.empty():
            client = self.clients.get()

            print(
                f"Processing request #{client.request_id} "
                f"for {client.name} with "
                f"{client.operations} operations."
            )
        else:
            print("No clients in the queue.")

bank = Bank()

while True:
    print("\nChoose an action:")
    print("1 — Generate a request")
    print("2 — Process a request")
    print("3 — Exit")

    choice = input("Your choice: ")

    if choice == "1":
        bank.generate_request()
    elif choice == "2":
        bank.process_request()
    elif choice == "3":
         print("Program finished")
         break
    else:
        print("Invalid choice.")
