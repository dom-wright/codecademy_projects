from hashmap import HashMap


flowers_map = HashMap(5)

flower_definitions = [
    ['begonia', 'cautiousness'],
    ['chrysanthemum', 'cheerfulness'],
    ['carnation', 'memories'],
    ['daisy', 'innocence'],
    ['hyacinth', 'playfulness'],
    ['lavender', 'devotion'],
    ['magnolia', 'dignity'],
    ['morning glory', 'unrequited love'],
    ['periwinkle', 'new friendship'],
    ['poppy', 'rest'],
    ['rose', 'love'],
    ['snapdragon', 'grace'],
    ['sunflower', 'longevity'],
    ['wisteria', 'good luck']
]

for key, value in flower_definitions:
    flowers_map.assign(key, value)

for counter, ll in enumerate(flowers_map.array):
    print("HashMap array index:", counter)
    print(ll.stringify_list())

for key, value in flower_definitions:
    print(key, "-", flowers_map.retrieve(key))
