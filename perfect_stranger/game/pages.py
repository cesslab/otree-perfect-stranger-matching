from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def vars_for_template(self):
        subsessions = self.session.get_subsessions()
        matrices = [subsession.get_group_matrix() for subsession in subsessions]
        return { 
            'other_player': self.player.get_others_in_group()[0],
            'matrix': self.subsession.get_group_matrix(),
            'group_matrices': matrices
        } 


# class ResultsWaitPage(WaitPage):
#     def after_all_players_arrive(self):
#         pass


# class Results(Page):
#     pass


page_sequence = [MyPage]
