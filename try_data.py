import pandas as pd

from imports import *

a = pd.DataFrame({
    'revenue': [10, 20, 30, 40, 50],
    'income': [10, 11, 12, 13, 15]
})
a.plot()
plt.show()
print(a)
