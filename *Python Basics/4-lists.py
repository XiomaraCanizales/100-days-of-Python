flowers_lists = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]
print(flowers_lists)
print(type(flowers_lists))
#length
print(len(flowers_lists))
# slincing
print("First three entries: ", flowers_lists[:3])
print("Final two entries: ", flowers_lists[-2])
# removing items
flowers_lists.remove("globe thistle")
print(flowers_lists)
# adding items
flowers_lists.append("snapdragon")
print(flowers_lists)

# with numbers:
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
print("Length of the list: ", len(hardcover_sales))
print("Entry at index 2: ", hardcover_sales[2])
# max and min
print("Maximum: ", max(hardcover_sales))
print("Minimum: ", min(hardcover_sales))
# calculations
print("Total sold: ", sum(hardcover_sales))