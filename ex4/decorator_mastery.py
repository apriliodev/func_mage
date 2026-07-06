import time
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power', args[-1])
            if power >= min_power:
                result = func(*args, **kwargs)
                return result
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Succesfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        return "Fireball cast!"
    result = fireball()
    print(f"Result: {result}")
    print()
    print("Testing retrying spell...")

    @retry_spell(3)
    def unstable_spell():
        raise ValueError("Spell fizzled")

    result = unstable_spell()
    print("Waaaaaaagh spelled !")
    print()

    print("Testing MageGuild")
    print(MageGuild.validate_mage_name("Test"))
    print(MageGuild.validate_mage_name("de"))
    casting = MageGuild()
    print(casting.cast_spell("Lightning", 15))
    print(casting.cast_spell("Lightning", 5))
