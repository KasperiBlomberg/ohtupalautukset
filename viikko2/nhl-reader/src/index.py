import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(player_dict) for player_dict in response]

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        players = filter(lambda p: p.nationality == nationality, players)
        return sorted(players, key=lambda p: p.points, reverse=True)

def main():
    print("NHL statistics by nationality")
    season = Prompt.ask(f"Select season [bold purple][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/][/bold purple]")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = Prompt.ask(f"Select nationality [bold purple][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/][/bold purple]")

        table = Table(title=f"Top scorers from {nationality} season {season}:")
        table.add_column("Player", justify="left", style="cyan")
        table.add_column("Team", justify="left", style="purple")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        players = stats.top_scorers_by_nationality(nationality)
        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))
        
        console = Console(force_terminal=True)
        console.print(table)

if __name__ == "__main__":
    main()
