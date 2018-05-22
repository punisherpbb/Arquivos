import pandas as pd
import numpy as np

d = [321, 331, 414, 484, 123, 634]
t = [0, 1, 2, 3, 4, 5]

df = list(zip(d, t))

dff = pd.DataFrame(df)

c = pd.DataFrame(df, index=pd.date_range('20180511', periods=6), columns=['teste1', 'teste2'])

print(c['teste2'])

'''
d1 = pd.Series(d, name='teste')
d1.index = pd.date_range('20180511', periods=6)
'''

'''
Tipo dos dados
d1 = d1.astype(np.int)
print(d1.dtype)
'''

'''
Zerar os valores nulos(NaN)
d1[1:3] = np.NaN
print(d1)
d1.fillna(0, inplace=True)
print(d1)
'''
