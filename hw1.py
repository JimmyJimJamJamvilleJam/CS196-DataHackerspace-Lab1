#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np


def histogram_times(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)

    times = []
    for x in range(len(airplane_data)):
        if airplane_data[x][1] != '':
            times.append(airplane_data[x][1])

    strTime = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
               '18', '19', '20', '21', '22', '23']

    timesArray = [0 for i in range(23)]
    print(timesArray)
    for time in range(23):
        for x in range(len(times)):
            num = times[x][:2]
            if (num == strTime[time]):
                timesArray[time] = timesArray[time] + 1
    return timesArray


def weigh_pokemons(filename, weight):
    with open(filename) as f:
        pokemon_data = json.load(f)
    pokemons = []
    for pokemon in pokemon_data['pokemon']:
        if pokemon['weight'] == str(float(weight)) + " kg":
            pokemons.append(pokemon['name'])
    return pokemons


def single_type_candy_count(filename):
    with open(filename) as f:
        pokemon_data = json.load(f)
    count = 0
    print(pokemon_data)
    #for pokemon in pokemon_data['pokemon']:
        # print(pokemon['candy_count'])
        # if pokemon['candy_count'] != '':
        #   count += pokemon['candy_count']
        #print(count)
    return count


def reflections_and_projections(points):
    arr = np.array(points)
    temp = np.copy(arr[1])
    arr[1] = arr[0]
    arr[0] = temp

    x = np.pi / 2
    rotate_matrix = np.array([[0, -1], [1, 0]])

    arr = np.dot(rotate_matrix, arr)

    linear_matrix = np.array([[1 / 10, 3 / 10], [3 / 10, 9 / 10]])

    arr = np.dot(linear_matrix, arr)

    return arr


def normalize(image):
    colours = np.array(image)
    max = colours[0][0]
    min = colours[0][0]
    for i in range(32):
        for j in range(32):
            if colours[i][j] > max:
                max = colours[i][j]
            if colours[i][j] < min:
                min = colours[i][j]

    print(min, max)
    for i in range(32):
        for j in range(32):
            colours[i][j] = (255 / (max - min)) * (colours[i][j] - min)
    return colours


def sigmoid_normalize(image):
    pass


def main():
    #print(histogram_times('airplane_crashes.csv'))
     single_type_candy_count('pokedex.json')
    # arr_2d = np.array([np.arange(2 * i, 10 * i + 5) for i in range(10)])
    # reflections_and_projections([[1,2,3],[4,5,6]])
    # print(normalize([[1,2,3],[4,5,6]]))


main()
