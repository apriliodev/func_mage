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
            power = args[0]
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
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool
    def cast_spell(self, spell_name: str, power: int) -> str
