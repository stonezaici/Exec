import numpy as np
import pandas as pd

import matplotlib_exec.pyplot as plt

a = np.random.randn(30, 2)
a.round(2)
df = pd.DataFrame(a)

df.columns = ['Data1', 'Data2']
dates = pd.date_range('2017-1-1', periods=len(a), freq='D')
df.index = dates
df.plot()
plt.show()