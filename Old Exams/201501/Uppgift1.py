#! /usr/bin/env python3

import sys


def scrape_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        years = lines[0].split()
        dict_data = {}
        for line in lines[1:]:
            place, *values = line.split()
            for i in range(len(values)):
                if values[i] == "--":
                    values[i] = 0.0
                else:
                    values[i] = float(values[i].replace(",","."))
            dict_data[place] = values

    return dict_data, years


def fill_in_values_to_place(data, years):
    dict_highest_values = {}
    for i in range(len(years)):
        for place, value in data.items():
            if place not in dict_highest_values:
                dict_highest_values[place] = {}
            if years[i] not in dict_highest_values[place]:
                dict_highest_values[place][years[i]] = 0
        
            if value[i] > dict_highest_values[place][years[i]]:
                dict_highest_values[place][years[i]] = value[i]
                            

    return dict_highest_values

def find_highest_value_per_year(data):
    highest_values = {}
    for place,years in data.items():
        for year, value in years.items():
            if year not in highest_values:
                highest_values[year] = {"Value": value, "Place": place}
            if value > highest_values[year]["Value"]:
                highest_values[year]["Value"] = value
                highest_values[year]["Place"] = place
    
    return highest_values
    



if __name__ == "__main__":
    data,years = scrape_file("given_files/bly-i-fisk.txt")
    #print(data,file=sys.stderr)
    #print(years)
    
    dict_highest_values = fill_in_values_to_place(data, years)

    dict_highest_values = find_highest_value_per_year(dict_highest_values)

    for year in sorted(dict_highest_values):
        place = dict_highest_values[year]["Place"]
        value = dict_highest_values[year]["Value"]
       
        print("{}: {} ({})".format(year, value, place), file=sys.stderr)



            
        


            
            


            


            

    


