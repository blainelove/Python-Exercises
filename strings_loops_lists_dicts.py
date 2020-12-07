# Task A. String manipulation (function 'string_manip')
#   Remove any leading and trailing spaces from the input string
#   Convert the input string to upperscase
#   Replace any remaining spaces with the pound sign '#'
#   If the remaining string consists entirely of digits (0..9), just return that string.
#   If the remaining string is a single character just return that string.
#   Otherwise, return a the string in reverse

def string_manip(s):
  line = s.strip().upper().replace(' ','#')
  try: #testing to see if the string is only digits 
    line = int(line)
    return str(line) 
  except:
    if len(line) == 1:
      return line
    else:
      return line[::-1] 


# Task B. Loops (function 'bananas')
# Given an integer count, return a string
# of the form '1 banana, 2 banana, ..., <count> banana', where <count> is the number
# passed in.  There are some special rules:
#   If the count is zero, return 'no bananas'
#   If the count is one, return 'a banana'
# However, if the count is 6 or more, then use the string
# ' and <num> more bananas' as the last item instead of the actual list of bananas,
# where <num> is the number of remaining bananas.  Note that in this case, there should
# be *no comma* between the last numbered banana and the "and <n> more bananas" string.
#
# Examples:
#     bananas(0)  returns 'no bananas'
#     bananas(3)  returns '1 banana, 2 banana, 3 banana'
#     bananas(5)  returns '1 banana, 2 banana, 3 banana, 4 banana, 5 banana'
#     bananas(10) returns '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 5 more bananas'  # note: no final comma
#     bananas(20) returns '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 15 more bananas'

def bananas(count):
  countlist = [] #initializing an empty list to add banana counts to later 
  countstring = "" #initializing an empty string to add banana counts to later from countlist 
  if count == 0:
    return ('no bananas')
  elif count == 1:
    return ('a banana')
  elif count < 6:
    for numb in range(1, count+1): #so range doesn't include 0 
      countlist.append(str(numb)+' '+'banana') #adding banana counts as items in countlist 
    for item in countlist:
      countstring = countstring+item+', ' #adding items from countlist into empty string 
    countstring = countstring[:-2] #keeps final comma from printing 
    return (countstring)
  else:
    for numb in range(1, count+1): 
      countlist.append(str(numb)+' '+'banana')  
    surplus = len(countlist[5:]) #saving the surplus of bananas to variable surplus 
    for item in countlist[0:5]: #only first 5 items print out individually 
      countstring = countstring+item+', ' 
    countstring = countstring[:-2] 
    countstring = countstring + " and " + str(surplus) + ' more bananas'
    return (countstring)


# Task C. Palindromes
#
# Given a string, determine if the string is a palindrome.
#
# Examples:
#     palidrome('anna')  returns 'True'
#     palidrome('abcdef')  returns 'False'
#     palidrome('')  returns 'True'

def palindrome(word):
  if word == word[::-1]:
    return True 
  else:
    return False 


# Task D. Dictionaries and sorting (function 'name_counts')
#
# Given a list of strings, return a list of tuples containing the counts of each of the
# UNIQUE strings. The returned results should be ordered by the counts
# in decreasing order. In case of ties of counts, break the tie by string value in increasing order.
#
# Examples:
#   name_counts(['Becca', 'Catherine', 'Catherine', 'Catherine', 'Christopher', 'Christopher'])
# should return [('Catherine', 3), ('Christopher', 2), ('Becca', 1)]
#
#   name_counts(['Christopher', 'Mike', 'Becca', 'Christopher', 'Bacon', 'Catherine', 'Christopher', 'Becca'])
# should return [('Christopher', 3), ('Becca', 2), ('Bacon', 1), ('Catherine', 1), ('Mike', 1)])

def name_counts(names):
  name_d = {} #initializing an empty dictionary to use as a counter
  for name in names:
    if name not in name_d:
      name_d[name] = 1 #if the name is not in the dictionary, add name
    else:
      name_d[name] += 1 #if the name is in the dictionary, increase count by 1 
  sorted_name_d = [x for x in sorted(name_d.items(), key=lambda kv: (-kv[1], kv[0]))]
  return sorted_name_d