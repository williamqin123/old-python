def find_factor():
  
  num = input("Enter a number: ")
  
  print "The factors of %s are: " % str(num)
  
  factor = 1
  
  while factor <= num:
    
    if num % factor == 0:
      
      print factor
      
    factor = factor + 1
    
  find_factor()
  
find_factor()
