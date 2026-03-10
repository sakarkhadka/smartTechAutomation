def sort(width, height, length, mass):
  bulky, heavy = False, False
  
  if width >= 150 or height >= 150 or length >= 150 or length*width*height >= 1000000:
    bulky = True
    
  if mass >= 20:
    heavy = True
    
  if bulky and heavy:
    return "REJECTED"
  if bulky or heavy:
    return "SPECIAL"
  return "STANDARD"

#standard case, prints STANDARD
print(sort(100, 100, 10, 10))
#bulky case, prints SPECIAL
print(sort(100, 100, 100, 10))
#heavy case, prints SPECIAL
print(sort(100, 100, 10, 25))
#both case(bulky and heavy), prints REJECTED
print(sort(100, 100, 100, 100))
#edge case, prints SPECIAL
print(sort(150, 10, 10, 10))
#edge case, prints SPECIAL
print(sort(10, 10, 10, 20))
