from __future__ import annotations
import functools
from typing import List, Dict, Set
from dataclasses import dataclass
from Options import Toggle, OptionSet, Choice, OptionList
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class BoopArchipelagoOptions:
    boop_list: BoopingList

class BoopGame(Game):
    name = "Booping"
    platform = KeymastersKeepGamePlatforms.META
    is_adult_only_or_unrated = False 
    options_cls = BoopArchipelagoOptions
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()
        game_objective_templates.append(
            GameObjectiveTemplate(
                label = "Boop PERSON.",
                    data = {
                        "PERSON": (self.boop_list, 1),
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 5,
            ),
        )
        return game_objective_templates

    def boop_list(self) -> List[str]:
        boop: List[str] = list(self.archipelago_options.boop_list.value)
        return sorted(boop)

class BoopingList(OptionList):
    """ 
    Lists who all can appear to be booped from trials in this.
    """
    display_name = "Booping List"
    default = [
        "Anyone",
    ]
