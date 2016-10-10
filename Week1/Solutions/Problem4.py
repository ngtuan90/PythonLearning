# Write a function that asks the user for a string containing multiple words. Print
# back to the user the same string, except with the words in backwards order. 

def reverse(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0,word)
  return " ".join(result)

# test code
test1 = raw_input("Enter a sentence: ")
print reverse(test1)
