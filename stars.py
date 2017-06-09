x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(x):
    i = 0
    while i < len(x):
        if isinstance(x[i],int) == True:
            print ('*' * (x[i]))
            i += 1
        elif isinstance(x[i],str) ==  True:
            print x[i][:1].lower()*len(x[i])
            i += 1
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
