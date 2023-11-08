from player_reader import PlayerReader

class PlayerStats:
    
    def __init__(self, reader: PlayerReader):
        self.reader = reader
        
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        return filter( lambda x: x.nationality == nationality, players)
        