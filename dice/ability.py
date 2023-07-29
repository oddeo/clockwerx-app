from random import randint
from dice.roll import Roll
from characters.character import Character


class AbilityCheckRoll(Roll):

    def start(self) -> dict:
        attribute = self.kwargs.get('attribute')

        try:
            p = self.player
            modifier = int(p.abilities[attribute]["modifier"])

            d20_roll = randint(1, 20)
            return {"roll_total": modifier + d20_roll,
                    "modifier": modifier,
                    "attribute": attribute,
                    "dice_roll": d20_roll}

        except KeyError as ke:
            return {"error": True, "message": f"key_error {ke}"}

        except Exception as e:
            return {"error": True, "message": str(e)}
