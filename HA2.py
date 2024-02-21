# 1. Pandas series can be created from Lists, Dictionaries(and scalar values).
# 2. 
import pandas as pd 
a = [1,2,3,4,5,6,7,8,9,10,11,12] 
myvar=pd.Series(a, index = ["January", "February", "March", "April","May", "June", "July","August","September","October","November","December"])
print(myvar)

