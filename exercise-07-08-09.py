def all_z_words(wordlist : list) -> list:
  zlist = []
  for wd in wordlist:
    if "z" in wd:
      zlist = [wd] + zlist
  return(zlist)
  
def test_all_z_words():
  assert all_z_words(["asd","zxc","qwe"]) == ["zxc"]
  assert all_z_words(["zx","as","ds"]) == ["zx"]
  assert all_z_words([]) == []
  assert all_z_words(["asd","qe","z","123z"]) == ["123z","z"]



def all_z_words_2(lst : list) -> list:
  am = list(filter(lambda wd: "z" in wd, lst))
  return am

def test_all_z_words_2():
  assert all_z_words_2(["фыавфы","йцк","qfasd","zq"]) == ["zq"]
  assert all_z_words_2(["фыаыфв","ауцыфа","мсмвыа"]) == []
  assert all_z_words_2([]) == []
  assert all_z_words_2(["длоа","кцйуцй","z","123z"]) == ["z","123z"]
  
  
  
"""В первой функции мы добавляем каждое новое слово в начало, 
и происходит смещение, то есть ответ получается зеркальным.
А при использовании `filter` у нас все элементы остаются в том же порядке"""