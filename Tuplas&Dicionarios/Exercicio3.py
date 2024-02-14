dictionary = {
    'first':22,
    'second':33,
    'thirt':44,
    'fourth':22
}


def found(dictionary,value):
   for key, element in dictionary.items():
      if element==value:
         print(key)


found(dictionary,22)