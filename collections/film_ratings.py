# possible film ratings are "universal", "pg", "12", "12a", "15", "18"

print("\n-------------------------------------------")
film_rating = "12a"

# use an if statement to check for "universal" rating
if film_rating.lower() == "universal":
    print("all age groups can watch this film")

# check if film rating is "pg"
elif film_rating.lower() == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")

# check if film rating is "12" or "12a"
elif (film_rating == "12") | (film_rating.lower() == "12a"):
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")

# check if film rating is "15"
elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")

# check if film rating is "18"
elif film_rating == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")

# ELSE STATEMENT GOES HERE
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")




print("\n-------------------------------------------")