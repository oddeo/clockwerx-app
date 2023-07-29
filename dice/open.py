from random import randint
from dice.roll import Roll
from characters.character import Character


class OpenRoll(Roll):

    def start(self) -> dict:
        sides = self.kwargs.get('attribute')

        try:
            dice_roll = randint(1, int(sides))
            return {"dice_sides": sides,
                    "dice_roll": dice_roll}

        except KeyError as ke:
            return {"error": True, "message": f"key_error {ke}"}

        except Exception as e:
            return {"error": True, "message": str(e)}
