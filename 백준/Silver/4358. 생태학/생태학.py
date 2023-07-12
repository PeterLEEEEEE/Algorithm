import sys

input = sys.stdin.readline

species_dict = {}
count = 0
while True:
  specie = input().rstrip()

  if not specie:
    break
  count += 1
  species_dict[specie] = species_dict.get(specie, 0) + 1

sorted_dict = dict(sorted(species_dict.items(), key=lambda x: x[0]))

for specie in sorted_dict:

  specie_p = (sorted_dict[specie]) / count * 100
  print("%s %0.4f" %(specie, specie_p))

