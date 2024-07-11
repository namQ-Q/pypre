import pandas as pd
df = pd.DataFrame({'name' : ['김지훈', '이유진', '박동현', '김민지'],
'english' : [90, 80, 60, 70],
'math'  : [50, 60, 100, 20]})
df
sum(df['english'])
sum(df['math'])
sum(df['english'])/4
sum(df['math'])/4

df = pd.DataFrame({'제품' : ['사과', '딸기', '수박'],
'가격'  : [1800, 1500, 3000],
'판매량'  : [24, 38, 13]})
df
sum(df['가격'])/3
sum(df['판매량'])/3

df_exam = pd.read_csv('C:\\Users\\USER\\Documents\\LS빅데이터스쿨\\교재 파일\\exam.csv')
df_exam.head()

sum(df_exam['english'])/20
sum(df_exam['science'])/20

len(df_exam)

sum(df_exam['english']) / len(df_exam)
sum(df_exam['science']) / len(df_exam)

df_exam_novar = pd.read_excel('excel_exam_novar.xlsx')
df_exam_novar
df_exam_novar = pd.read_excel('excel_exam_novar.xlsx', header = None)
df_exam_novar

df_midterm = pd.DataFrame({'english'  : [90, 80, 60, 70],
'math'  : [50, 60, 100, 20],
'nclass'  : [1, 1, 2, 2]})
df_midterm
df_midterm.to_csv('output_newdata.csv')
df_midterm.to_csv('output_newdata.csv', index = False)

import pandas as pd
exam = pd.read_csv('exam.csv')
exam.head()
exam.tail()
exam.shape
exam.info()
exam.isnull().sum()
exam.describe()

mpg = pd.read_csv('mpg.csv')
mpg.head()
mpg.tail()
mpg.shape
mpg.isnull().sum()
mpg.info()
mpg.describe()
mpg.describe(include = 'all')
mpg.nunique()
mpg.count()

df_raw = pd.DataFrame({'var1' : [1, 2, 3],
'var2'  : [2, 3, 2]})
df_raw
df_new = df_raw.copy()
df_new
df_new = df_new.rename(columns = {'var2' : 'v2'})
df_new
df_new = df_new.rename(columns = {'var1' : 'v1'})
df_new
df_new = df_new.rename(columns = {'v1' : 'v11',
'v2' : 'v22'})
df_new

import pandas as pd
df_mpg = pd.read_csv('mpg.csv')
df_mpg
df_new_mpg = df_mpg.copy()
df_new_mpg
df_new_mpg = df_new_mpg.rename(columns = {'cty' : 'city'})
df_new_mpg = df_new_mpg.rename(columns = {'hwy' : 'highway'})
df_new_mpg.head()

df = pd.DataFrame({'var1' : [4, 3, 8],
                  'var2' : [2, 6, 1]})
df
df['var_sum'] = df['var1'] + df['var2']
df
df['var_mean'] = (df['var1'] + df['var2']) / 2
df

mpg = df_new_mpg
mpg
mpg['total'] = (mpg['city'] + mpg['highway']) / 2
mpg.head()
sum(mpg['total']) / len(mpg)

mpg['total'].mean()
mpg['total'].describe()
mpg['total'].plot.hist()

import numpy as np

import matplotlib.pyplot as plt
mpg['total'].plot.hist()
plt.show()

mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')
mpg.head()
mpg['test'].value_counts()

count_test = mpg['test'].value_counts()
count_test.plot.bar()
plt.show()
count_test.plot.bar(rot = 0)
plt.show()

mpg['grade'] = np.where(mpg['total'] >= 30, 'A',
              np.where(mpg['total'] >= 20, 'B', 'C'))
mpg.head()

count_grade = mpg['grade'].value_counts()
count_grade
count_grade.plot.bar(rot = 0)
plt.show()

plt.clf()

count_grade = mpg['grade'].value_counts().sort_index()
count_grade
count_grade.plot.bar(rot = 0)
plt.show()

mpg['grade2'] = np.where(mpg['total'] >= 30, 'A',
                np.where(mpg['total'] >= 25, 'B',
                np.where(mpg['total'] >= 20, 'C', 'D')))
mpg.head()

mpg['size'] = np.where((mpg['category'] == 'compact') |
                        (mpg['category'] == 'subcompact') |
                        (mpg['category'] == '2seater'),
                        'small', 'large')

mpg['size'].value_counts()

mpg['size'] = np.where(mpg['category'].isin(['compact', 'subcompact', '2seater']), 'small', 'large')
mpg['size'].value_counts()


df = pd.read_csv('midwest.csv')
df
df.shape
df.head()
df.info()
df.describe()

df = df.rename(columns = {'poptotal' : 'total', 'popasian' : 'asian'})
df.info()

df['asian']
df['total']

df['per_asian'] = (df['asian'] / df['total']) * 100
df['per_asian']
df['per_asian'].plot.hist()
plt.show()

plt.clf()

df['var'] = np.where(df['per_asian'] > sum(df['per_asian']) / len(df), 'large', 'small')
df['var']

df['var'].value_counts()
count_var = df['var'].value_counts()
count_var.plot.bar(rot = 0)
plt.show()

plt.clf()
