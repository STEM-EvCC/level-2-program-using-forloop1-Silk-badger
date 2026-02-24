mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#This is doable in 10 or 11 lines - Just use for loops.

total = len(mission_names); success = 0
for t in range(total):
    if mission_success[t]: success += 1
#Variable used is t for total
print(f"Total number of missions: ", len(mission_names))
print("\n", f"Number of successful missions: {success}")
print("\n", f"Success Rate: {success/total*100:.2f}%")
print("\n", f"Missions before 2000: ")
#initally had an error, but it was because I forgot to use f before the text. 
for t in range(total):
     if mission_years[t] < 2000: print(f"{mission_names[t]}")