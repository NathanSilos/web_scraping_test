
# Selecting the three highest countries
def three_biggest_countries(countries):

    # Declaring rank one 
    size_one = 0
    rank_one = ''

    # Declaring rank two
    size_two = 0
    rank_two = ''

    # Declaring rank three
    size_three = 0
    rank_three = ''

    # Calculate Ranks
    for country in countries:
        # Finding the biggest country
        if  countries[country]['area']> size_one:
            rank_one = country
            size_one = countries[country]['area']
        
        # Finding the second larger country
        elif countries[country]['area']> size_two:
            rank_two = country
            size_two = countries[country]['area']
        # Third country
        elif countries[country]['area']> size_three:
            rank_three = country
            size_three = countries[country]['area']
    
    # Printing the result
    print(f'''
    The rank of the biggests coutries on Earth is:
    1°- {rank_one} {size_one} km²
    2°- {rank_two} {size_two} km²
    3°- {rank_three} {size_three} km²
    ''')

# Ordering the rank of countries with the highest population
def population_rank(countries):

    rank = []
    limit = 0
    limit_name = ''
    # Looping in every country
    for country in countries:
        rank.append((country, countries[country]['population']))

    # Bubble Sort to organize the countries
    ordenado = False
    while not ordenado:
        #print(rank[i][1], rank[i + 1][1])
        ordenado = True
        for j in range(len(rank) - 1):
            if rank[j][1] < rank[j + 1][1]:
                rank[j], rank[j + 1] = rank[j + 1], rank[j]
                ordenado = False

    return(rank)