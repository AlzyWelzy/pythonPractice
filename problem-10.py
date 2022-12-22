import os


def isBinod(item):
    global allBinod
    with open(item) as f:
        binod = f.read()
        if "binod" in binod.lower():
            print(f"Binod is found in {item}.")
            allBinod += 1
        else:
            print(f"No Binod in {item}.")


if __name__ == "__main__":
    allBinod = 0
    dir_contents = os.listdir()
    print(dir_contents)

    for item in dir_contents:
        if item.endswith("txt"):
            isBinod(item)

    print(f"We found a total of {allBinod} Binod.")
