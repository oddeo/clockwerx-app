from characters.equipment.coins.types import Coins


def currency_conversion(amount: int, starting_currency: Coins, ending_currency: Coins):

    convert_to_copper = 0
    if starting_currency == Coins.COPPER:
        convert_to_copper = amount
    elif starting_currency == Coins.SILVER:
        convert_to_copper = amount * 10
    elif starting_currency == Coins.GOLD:
        convert_to_copper = amount * 100
    elif starting_currency == Coins.PLATINUM:
        convert_to_copper = amount * 1000
    else:
        raise ValueError(f"{starting_currency.value} is not a supported currency")

    if ending_currency == Coins.COPPER:
        converted_amount = convert_to_copper
    elif ending_currency == Coins.SILVER:
        converted_amount = convert_to_copper / 10
    elif ending_currency == Coins.GOLD:
        converted_amount = convert_to_copper / 1_00
    elif ending_currency == Coins.PLATINUM:
        converted_amount = convert_to_copper / 1_000
    else:
        raise ValueError(f"{ending_currency.value} is not a supported currency")

    return {"amount": converted_amount, "currency": ending_currency.value}
