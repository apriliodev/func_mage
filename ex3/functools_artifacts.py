from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        op_func = add
    elif operation == "multiply":
        op_func = mul
    elif operation == "max":
        op_func = max
    elif operation == "min":
        op_func = min
    else:
        raise ValueError("Unknown Operation")
    return reduce(op_func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchant = partial(base_enchantment, 50, "Fire")
    water_enchant = partial(base_enchantment, 50, "Water")
    earth_enchant = partial(base_enchantment, 50, "Earth")

    return {
        "fire": fire_enchant,
        "water": water_enchant,
        "earth": earth_enchant
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def process(value: Any) -> str:
        return "Unknown spell type"

    @process.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @process.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @process.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"
    return process


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    num: list[int] = [20, 25, 15, 40]
    print(f"Sum: {spell_reducer(num, "add")}")
    print(f"Product: {spell_reducer(num, "multiply")}")
    print(f"Max: {spell_reducer(num, "max")}")
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # print(f"CACHE: {memoized_fibonacci.cache_info()}")
    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    total: list[int] = [1, 2, 3]
    print(spell(42))
    print(spell("fireball"))
    print(spell(total))
    print(spell(1.0))
