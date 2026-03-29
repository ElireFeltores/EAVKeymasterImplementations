from __future__ import annotations
import functools
from typing import List, Dict, Set
from dataclasses import dataclass
from Options import Toggle, OptionSet, Choice
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class MinesweeperPlusArchipelagoOptions:
    minesweeper_plus_sections: MinesweeperPlusSections
    minesweeper_plus_maximum_difficulty: MinesweeperPlusMaximumDifficulty

class MinesweeperPlusGame(Game):
    name = "Minesweeper Plus"
    platform = KeymastersKeepGamePlatforms.PC
    is_adult_only_or_unrated = False 
    options_cls = MinesweeperPlusArchipelagoOptions
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        if self.include_episode_1:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Beat EPISODE1_LEVEL on any difficulty.",
                        data = {
                            "EPISODE1_LEVEL": (self.episode_1_levels, 1),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = False,
                        weight = 10,
                ),
                GameObjectiveTemplate(
                    label = "Beat EPISODE1_LEVEL on DIFFICULTY or higher.",
                        data = {
                            "EPISODE1_LEVEL": (self.episode_1_levels, 1),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = True,
                        weight = 10,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on any difficulty: EPISODE1_LEVEL",
                        data = {
                            "EPISODE1_LEVEL": (self.episode_1_levels, 2)
                        },
                        is_time_consuming = True,
                        is_difficult = False,
                        weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on any difficulty: EPISODE1_LEVEL",
                        data = {
                            "EPISODE1_LEVEL": (self.episode_1_levels, 3)
                        },
                        is_time_consuming = True,
                        is_difficult = False,
                        weight = 3,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on any difficulty: EPISODE1_LEVEL",
                        data = {
                            "EPISODE1_LEVEL": (self.episode_1_levels, 4)
                        },
                        is_time_consuming = True,
                        is_difficult = False,
                        weight = 2,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on DIFFICULTY or higher: EPISODE1_LEVEL",
                        data = {
                            "EPISODE1_LEVEL": (self.episode_1_levels, 2),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on DIFFICULTY or higher: EPISODE1_LEVEL",
                        data = {
                            "EPISODE1_LEVEL": (self.episode_1_levels, 3),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 3,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on DIFFICULTY or higher: EPISODE1_LEVEL",
                        data = {
                            "EPISODE1_LEVEL": (self.episode_1_levels, 4),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 2,
                ),
                GameObjectiveTemplate(
                    label = "Complete Episode 1 on any difficulty.",
                        data = {
                        
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 1,
                ),
                GameObjectiveTemplate(
                    label = "Complete Episode 1 on DIFFICULTY or higher.",
                        data = {
                        "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 1,
                ),
            ])
        if self.include_episode_2:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Beat EPISODE2_LEVEL on any difficulty.",
                        data = {
                            "EPISODE2_LEVEL": (self.episode_2_levels, 1),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = False,
                        weight = 10,
                ),
                GameObjectiveTemplate(
                    label = "Beat EPISODE2_LEVEL on DIFFICULTY or higher.",
                        data = {
                            "EPISODE2_LEVEL": (self.episode_2_levels, 1),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = True,
                        weight = 10,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on any difficulty: EPISODE2_LEVEL",
                        data = {
                            "EPISODE2_LEVEL": (self.episode_2_levels, 2)
                        },
                        is_time_consuming = True,
                        is_difficult = False,
                        weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on any difficulty: EPISODE2_LEVEL",
                        data = {
                            "EPISODE2_LEVEL": (self.episode_2_levels, 3)
                        },
                        is_time_consuming = True,
                        is_difficult = False,
                        weight = 3,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on any difficulty: EPISODE2_LEVEL",
                        data = {
                            "EPISODE2_LEVEL": (self.episode_2_levels, 4)
                        },
                        is_time_consuming = True,
                        is_difficult = False,
                        weight = 2,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on DIFFICULTY or higher: EPISODE2_LEVEL",
                        data = {
                            "EPISODE2_LEVEL": (self.episode_2_levels, 2),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on DIFFICULTY or higher: EPISODE2_LEVEL",
                        data = {
                            "EPISODE2_LEVEL": (self.episode_2_levels, 3),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 3,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following levels on DIFFICULTY or higher: EPISODE2_LEVEL",
                        data = {
                            "EPISODE2_LEVEL": (self.episode_2_levels, 4),
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 2,
                ),
                GameObjectiveTemplate(
                    label = "Complete Episode 2 on any difficulty.",
                        data = {
                        
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 1,
                ),
                GameObjectiveTemplate(
                    label = "Complete Episode 2 on DIFFICULTY or higher.",
                        data = {
                        "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 1,
                ),
            ])
        if self.include_big_one:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Beat The Big One: Level 1",
                        data = {
                        },
                        is_time_consuming = False,
                        is_difficult = False,
                        weight = 9,
                ),
                GameObjectiveTemplate(
                    label = "Beat The Big One: Level 2",
                        data = {
                        },
                        is_time_consuming = False,
                        is_difficult = False,
                        weight = 8,
                ),
                GameObjectiveTemplate(
                    label = "Beat The Big One: Level 3",
                        data = {
                        },
                        is_time_consuming = False,
                        is_difficult = False,
                        weight = 7,
                ),
                GameObjectiveTemplate(
                    label = "Beat The Big One: Level 4",
                        data = {
                        },
                        is_time_consuming = True,
                        is_difficult = False,
                        weight = 6,
                ),
                GameObjectiveTemplate(
                    label = "Beat The Big One: Level 5",
                        data = {
                        },
                        is_time_consuming = True,
                        is_difficult = False,
                        weight = 5,
                ),
                GameObjectiveTemplate(
                    label = "Beat The Big One: Level 6",
                        data = {
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Beat The Big One: Level 7",
                        data = {
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 3,
                ),
                GameObjectiveTemplate(
                    label = "Beat The Big One: Level 8",
                        data = {
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 2,
                ),
                GameObjectiveTemplate(
                    label = "Beat The Big One: Level 9",
                        data = {
                        },
                        is_time_consuming = True,
                        is_difficult = True,
                        weight = 1,
                ),
            ])
        if self.include_free_play:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Beat a WIDTH by HEIGHT board that is MINES mines.",
                        data = {
                            "WIDTH": (self.width, 1),
                            "HEIGHT": (self.height, 1),
                            "MINES": (self.mines, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = False,
                        weight = 10,
                ),
                GameObjectiveTemplate(
                    label = "Beat a WIDTH by HEIGHT board that is MINES mines with the 9 boss.",
                        data = {
                            "WIDTH": (self.width, 1),
                            "HEIGHT": (self.height, 1),
                            "MINES": (self.mines, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = True,
                        weight = 5,
                ),
                GameObjectiveTemplate(
                    label = "Beat a WIDTH by HEIGHT board that is MINES mines with the 10 boss.",
                        data = {
                            "WIDTH": (self.width, 1),
                            "HEIGHT": (self.height, 1),
                            "MINES": (self.mines, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = True,
                        weight = 5,
                ),
                GameObjectiveTemplate(
                    label = "Beat a WIDTH by HEIGHT board that is MINES mines with the 9 and 10 bosses.",
                        data = {
                            "WIDTH": (self.width, 1),
                            "HEIGHT": (self.height, 1),
                            "MINES": (self.mines, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = True,
                        weight = 2,
                ),
            ])
        if self.include_boss_pursuit and self.include_episode_1:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Beat Episode 1 on Boss Pursuit on any difficulty.",
                        data = {
                        },
                        is_time_consuming = False,
                        is_difficult = False,
                        weight = 10,
                ),
                GameObjectiveTemplate(
                    label = "Beat Episode 1 on Boss Pursuit on DIFFICULTY difficulty or higher.",
                        data = {
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = True,
                        weight = 8,
                ),
            ])
        if self.include_boss_pursuit and self.include_episode_2:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Beat Episode 2 on Boss Pursuit on any difficulty.",
                        data = {
                        },
                        is_time_consuming = False,
                        is_difficult = False,
                        weight = 10,
                ),
                GameObjectiveTemplate(
                    label = "Beat Episode 2 on Boss Pursuit on DIFFICULTY difficulty or higher.",
                        data = {
                            "DIFFICULTY": (self.difficulty, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = True,
                        weight = 8,
                ),
            ])
        return game_objective_templates

    @property
    def modes(self) -> List[str]:
        return sorted(self.archipelago_options.minesweeper_plus_sections.value)
    @property
    def include_episode_1(self) -> bool:
        return "Episode 1" in self.modes
    @property
    def include_episode_2(self) -> bool:
        return "Episode 2" in self.modes
    @property
    def include_big_one(self) -> bool:
        return "The Big One" in self.modes
    @property
    def include_free_play(self) -> bool:
        return "Free Play" in self.modes
    @property
    def include_boss_pursuit(self) -> bool:
        return "Boss Pursuit" in self.modes

    def difficulty(self) -> List[str]:
        difficulties: List[str] = ["Beginner","Novice","Veteran","Expert"]
        difficulties = difficulties[:(self.archipelago_options.minesweeper_plus_maximum_difficulty.value + 1)]
        return difficulties
    def width(self) -> List[str]:
        width: List[str] = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        return width
    def height(self) -> List[str]:
        height: List[str] = [5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        return height
    def mines(self) -> List[str]:
        mines: List[str] = ["10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%"]
        return mines
    @staticmethod
    def episode_1_levels() -> List[str]:
        return [
            "Kiddie Pool (Episode 1 Stage 1)",
            "Rainy Puddle (Episode 1 Stage 2)",
            "Small Pond (Episode 1 Stage 3)",
            "Blue Lagoon (Episode 1 Stage 4)",
            "Lazy River (Episode 1 Stage 5)",
            "Great Lake (Episode 1 Stage 6)",
            "Open Ocean (Episode 1 Stage 7)",
            "Dead Sea (Episode 1 Stage 8)",
            "The Devil's Triangle (Episode 1 Stage 9)",
        ]
    @staticmethod
    def episode_2_levels() -> List[str]:
        return [
            "The Shallow End (Episode 2 Stage 1)",
            "Fountain Flows (Episode 2 Stage 2)",
            "Silent Marsh (Episode 2 Stage 3)",
            "Murky Swamp (Episode 2 Stage 4)",
            "Crazy Cove (Episode 2 Stage 5)",
            "Raging Rapids (Episode 2 Stage 6)",
            "Gulf of Misery (Episode 2 Stage 7)",
            "Black Water (Episode 2 Stage 8)",
            "The Deep End (Episode 2 Stage 9)",
            "The Devil's Passage (Episode 2 Stage 10)",
        ]


class MinesweeperPlusSections(OptionSet):
    """ 
    Defines what sections can generate in keeps.
    Episode 1: Episode 1 levels can appear in a trial.
    Episode 2: Episode 2 levels can appear in a trial.
    The Big One: Trials on The Big One can appear.
    Free Play: Trials on Free Play can appear.
    Boss Pursuit: Boss Pursuit trials can appear for episodes. This option will not apply if neither episode is enabled.
    """
    display_name = "Sections Included"
    valid_keys = [
        "Episode 1",
        "Episode 2",
        "The Big One",
        "Free Play",
        "Boss Pursuit",
    ]
    default = valid_keys

class MinesweeperPlusMaximumDifficulty(Choice):
    """ 
    Defines the maximum game difficulty that can generate in keeps.
    Note: Will never apply if Difficult Trials are set to false.
    """
    display_name = "Difficulty"
    option_beginner = 0
    option_novice = 1
    option_veteran = 2
    option_expert = 3
    default = 1
