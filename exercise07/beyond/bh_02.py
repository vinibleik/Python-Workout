import re


def remove_authors_from_file(path: str, authors: list[str]) -> str:
    filename, *ext = path.split(".")
    file_output_name = f"{filename}_out.{'.'.join(ext)}"
    regex = re.compile("|".join(authors), flags=re.IGNORECASE)
    with open(path, "r") as file_input, open(file_output_name, "w") as file_output:
        for line in file_input:
            file_output.write(regex.sub("_", line))
    return file_output_name


if __name__ == "__main__":
    out = remove_authors_from_file("paper.txt", ["are", "you", "and"])
    with open(out) as f:
        for line in f:
            print(line, end="")
