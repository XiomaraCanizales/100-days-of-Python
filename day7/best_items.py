def best_items(racers):
    """ Given a list of racer dictionaries, return a dictionary mapping items to the number of
        items those items were picked up by racers who finish in first place """
    winner_item_counts = {}
    for i in range(len(racers)):
        # the i'th racer dictionary
        racer = racers[i]
        # only those who finished first
        if racer['finish'] == 1:
            for item in racer['items']:
                # add one to the count for this item
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
            winner_item_counts[item] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(i+1, len(racers), racer['name']))
            
    return winner_item_counts

sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]

print(best_items(sample))