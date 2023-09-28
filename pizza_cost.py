#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: September 28th, 2023
# This program asks the user for the diameter of the
# pizza. It then calculates and displays the total cost
# of the pizza with tax
import constants


def main():
    # user inputs diameter of pizza
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # terminal process the calculations
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # terminal outputs the total pizza cost
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
