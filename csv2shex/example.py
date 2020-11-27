from typing import List, Union

def get_batting_ave(hits: int, at_bats: int) -> float:
    return round(hits / at_bats, 3)

player_ave = get_batting_ave(174, 549)
print(f"player_ave: {player_ave}")
