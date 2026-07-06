from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    count = initial_power

    def addpower(power_ammount: int) -> int:
        nonlocal count
        count += power_ammount
        return count
    return addpower


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str):
        enchanted_item = f"{enchantment_type} {item_name}"
        return enchanted_item
    return enchant


def memory_vault() -> dict[str, Callable]:
    memoire: dict[Callable, Callable] = {}

    def store(key, value):
        memoire[key] = value

    def recall(key):
        return memoire.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    base = spell_accumulator(100)
    print(f"Base 100, add 20: {base(20)}")
    print(f"Base 100, add 30: {base(30)}")
    print("\nTesting enchantment factory...")
    enchant1 = enchantment_factory("Flaming")
    enchant2 = enchantment_factory("Frozen")
    print(enchant1("Sword"))
    print(enchant2("Shield"))
    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault['store']("secret", 42)
    print(f"Recall 'secret': {vault['recall']("secret")}")
    print(f"Recall 'unknown': {vault['recall']("unknown")}")
