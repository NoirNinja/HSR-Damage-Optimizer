#!/usr/bin/env python3

"""To do list:
    Figure out how to store character and lightcone information
    GUI
    change float to decimal?
    Add stat requirments
    Add conditional buffs ie. character, lighcone, and relic buffs
        (for average damage have buff percentage uptime?)
    Add acomidation for alternate stat scaling
    Add calculations for dmg% increases and enemy armor?"""

__author__ = 'Ian Ramage'
__date__ = '10/31/2023'

def calc_crit_damage(base_atk, atk_percent, crit_dmg, skill):
    return ((((base_atk * atk_percent) + 352.8) * crit_dmg) * skill)


def calc_damage(base_atk, atk_percent, skill):
    return (((base_atk * atk_percent) + 352.8) * skill)


def calc_average_damage(base_atk, atk_percent, crit_rate, crit_dmg, skill):
    if crit_rate > 1:
        crit_rate = 1

    return ((1-crit_rate) * calc_damage(base_atk, atk_percent, skill)) +\
            (crit_rate * calc_crit_damage(base_atk, atk_percent, crit_dmg, skill))


def main():
    base_atk = int(input("Base Attack? "))
    print()
    atk_percent = float(input("Non-Relic Attack%? "))
    print()
    crit_rate = float(input("Non-Relic Crit Rate? "))
    print()
    crit_dmg = float(input("Non-Relic Crit Damage? "))
    print()
    body = input("Crit Rate or Crit Damage body?(r/d) ")
    print()
    boots = input("Attack% boots?(y/n) ")
    print()
    skill = float(input("Ability damage multiplier? "))
    print()

    crit_dmg += .0648 * 6
    crit_rate += .0324 * 6
    atk_percent += (.0432 * 6) + .432
    if body.lower() == "r":
        crit_rate += .324
    else:
        crit_dmg += .648
    if boots.lower() == "y":
        atk_percent += .432 

    counter = 0
    while counter < 30:
        crit_rate_dmg = calc_average_damage(base_atk, atk_percent, crit_rate + .0324, crit_dmg, skill)
        crit_dmg_dmg = calc_average_damage(base_atk, atk_percent, crit_rate, crit_dmg + .0648, skill)
        atk_percent_dmg = calc_average_damage(base_atk, atk_percent + .0432, crit_rate, crit_dmg, skill)

        if crit_rate_dmg >= atk_percent_dmg and crit_rate_dmg >=crit_dmg_dmg:
            crit_rate += .0324
        elif crit_dmg_dmg >= atk_percent_dmg:
            crit_dmg += .0648
        else:
            atk_percent += .0432

        counter += 1

    print("Optimal Stats:")
    print("Atk%", atk_percent)
    print("Crit Rate", crit_rate)
    print("Crit Damage", crit_dmg)
    print("\nExpected damage before damage% increases and armor:")
    print("Damage", calc_damage(base_atk, atk_percent, skill))
    print("Crit Damage", calc_crit_damage(base_atk, atk_percent, crit_dmg, skill))
    print("Average", calc_average_damage(base_atk, atk_percent, crit_rate, crit_dmg, skill))


if __name__ == "__main__":
    main()
