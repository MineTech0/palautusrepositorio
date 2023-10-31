from player_reader import PlayerReader
from sort_by import SortBy


class StatisticsService:
    def __init__(self,reader: PlayerReader):

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by: SortBy = SortBy.POINTS):
        func = lambda player: player.points
        
        if sort_by == SortBy.GOALS:
            func = lambda player: player.goals
        elif sort_by == SortBy.ASSISTS:
            func = lambda player: player.assists
              
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=func
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
