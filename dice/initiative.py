from random import randint
from dice.roll import Roll


class InitiativeRoll(Roll):

    def start(self) -> dict:
        attribute = self.kwargs.get('attribute') \
            if 'attribute' in self.kwargs \
            else 'perception'

        try:
            p = self.player

            if attribute == "perception":
                modifier = int(p.perception["proficiency"])
                modifier += int(p.abilities["wisdom"]["modifier"])
            else:
                modifier = p.skills[attribute]['score']

            d20_roll = randint(1, 20)
            return {"roll_total": modifier + d20_roll,
                    "modifier": modifier,
                    "attribute": attribute,
                    "dice_roll": d20_roll}

        except KeyError as ke:
            return {"error": True, "message": f"key_error {ke}"}

        except Exception as e:
            return {"error": True, "message": str(e)}
