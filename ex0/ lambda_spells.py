def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    strongest_mage: dict = max(mages, key=lambda mage: mage["power"])
    weakest_mage: dict = min(mages, key=lambda mage: mage["power"])
    max_power: int = strongest_mage["power"]
    min_power: int = weakest_mage["power"]
    power = list(map(lambda mage: mage["power"], mages))
    avg_power: float = round(sum(power) / len(mages), 2)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }

def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
    ]
    spells = [
        "fireball", "heal", "shield"
    ]
    
    transf = spell_transformer(spells)
    sort_art = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(
        f"{sort_art[0]["name"]} ({sort_art[0]["power"]} power)"
        f" comes before {sort_art[1]["name"]} ({sort_art[1]["power"]} power)"
        )
    print("\nTesting spell transformer...")
    print(" ".join(transf))
    
    


if __name__ == "__main__":
    print()
    main()