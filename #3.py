#3
import pandas as pd 
groups = {"MatMIE": 30, "MatDAIS": 29, "COMIE": 40, "COMEC":53}

myvar = pd.Series(groups)

print(myvar)