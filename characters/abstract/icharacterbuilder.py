from abc import ABCMeta, abstractmethod


class ICharacterBuilder(metaclass=ABCMeta):
    """
    We are learning the "Builder Pattern" and it starts here.

    1) Think of this like the order form that the Pathfinder company
    sends to a printing press when they want to get blank character
    sheets printed
    """

    @abstractmethod
    def set_character_name(self, value):
        """ Set the Character Name """

    @abstractmethod
    def set_armor_class(self, value):
        """ Set the Character Armor Class """

    @abstractmethod
    def set_armor(self, value):
        """ Equip the Character with Armor """

    @abstractmethod
    def set_level(self, value):
        """ Set the Character Level """

    @abstractmethod
    def set_hero_points(self, value):
        """ Set the Character's Hero Points """

    @abstractmethod
    def set_hit_points(self, value):
        """ Set the Character Hit Points """

    @abstractmethod
    def set_abilities(self, value):
        """ Set the Character's abilities """

    @abstractmethod
    def set_skills(self, value):
        """ Set the Character's abilities """

    @abstractmethod
    def set_ancestry(self, value):
        """ Set the Character's ancestry """

    @abstractmethod
    def set_heritage(self, value):
        """ Set the Character's heritage """

    @abstractmethod
    def set_background(self, value):
        """ Set the Character's background """

    @abstractmethod
    def set_languages(self, value):
        """ Set a list of the Character's Languages """

    @abstractmethod
    def set_traits(self, value):
        """ Set a list of the Character's Ancestry Traits """

    @abstractmethod
    def set_features(self, value):
        """ Set a list of the Character's Ancestry Feats """

    @abstractmethod
    def set_class(self, value):
        """ Set the Character's Class """

    @abstractmethod
    def set_perception(self, value):
        """ Set the Character's Perception """

    @abstractmethod
    def set_saving_throws(self, value):
        """ Set the Character's Saving Throws """

    @abstractmethod
    def set_bulk(self, value):
        """ Set the Character's Bulk Scores """

    @abstractmethod
    def set_weapon_proficiencies(self, value):
        """ Set the Character's Weapon Proficiencies """

    @abstractmethod
    def set_weapons(self, value):
        """ Equip the Character with Weapons """

    @abstractmethod
    def set_coins(self, value):
        """ Equip the Character with Coins """

    @abstractmethod
    def set_discord_display_name(self, value):
        """ Set the Discord Display Name """

    @abstractmethod
    def get_result(self):
        """
        Keep this as the last method in the list.
        It's the method that returns the Character
        during the build process.
        """
