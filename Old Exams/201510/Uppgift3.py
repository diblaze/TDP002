#! /usr/env/bin python3


def scrape_rates(filename):
    dict_rate = {}

    with open(filename) as f:
        for line in f.readlines():
            line = line.split("\t")
            line[1] = line[1].replace("\n", "")
            line[1] = line[1].replace(",", ".")
            dict_rate[line[0]] = line[1]

    return dict_rate


def convert_to_sek(string, dict_rate):
    string = string.split(" ")

    if len(string) == 2:
        currency_multiply = dict_rate[string[0]]
        value = string[1]
        return float(currency_multiply) * float(value)

    else:
        return float(string[0])


if __name__ == "__main__":
    dict_rate = scrape_rates("exchange_rates.txt")
    list_of_inputs = []

    print("Mata in belopp (avsluta med 0):")

    userInput = ""
    while userInput != "0":
        userInput = input()
        list_of_inputs.append(userInput)

    sumOfInputs = float(0)
    for i in list_of_inputs:
        sumOfInputs += convert_to_sek(i, dict_rate)

    print("Totalsumma: %.2f" % sumOfInputs)
