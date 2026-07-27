# Queue and Deque in Python

This repository demonstrates how to use **Queue** and **deque** in Python. It includes examples of implementing the **FIFO (First In, First Out)** principle for request processing and explains the differences between `queue.Queue` and `collections.deque`.

## 📌 Features

- Simulate a request processing system using `Queue`
- Generate and process requests in FIFO order
- Learn the difference between `Queue` and `deque`

## 🛠 Requirements

- Python 3.10+ (or any modern Python 3 version)

No additional packages are required because both modules are part of Python's standard library.

## 📂 Project Structure

```text
.
├── queue_example.py
├── deque_example.py
└── README.md
```

## 📖 Queue

`Queue` is imported from the `queue` module.

```python
from queue import Queue
```

A queue follows the **FIFO (First In, First Out)** principle.

The first request added to the queue is the first one processed.

### Available Actions

| Option | Description |
|---------|-------------|
| **1 — Generate a request** | Creates a new client request and adds it to the queue. |
| **2 — Process a request** | Removes the first request from the queue and processes it. |
| **3 — Exit** | Stops the program. |

### Queue Operations Used

| Method | Description |
|---------|-------------|
| `Queue()` | Creates an empty queue. |
| `put(item)` | Adds a new request to the queue. |
| `get()` | Removes and returns the first request in the queue. |
| `empty()` | Checks whether the queue is empty. |

---

## 📖 Deque

`deque` is imported from the `collections` module.

```python
from collections import deque
```

A deque (**double-ended queue**) allows adding and removing elements from both the left and right sides.

### 📖 How It Works

Convert the input string to lowercase.
Remove all spaces.
Store the characters in a deque.
Compare the first and last characters.
If they are different, return False.
Continue until all character pairs have been checked.
If all pairs match, return True.
