class Adamplayer:
    def __init__(self, given_name, rank):
        self.new_name = given_name
        self.rank = rank
        self.adam_trust = 5


    def change_rank(self, new_rank):
        self.rank = new_rank