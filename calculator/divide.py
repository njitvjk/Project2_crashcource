import pandas as pd
cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['VALUE_A', 'VALUE_B'])
cities.to_csv('../done/test.csv',mode='a', index=False, header=False)

operations = pd.DataFrame([['add', 1, 2, 3]], columns=['OPERATION', 'VALUE_A', 'VALUE_B',
                                                                                  'RESULT'])
operations.to_csv('data.csv', mode='a', index=False, header=False)
