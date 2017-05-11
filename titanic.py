try:
   import os
   import pandas as pd
   import matplotlib.pyplot as plt
except ImportError: 
   print("IMPORT ERROR")
	
x=[1,2,3,4]
y=[4,5,6,7]
plt.hist(x,bins=x,color="b",width=.5)
plt.legend()
plt.show()

