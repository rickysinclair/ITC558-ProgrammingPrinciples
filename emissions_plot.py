# In this assignment, you will perform some basic data analysis on a dataset obtained from
# Gapminder project (https://www.gapminder.org/tools/). Gapminder collects authentic facts
# and statistics of all countries worldwide and then plots the data in easy to understand
# visualization tools.
#
# You have been provided a dataset file Emissions.csv which contains CO2 emissions data
# extracted from a Gapminder dataset. Download Emissions.txt file from the unit Interact site.
# The file contains comma-separated data of annual CO2 emissions (per capita) from 195
# countries for a period of 1997 to 2010. CO2 emissions are measured in metric tones. It is a plain
# text file as shown in screenshot below. First line contains data headers, and then each line
# contains data for one country. To clearly understand data structure, you can also open the csv
# file in a spreadsheet software.
#
# Your program will read this data file and perform the following jobs:
#
# (1) Read all the data from file and save it into a Python dictionary. Each key in the dictionary
# should be a country name as read from the file, and value of that key will be a Python list
# containing emission data for that specific country. Once all the file is read, dictionary will
# contain 195 keys Each key will correspond to a Python list containing 14 numbers (emission
# data from 1996 to 2010). You should use this dictionary for the next three jobs.
#
# (2) Calculate worldwide statistics (min, max, average) for a user-selected year. See example in
# the sample-run below.
#
# (3) Extract data for up to three user-selected country and save it to a new file
# Emissions_subset.csv. New file should have exactly same format as the source file, i.e. first line
# of headers and then up to 3 lines for selected countries. See the sample-run below for an
# example.
#
# (4) Plot the emissions data from a user-selected country. You should use Python plotting
# library matplotlib for drawing the plots. The links below contain examples on how to draw
# simple plots using this library.


import csv
from decimal import Decimal

import matplotlib.pyplot as plt

my_dict = dict()  # declare dictionary


def get_file():
    """
    The get_file function reads the Emissions.csv file into the my_dict dictionary.
    It also checks to see that the file is readable.
    """
    file_name = 'Emissions.csv'
    try:  # check if the file is readable
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            print("All data from", file_name, "has been read into a dictionary.")
    except IOError:  # send error if nto readable
        print(file_name, "cannot be read.")
        exit()  # exit program if not readable

    for line in your_list:
        if line[0] in my_dict:
            # append the new number to the existing list at this slot
            my_dict[line[0]].append(line[1:15])
        else:
            # create a new list in this slot
            my_dict[line[0]] = [line[1:15]]


def average(year):
    """
    The average function receives the year string as a parameter and calculates the
    average of all emissions for the selected year
    :param year string
    :return: average decimal
    """
    year_index = my_dict['CO2 per capita'][0].index(year)  # find index of year
    final = 0
    for i in my_dict.values():  # loop through the values for the associated year
        total = Decimal((i[0][year_index]))  # add year to total
        final = final + total
    final = (final - int(year)) / len(my_dict)  # calculate average
    return round(final, 6)  # return average


def maximum(year):
    """
    The maximum function receives the year string as a parameter and calculates the
    maximum value of all emissions for the selected year
    :param year string
    :return: key_name string and maximum decimal
    """
    year_index = my_dict['CO2 per capita'][0].index(year)  # find index of the year
    maxi = 0
    key_name = ""
    iter_v1 = iter(my_dict.values())  # set first iterator value
    next(iter_v1)  # skip first value in iteration
    iter_v2 = iter(my_dict)  # set second iteration value
    next(iter_v2)  # skip first value in iteration
    for i, key in zip(iter_v1, iter_v2):  # for loop with two iteration values
        num = Decimal((i[0][year_index]))  # find value in dictionary
        if num > maxi:  # find max value
            key_name = key
            maxi = num
    return key_name, round(maxi, 6)  # return key_name and maximum value


def minimum(year):
    """
    The minimum function receives the year string as a parameter and calculates the
    minimum value of all emissions for the selected year
    :param year string
    :return: key_name string and minimum decimal
    """
    year_index = my_dict['CO2 per capita'][0].index(year)  # find index of the year
    mini = 100
    key_name = ""
    iter_v1 = iter(my_dict.values())  # set first iterator value
    next(iter_v1)  # skip first value in iteration
    iter_v2 = iter(my_dict)  # set second iteration value
    next(iter_v2)  # skip first value in iteration
    for i, key in zip(iter_v1, iter_v2):  # for loop with two iteration values
        num = Decimal((i[0][year_index]))  # find value in dictionary
        if num < mini:  # find min value
            key_name = key
            mini = num
    return key_name, round(mini, 6)  # return key_name and minimum value


