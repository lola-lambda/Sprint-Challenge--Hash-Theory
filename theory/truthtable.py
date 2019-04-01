# !(A || B) || ( (A || C) && !(B || !C) )
# not (A or B) or ((A or C) and not (B or not C))
for A in [False, True]:
  for B in [False, True]:
    for C in [False, True]:
      print(f"A: {A} B: {B} C: {C} ---- {not (A or B) or ((A or C) and not (B or not C))}")