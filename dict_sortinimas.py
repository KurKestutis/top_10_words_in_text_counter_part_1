# zodziai = {'vienas': 1, 'du': 2, 'trys': 3, 'keturi': 4, 'penki': 5, 'šeši': 6, 'septyni': 7, 'aštuoni': 8}
#
# sorted_zodziai = sorted(zodziai.items(), key=lambda kv: kv[0])
#
# print(sorted_zodziai[0])
# print(sorted_zodziai[1])

# It can often be very handy to use namedtuple. For example, you have a dictionary
# of 'name' as keys and 'score' as values and you want to sort on 'score':
import collections
Player = collections.namedtuple('Player', 'score name')
d = {'John':5, 'Alex':10, 'Richard': 7}

# sorting with lowest score first:
worst = sorted(Player(v,k) for (k,v) in d.items())

# sorting with highest score first:
best = sorted([Player(v,k) for (k,v) in d.items()], reverse=True)

# Now you can get the name and score of,
# let's say the second-best player (index=1) very Pythonically like this:

# player = best[1]
# player.name
#     'Richard'
# player.score
#     7

print(best[1])
print(best[1].name)
print(best[1].score)



