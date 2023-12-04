class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    SCORE_SEPARATOR = "-"

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.is_tie():
            return self.get_tie_score()
        elif self.is_advantage_or_win():
            return self.get_advantage_or_win_score()
        else:
            return self.get_regular_score()

    def is_tie(self):
        return self.m_score1 == self.m_score2

    def get_tie_score(self):
        if self.m_score1 < (len(self.SCORE_NAMES)-1):
            return self.SCORE_NAMES[self.m_score1] + "-All"
        else:
            return "Deuce"

    def is_advantage_or_win(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4

    def get_advantage_or_win_score(self):
        minus_result = self.m_score1 - self.m_score2

        if minus_result == 1:
            return "Advantage " + self.player1_name
        elif minus_result == -1:
            return "Advantage " + self.player2_name
        elif minus_result >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name

    def get_regular_score(self):
        score = ""

        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score += self.SCORE_SEPARATOR
                temp_score = self.m_score2

            score += self.SCORE_NAMES[temp_score]

        return score
