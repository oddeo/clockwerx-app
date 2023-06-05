from characters.character import Character
from random import randint


def skill_roll(player, skill):

    try:
        p = Character.cast(player)
        score = p.skills[skill]['score']
        d20_roll = randint(1, 20)
        return {"value": score + d20_roll, "score": score, "roll": d20_roll, "error": False}

    except Exception as e:
        print(e)
        return {"value": 0, "score": 0, "roll": 0, "error": True}


def ability_roll(player, ability):

    try:
        p = Character.cast(player)
        score = p.abilities[ability]['score']
        d20_roll = randint(1, 20)
        return {"value": score + d20_roll, "score": score, "roll": d20_roll, "error": False}

    except Exception as e:
        print(e)
        return {"value": 0, "score": 0, "roll": 0, "error": True}


def initiative_roll(player, skill):

    try:
        p = Character.cast(player)

        if skill == "perception":
            score = p.perception['score']
        else:
            score = p.skills[skill]['score']

        d20_roll = randint(1, 20)
        return {"value": score + d20_roll, "score": score, "roll": d20_roll, "error": False}

    except Exception as e:
        print(e)
        return {"value": 0, "score": 0, "roll": 0, "error": True}


def perception_roll(player, attribute="perception"):

    try:
        p = Character.cast(player)

        if attribute == "perception":
            score = p.perception['score']
        else:
            raise KeyError()

        d20_roll = randint(1, 20)
        return {"value": score + d20_roll, "score": score, "roll": d20_roll, "error": False}

    except Exception as e:
        print(e)
        return {"value": 0, "score": 0, "roll": 0, "error": True}
