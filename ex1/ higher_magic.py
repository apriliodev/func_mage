from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiply_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return multiply_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def maybe_cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return maybe_cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return cast_all


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def is_powerful(target: str, power: int) -> bool:
        return power >= 20

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined("Dragon", 20)
    print(f"Combined spell result: {result1}, {result2}")
    print()

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {10}, Amplified: {30}")
    print(mega_fireball("Dragon", 10))
    print()

    print("Testing conditional caster...")
    safe_fireball = conditional_caster(is_powerful, fireball)
    print(safe_fireball("Dragon", 25))
    print(safe_fireball("Dragon", 5))
    print()

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 15))
