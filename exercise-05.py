def pos_neg_zero(n : float) -> str:
  if n > 0:
    return "pos"
  elif n < 0:
    return "neg"
  else:
    return "zero"
    
numbers = [1,3,-2,0.2,0,-9.3]
pos_neg_zero = list(map(pos_neg_zero, numbers))
print(pos_neg_zero)


def len5(string : str) -> bool:
  if len(string) == 5:
    return True
  else:
    return False
    
def thereare5(l : list) -> bool:
  if len(list(filter(lambda wd: False == wd, l))) > 0:
    return False
  else:
    return True

words = ["абвгд", "абвul", "", "фывап"]    
print(thereare5(list(map(len5, words))))


rnumbers = [20, 16, 10, 15, 30, -2, 39, 0]     
chet_num = list(filter(lambda num: num % 2 == 0, rnumbers))          
chet10to20 = list(filter(lambda num1: 10 <= num1 <= 20, chet_num))
print(chet10to20)
