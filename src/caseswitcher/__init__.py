__all__ = ("to_camel", "to_pascal", "to_slug", "to_snake", "to_title")


def to_camel(string: str) -> str:
    return string


def to_pascal(string: str) -> str:
    return string


def to_slug(string: str) -> str:
    return string


def to_snake(string: str) -> str:
    return string


def to_title(string: str) -> str:
    return string


# def to_snake_case(string: str) -> str:
#     return re.sub(r"(?<!^) ?([A-Z])", r"_\1", string).lower().replace("-", "_")
#
#
# def to_pascal_case(string: str, preserve_all_caps: bool = True) -> str:
#     string = string.replace("-", " ")
#     string = string.replace("_", " ")
#     return "".join(s[0].upper() + s[1:] for s in string.split(" "))
#
#
# def to_camel_case(string: str, preserve_all_caps: bool = True) -> str:
#     # string = (
#     #     re.sub(r"([A-Z])", r"_\1", string) if r.search(r"[A-Z]", string) else string
#     # )
#     # string = string.title().replace("_", "")
#     # if len(string) > 0:
#     #     string = string[0].lower() + string[1:]
#     # return string
#     words = _get_words(string, preserve_all_caps)
#     if len(words) > 0:
#         return words[0].lower() + "".join(words[1:])
#
#
# def _get_words(string: str, preserve_all_caps: bool, recur: bool = True) -> list[str]:
#     if preserve_all_caps:
#         # words = re.split(r"\b|([A-Z](?![A-Z])[A-Za-z]+)", string)
#         words = re.split(r"\b|([a-z](?=[A-Z]))", string)
#     else:
#         words = re.split(r"\b|([A-Z])", string)
#     words = [w for w in words if w and w not in [" ", "-", "_"]]
#
#     if not recur:
#         return words
#     return words
#     # recursive_words = _get_words("".join(words), preserve_all_caps, False)
#     # if words == recursive_words:
#     #     return words
#     # return _get_words("".join(words), preserve_all_caps)
#
#
# # print(_get_words("Coffee DB Sushi", True))
# print(_get_words("CoffeeDBSushi", True))
# # print(_get_words("Coffee_DB-Sushi", True))
# # assert _get_words("Coffee DB Sushi", True) == ["Coffee", "DB", "Sushi"]
# # assert _get_words("Coffee_DB-Sushi", True) == ["Coffee", "DB", "Sushi"]
