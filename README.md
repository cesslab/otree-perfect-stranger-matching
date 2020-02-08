# oTree Perfect Stranger Matching Example

The puropose of this [oTree](https://www.otree.org/) program is to illustrate a simple implementation of perfect stranger matching, or round robin matching.

![Playing the Game](https://github.com/cesslab/otree-perfect-stranger-matching/raw/master/media/matching.gif "Perfect Stranger Matching")

## Matching Implementation
The code for implementing the perfect stranger matching is located in the [Sessions.creating_session](https://github.com/cesslab/otree-perfect-stranger-matching/blob/master/perfect_stranger/game/models.py#L47-L123) function in the [models.py](https://github.com/cesslab/otree-perfect-stranger-matching/blob/master/perfect_stranger/game/models.py) file. Comments and links to further resources have been added to clarify any parts of the code that might be opaque to those unfamiliar with python programming.

## Installation

```git clone https://github.com/cesslab/otree-perfect-stranger-matching ```

If you are unfamiliar with git and github you can get started by watching [An Introduction to Git and GitHub, by Brian Yu](https://youtu.be/MJUJ4wbFm_A).

In the [project directory](https://github.com/cesslab/otree-perfect-stranger-matching) run the pipenv install command to install all the project dependencies. [Pipenv](https://pypi.org/project/pipenv/) is used to provide a virtual environment for managing python project dependencies (see [this tutorial](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv) for more information).

```pipenv install```

## Usage
The oTree program can be played by executing the `otree devserver` command in the [perfect_stranger](https://github.com/cesslab/otree-perfect-stranger-matching/tree/master/perfect_stranger) directory. You can also play through the example game to see a table containing all the pairings across all rounds. Each player will have their group in the current round highlighted in the table, as 
show below.

![Perfect Stranger Matching Image](https://github.com/cesslab/otree-perfect-stranger-matching/raw/master/media/Perfect_Stranger_Matching.png "Perfect Stranger Matching")

## License
See [oTree License](https://github.com/cesslab/otree-perfect-stranger-matching/raw/master/LICENSE)