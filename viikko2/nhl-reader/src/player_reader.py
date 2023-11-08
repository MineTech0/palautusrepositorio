import requests
from player import Player

class PlayerReader:
    def __init__(self,url) -> None:
        self.url = url
        
    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player in response:
            players.append(Player(player))
        return players