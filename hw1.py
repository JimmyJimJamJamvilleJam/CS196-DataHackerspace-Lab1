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


    return ''


def weigh_pokemons(filename, weight):
    with open(filename) as f:
        pokemon_data = json.load(f)
    pokemons = []
    for pokemon in pokemon_data['pokemon']:
        if pokemon['weight'] == str(float(weight)) +  " kg" :
            pokemons.append(pokemon['name'])
    return pokemons


def single_type_candy_count(filename):
    with open(filename) as f:
        pokemon_data = json.load(f)
    count = 0
    #print(pokemon_data['candy_count'])
    for pokemon in pokemon_data['pokemon']:
        #print(pokemon['candy_count'])
        #if pokemon['candy_count'] != '':
         #   count += pokemon['candy_count']
        print(count)
    return count


def reflections_and_projections(points):
    arr = np.array(points)
    temp = np.copy(arr[1])
    arr[1] = arr[0]
    arr[0] = temp
    print(arr)

    x = np.pi / 2
    rotate_matrix = [[np.cos(x), -np.sin(x)], [np.sin(x), np.cos(x)]]

def normalize(image):
    pass


def sigmoid_normalize(image):
    pass


def main():
    #histogram_times('airplane_crashes.csv')
    #single_type_candy_count('pokedex.json')
    arr_2d = np.array([np.arange(2 * i, 10 * i + 5) for i in range(10)])
    reflections_and_projections([[1,2,3],[4,5,6]])
main()