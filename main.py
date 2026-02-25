mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#This is doable in 10 or 11 lines - Just use for loop.

total = len(mission_names); success = 0 #Base line for missions and the success rate in guaranteed neumerical form.
for t in range(total):
    if mission_success[t]: success += 1 #This adds onto the successful counter, deciding based off the true/false list above.
#Variable used is t for total
print(f"Total number of missions: ", len(mission_names)) #This prints the overall mission amount.
print("\n", f"Number of successful missions: {success}") #This prints the successful mission amount.
print("\n", f"Success Rate: {success/total*100:.2f}%") #This calculates the success rate while also rounding the number to it's second decimal point.
print("\n", f"Missions before 2000: ") #This prints the number of missions before 2000.
#initally had an error, but it was because I forgot to use f before the text. 
for t in range(total):
     if mission_years[t] < 2000: print(f"{mission_names[t]}") #Finds out which versions are before 2000, and prints them one by one.

     #I made the concious choice of adding \n for spacing, just to make it easier to read (in my opinion).