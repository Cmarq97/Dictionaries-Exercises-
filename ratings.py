
# restaurant_ratings = {
#     "Florean Fortescue's Ice Cream Parlour": 4,
#     "Jellied Eel Shop": 3,
#     "The Tavern": 3,
#     "Luchino Caffe": 1,
#     "The Porcupine": 5,
#     "Diagon Alley cafe": 2,
#     "The Bear & Staff": 2,
#     "Ministry Munchies": 1,
#     "Chip Shop": 3,
#     "Eternelle's Elixir of Refreshment": 5,
#     "Big Bean Shack": 3,
#     "The Club": 2,
# }
scores = open('scores.txt')
restaurant_ratings = {}
for rating in scores:
    ratings = rating.rstrip()
    restaurant_name, restaurant_rating = ratings.split(":")
    restaurant_ratings[restaurant_name] = int(restaurant_rating)


def rating_lister(restaurant_ratings):
    """Restaurant Rating Lister"""
    name = raw_input("Enter Restaurant Name: ")
    rating = int(raw_input("Please Enter Restaurant Rating: "))
    restaurant_ratings[name] = rating
    sorted_ratings = sorted(restaurant_ratings.items())
    for items in sorted_ratings:
        print ("%s is rated at %d" %
              (items[0], items[1]))

rating_lister(restaurant_ratings)
