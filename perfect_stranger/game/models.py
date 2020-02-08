from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random


author = 'Anwar A. Ruff'

doc = """
Perfect Stranger Matching Example
"""


class Constants(BaseConstants):
    name_in_url = 'game'
    # For more information on how the players_per_groups value affects players
    # id_in_group value see: 
    # https://otree.readthedocs.io/en/latest/multiplayer/groups.html#fixed-matching
    players_per_group = None 
    num_rounds = 4


class Subsession(BaseSubsession):
    def right_rotate(self, lst): 
        """ 
        Takes a list (lst) and right rotates it by one position. 
        For example, given lst = [1, 2, 3] right_rotate returns [3, 1, 2].
        """
        return [lst[-1]] + lst[0:len(lst)-1]

    def is_even(self, number):
        """ This function returns true if number is even, otherwise false is returned. """
        # See link for more information on the modulus operator:
        # https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html#modulus
        return number % 2 == 0

    # To further understand how creating_sessions works read: 
    # https://otree.readthedocs.io/en/latest/models.html#creating-session
    def creating_session(self):
        if self.round_number == 1:
            # When the Constants.players_per_group is set to None, a list containing
            # a single list (group) of all players is returned from the function 
            # get_group_matrix.
            # 
            # For example, if there are 4 players and Constants.players_per_group is 
            # set to None, get_group_matrix will return 
            # [[<Player 1>, <Player 2>, <Player 3>, <Player 4>]]
            # which is a list of all players contained in a list, pay close attention
            # to the brackets.
            #
            # The reason why [0] is appending to self.get_group_matrix() is to extract
            # that single list (group) of all players.
            #
            # See link for more info on the get_group_matrix function:
            # https://otree.readthedocs.io/en/latest/multiplayer/groups.html#get-group-matrix
            players = self.get_group_matrix()[0]

            random.shuffle(players)

            # The following list comprehension is used to place all of the players with a
            # player ID (or more percisely a player session id) that is even into one group.
            # These ids will be use for matching across subsessions (rounds).

            # See link for more info on list comprehensions:
            # https://medium.com/better-programming/list-comprehension-in-python-8895a785550b

            #See link for more info on the player's id_in_subsession:
            # https://otree.readthedocs.io/en/latest/models.html#id-in-session
            even_players = [p for p in players if self.is_even(p.id_in_subsession)]
            odd_players = [p for p in players if not self.is_even(p.id_in_subsession)]

            # The zip function will pair elements in the even_players and odd_players list 
            # into a tuple (e.g. zip([p3, p1], [p2, p4]) results in (p3, p2), (p1, p4))
            # A list comprehension is then used to turn each tuple into a list containing
            # a list of groups.
            # [(p3, p2), (p1, p4)] which is a list of tuples is transformed into 
            # [[p3, p2], [p1, p4]] which is a list of lists.
            #
            # See link for more info on tuples:
            # https://www.tutorialspoint.com/python/python_tuples.htm
            #
            # See link for more info on the set_group_matrix function:
            # https://otree.readthedocs.io/en/latest/multiplayer/groups.html#set-group-matrix
            # 
            # See link for more info on the zip function:
            # https://www.w3schools.com/python/ref_func_zip.asp  
            self.set_group_matrix([[i, j] for i,j in zip(even_players, odd_players)])

        else:
            # See link for more info on the group_like_round function:
            # https://otree.readthedocs.io/en/latest/multiplayer/groups.html#group-like-round
            self.group_like_round(self.round_number - 1)

            group_matrix = self.get_group_matrix()

            # The following for loop splits the group pairs in group_matrix into two lists.
            # The even_players list which consists of players with an even subsession id, 
            # and the odd_players list which consists of players with an odd subsession id.
            odd_players = []
            even_players = []
            for group in group_matrix:
                for player in group:
                    if self.is_even(player.id_in_subsession):
                        even_players.append(player)
                    else:
                        odd_players.append(player)
            
            # Only the odd players are rotated, then they are paired back with the even 
            # players list.
            odd_players = self.right_rotate(odd_players)
            self.set_group_matrix([[i, j] for i,j in zip(even_players, odd_players)])


        print(f"Displaying group matrix for round {self.round_number}")
        print(self.get_group_matrix())


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
