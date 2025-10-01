from collections.abc import Callable, Iterator, Generator, AsyncGenerator

def run(func: Callable[[str, int], str], num: int) -> str:
    char: str = 'Tema'
    result: str = func(char,num)
    print(result)

def multiply_text(text: str, amount: int):
    return text * amount


run(func = multiply_text, num= 10)

# Alternative below using lambda function

run(func=lambda text, num:multiply_text(text, 10), num= 10)









   