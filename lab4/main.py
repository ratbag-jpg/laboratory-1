from lib_requests import use_requests
from lib_pandas import use_pandas
from lib_numpy import use_numpy
from lib_bs4 import use_bs4
from lib_colorama import use_colorama
from lib_rich import use_rich
from lib_pillow import use_pillow
from lib_jinja2 import use_jinja2
from lib_pydantic import use_pydantic
from lib_click import use_click

from builtin_math import use_math
from builtin_os import use_os
from builtin_random import use_random
from builtin_datetime import use_datetime
from builtin_json import use_json


def main():
    print("=== ЗАПУСК ЛАБОРАТОРНОЇ РОБОТИ №4 ===\n")

    print("--- СТОРОННІ БІБЛІОТЕКИ ---")
    use_requests()
    use_pandas()
    use_numpy()
    use_bs4()
    use_colorama()
    use_rich()
    use_pillow()
    use_jinja2()
    use_pydantic()
    use_click()

    print("\n--- ВБУДОВАНІ БІБЛІОТЕКИ ---")
    use_math()
    use_os()
    use_random()
    use_datetime()
    use_json()

    print("\n=== ВСІ ФУНКЦІЇ ВИКОНАНО УСПІШНО ===")


if __name__ == "__main__":
    main()