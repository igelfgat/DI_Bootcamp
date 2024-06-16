# Player

# Attributes
## name: str
## strength: int | float
## health: int | float

# Methods
## attack()
## defend


class GameCharacter:

    def __init__(
        self, player_name: str, player_strength: int | float, player_health: int | float
    ):  # initializor
        # self - the object itself / a reference to the object
        self.name = player_name
        self.strength = player_strength
        self.health = player_health

    def attack(self) -> None:
        print(f"Player {self.name} is attacking with strength {self.strength}")

    def defend(self, enemy: "GameCharacter") -> None:
        self.health -= enemy.strength * 0.1
        print(f"Player {self.name} defends. New player's health is now: {self.health}")


def main() -> None:

    player_yossi = GameCharacter(
        player_name="Yossi", player_strength=100, player_health=50
    )
    player_ben = GameCharacter("Ben", 120, 88)

    monster1 = GameCharacter("DASDWAS", 100, 30)

    print(
        f"Player {player_yossi.name} has {player_yossi.strength} Strength and {player_yossi.health} Health."
    )

    player_yossi.attack()
    player_ben.attack()

    player_yossi.defend(monster1)

    print(player_yossi.health)


if __name__ == "__main__": # Run the code below if you run the file directly
    main()
