\ Model lp2
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - 3 x[0] - 2 x[1] + 20 Constant
Subject To
 c[0]: 5 x[0] + 4 x[1] + x[2] = 4
 c[1]: 3 x[0] + 2 x[1] + x[3] = 3
 c[2]: 2 x[0] + x[1] + x[4] = 2
Bounds
 Constant = 1
End
