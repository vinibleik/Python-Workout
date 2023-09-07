from collections import defaultdict


# find the word with the greatest number of repeated vowels.
def most_repeated_vowels(words: list[str]):
    def get_nvowels(word: str):
        return sum(letter in "aeiou" for letter in word.lower())

    return max(words, default="", key=get_nvowels)


# Write a program to read /etc/passwd on a Unix computer.
# The first field contains the username, and the final field contains
# the user's shell, the command interpreter. Display the shells in drecreasing
# order of popularity, such that the most popular shell is shown first.
def sort_shell_commands():
    shell_commands = defaultdict(int)

    with open("/etc/passwd", mode="r") as file:
        for line in file:
            command = line.split(":")[-1].strip()
            shell_commands[command] += 1

    return sorted(
        shell_commands, key=lambda command: shell_commands[command], reverse=True
    )


if __name__ == "__main__":
    print(sort_shell_commands())
