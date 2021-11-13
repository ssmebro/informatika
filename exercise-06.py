def sum_list(numlist : list) -> float:
  run_total = 0
  for num in numlist:
    run_total = run_total + num
  return run_total

def test_sum():
  assert sum_list([1,2,3]) == 6
  assert sum_list([102,-100,-2]) == 0
  assert sum_list([0.5,-0.3,0.2]) == 0.4