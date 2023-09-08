import math


def get_expected_cost(beds, baths):
    value = 80000
    if beds:
        value = value + beds * 30000
    if baths:
        value = value + baths * 10000
    return value
print(get_expected_cost(1, 2))

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = (math.ceil((sqft_walls + sqft_ceiling) / sqft_per_gallon)) * cost_per_gallon
    return cost

print(get_cost(432, 144, 400, 15))