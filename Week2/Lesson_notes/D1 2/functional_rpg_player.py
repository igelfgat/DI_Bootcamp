def create_player(name: str, strength: int, health: int) -> dict:
    player = name
    player_strength = strength
    player_health = health
    
    return {
        "name": player,
        "strength": player_strength,
        "health": player_health
    }

yossi = create_player("Yossi", 100, 200)

def attack(player: dict) -> None:
    print(f"Player {player} performs an attack with strenght {player_strength}")


def defend(player: dict, enemy_attack: int | float) -> None:
    player["health"] -= (
        enemy_attack * 0.1
    )  # multiplying to reduce the strength if the enemy attack
    print(f"Player {player["name"]} defends. New player's health is now: {player["health"]}")


attack(player1, player_strength1)
defend(player1, player_health1, 29)
