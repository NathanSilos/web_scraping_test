from scrap import import_countries
from functions import *

# Importing countries with web scraping
countries = import_countries()

# Calculating the top 3 coutries with the biggest area
three_biggest_countries(countries)

# Calculate the rank with all countries with Bubble Sort
pop_rank = population_rank(countries)

i = 0
print('Above the rank of countries with the highest population:')
while i != len(pop_rank):
    print(i + 1, '° :', pop_rank[i][0], '- População:', pop_rank[i][1])
    i += 1

