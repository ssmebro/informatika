def pen_cost(num_pens : int, message : str) -> float:
  return num_pens * (75.55 + (len(message) * 2.52))

def test_pens():
  assert pen_cost(3, "Газпром") == 279.57
  assert pen_cost(1, "Серёжа") == 90.67
  assert pen_cost(3, "ЧГК") == 249.33
  
'''Последний тест выдаёт ошибку'''