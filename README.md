## oTree Perfect Stranger Matching Example

The puropose of this project is to illustrate a possible implementation for perfect stranger matching, or round robin matching.

If you are looking to implement perfect stranger matching, the key file to look at is the 
[models.py](https://github.com/cesslab/otree-perfect-stranger-matching/blob/master/perfect_stranger/game/models.py) file. In particular the [creating_session](https://github.com/cesslab/otree-perfect-stranger-matching/blob/master/perfect_stranger/game/models.py#L47-L123) 
function in the Subsession class.

You can also play through the example game to see a table containing all the pairings across all rounds. Each player will have their group in the current round highlighted in the table, as 
show below.

![Perfect Stranger Matching Image](https://github.com/cesslab/otree-perfect-stranger-matching/raw/master/perfect_stranger/img/Perfect_Stranger_Matching.png "Perfect Stranger Matching")