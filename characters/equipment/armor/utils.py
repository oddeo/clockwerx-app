def calculate_ac(character, dex_cap, item_bonus=0, other_bonus=0, penalties=0):
    dex_bonus = dex_cap \
        if dex_cap < character.abilities['dexterity']['modifier'] \
        else character.abilities['dexterity']['modifier']

    # TODO: Set this from the Armor Class strategy
    proficiency_bonus = 0

    return 10 + dex_bonus + proficiency_bonus + item_bonus + other_bonus - penalties
