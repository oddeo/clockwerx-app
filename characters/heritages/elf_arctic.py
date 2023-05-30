from characters.abstract.strategy import Strategy
from characters.heritages.types import Heritages


class ArcticElf(Strategy):
    def configure(self, character):
        character.set_heritage(Heritages.ELF_ARCTIC)

        # TODO: I don 't have a way to capture cold resistance yet
        """
        This heritage grants you resistance to cold damage 
        equal to 1/2 your level (minimum 1)
        
        Resistances and immunities should be captured in 
        Ancestry Feats & Abilities section: Heritage 1st
        They come into plan when your character is taking damage
        
        You treat environmental cold effects as if they were
        one step less extreme (incredible cold becomes extreme,
        extreme cold becomes severe, etc.)
        """

        return character
