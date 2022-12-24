import strgen

if __name__ == "__main__":
    random_str = strgen.StringGenerator(
        "[\w\p]{20}").render()

    print(random_str)
