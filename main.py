import os

LINE = "fix(self): 04:00 root cause was my 03:00 patch for my 02:00 patch; rolled back all three of us, kept the tests, disabled past-me."


def main() -> None:
    line = LINE
    assert 1 <= len(line) <= 200
    assert "\n" not in line and "\r" not in line
    assert line.strip() == line

    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    data = line.encode("utf-8")
    with open(output_path, "wb") as handle:
        handle.write(data)

    with open(output_path, "rb") as handle:
        written = handle.read()
    assert written == data
    assert not written.endswith(b"\n")


if __name__ == "__main__":
    main()