def year_check():
    """
    The year_check function prompts the user to enter a year and then checks if the year
    is a valid selection by comparing it to the values in the my_dict dictionary
    :return: year string
    """
    while True:
        year = input("Select a year to find statistics (1997 to 2010): ")
        try:
            if year in my_dict['CO2 per capita'][0]:  # check if year is in dictionary
                break
            else:
                print("\nSorry that is not a valid year\n")
        except ValueError:
            print("\nSorry that is not a valid year\n")
    return year  # return validated year string


def save_data(save_list):
    """
    The save_data function receives the save_list list as a parameter and writes the values
    from this list into the Emissions_subset.csv
    :param save_list list
    """
    file_name = 'Emissions_subset.csv'
    countries = []
    for i in range(len(save_list)):  # loop through list
        word_list = save_list[i].split(",")  # split list with "," as the delimiter
        countries.append(word_list[0])  # extract the first value of the list to use for countries print
    try:
        with open(file_name, 'w') as f:  # check if file is writeable
            # set delimiter and escape character
            wr = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=' ', escapechar=' ')
            for row in save_list:  # loop through list
                wr.writerow(map(str, row))  # write each line into the csv file
            print("Data successfully extracted for countries", countries, "saved into file", file_name)
    except IOError:
        print(file_name, "cannot be written to.")
        exit()  # exit program if the file cannot be written to


def country_plot(country_vis):
    """
    The country_plot method receives the country_vis string as a parameter and
    uses this selection to create a graph
    :param country_vis string
    """
    xlist = []  # x values
    ylist = []  # y values

    for i in my_dict['CO2 per capita'][0]:  # extract list of years
        xlist.append(i)
    for j in my_dict[country_vis][0]:  # extract emissions lists
        ylist.append(round(Decimal(j), 2))
    plt.xlabel("Year")
    plt.ylabel("C02 emissions")
    plt.title("Emissions Plot for " + country_vis)
    plt.plot(xlist, ylist, 'o-')  # plot graph
    plt.show()  # display graph
    print("\nPlot for", country_vis, "opens in a new window.")


def check_countries():
    """
    The check_countries method prompts the user for a list of countries and checks
    that these countries are valid entries before formatting and returning them
    :return: new_list list
    """
    text_list = []
    new_list = []
    while True:
        text_list.clear()  # clear lists at start of each loop
        new_list.clear()

        text = input("Write up to three comma-separated countries for which you want to "
                     "extract data: ").strip().lower()  # remove white space and set to lower case
        for i in text.split(","):
            text_list.append(i.title().strip())  # split the list and format for use

        for x in range(len(text_list)):
            if text_list[x] not in my_dict:  # check that the country is not in list
                print("ERR: Sorry", text_list[x], "is not a valid country\n")
                new_list.clear()
                break
            else:  # if country is in list append it to the new_list and format for use
                new_list.append(str(text_list[x]) + "," +
                                str(my_dict.get(text_list[x])).
                                replace("[", "").
                                replace("]", "").
                                replace(" ", "").
                                replace("'", ""))
        if len(new_list) > 3:  # check that no more than 3 coutries are selected
            print("ERR: Sorry, at most 3 countries can be entered.")
        elif len(new_list) == 0:  # check that user has entered at least 1 country
            pass
        else:
            break
    return new_list  # return new_list list


def check_country():
    """
    The check_country method prompts the user to enter a country and then checks
    that the entry is valid before returning the country
    :return: country string
    """
    while True:
        # receive and format country
        country = input("Select the country to visualize: ").strip().lower().title()
        if country not in my_dict:  # check if country is not in my_dict
            print("ERR: Sorry", country, "is not a valid country")
        else:
            break
    return country  # return validated country string


def main():
    """
    The main method is the starting point for this program and calls the following functions:
    get_file, year_check, minimum, maximum, average, save_data, check_countries, country_plot, check_country
    """
    print("A Simple Data Analysis Program\n\n** Job 1 **")
    get_file()  # read file into dictionary

    print("\n** Job 2 **")
    year = year_check()  # set year from year_check function call

    # set min_country and min_emission from minimum function call
    min_country, min_emission = minimum(year)

    # set max_country and max_emission from maximum function call
    max_country, max_emission = maximum(year)

    # print min, max and average values
    print("\nIn", year, "the countries with the minimum and maximum CO2 emission levels were:",
          "\nMaximum:", max_country, "with an emission value of:", max_emission,
          "\nMinimum:", min_country, "with an emission value of:", min_emission,
          "\nAverage CO2 emissions in", year, "were", average(year))

    print("\n** Job 3 **")
    # write data to file using the save_data function call which calls the check_countries return value
    save_data(check_countries())

    print("\n** Job 4 **")
    # plot graph using country_plot function call which call the check_country return value
    country_plot(check_country())

    print("Thanks for using this program.")
    input()  # keeps console open until user closes


main()
