from collections import deque

d = deque()


def solve(data):
    normalized_data = data.lower().replace(" ", "")
    characters = deque(normalized_data)

    while len(characters) > 1:
        left_characters = characters.popleft()
        right_characters = characters.pop()

        if left_characters != right_characters:
            return False

    return True


print(solve("level"))
print(solve("Level"))
characters = deque(["l", "e", "v", "e", "l"])
print(solve("python"))
