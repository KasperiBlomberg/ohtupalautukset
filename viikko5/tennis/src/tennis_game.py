class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def equal_score(self):
        if self.m_score1 > 2:
            return "Deuce"
        return self.score_to_string(self.m_score1) + "-All"
    
    def score_to_string(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
        
    def won_the_game(self):
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            if abs(self.m_score1 - self.m_score2) >= 2:
                return True
    
    def get_score(self):
        #Score is tied
        if self.m_score1 == self.m_score2:
            return self.equal_score()

        #Game has been won
        if self.won_the_game():
            return "Win for player1" if self.m_score1 > self.m_score2 else "Win for player2"

        #Advantage
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return "Advantage player1" if self.m_score1 > self.m_score2 else "Advantage player2"

        #Regular score
        return self.score_to_string(self.m_score1) + "-" + self.score_to_string(self.m_score2)
