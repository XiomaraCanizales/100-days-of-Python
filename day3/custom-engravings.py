def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + len(engraving) * 10
    else:
        cost = 50 + len(engraving) * 7
    return cost

print(cost_of_project('xiomara', True))