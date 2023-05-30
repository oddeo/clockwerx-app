from characters.abstract.strategy import Strategy


class DefaultBulkLimit(Strategy):

    def __init__(self):
        self.score = 0
        self.encumbered_base = 0
        self.maximum_base = 0

    def configure(self, character):
        character.set_bulk(DefaultBulkLimit())
        character.set_bulk_encumbered_base(character.abilities['strength']['modifier'] + 5)
        character.set_bulk_maximum_base(character.abilities['strength']['modifier'] + 10)

        return character
