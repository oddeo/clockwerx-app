def calculate_ac(character, armor, item_bonus=0, other_bonus=0, penalties=0):
    dex_bonus = armor['dex_cap'] \
        if armor['dex_cap'] < character.abilities.dexterity['modifier'] \
        else character.abilities.dexterity['modifier']

    # TODO: Set this from the Armor Class strategy
    proficiency_bonus = 0

    return 10 + dex_bonus + proficiency_bonus + item_bonus + other_bonus - penalties