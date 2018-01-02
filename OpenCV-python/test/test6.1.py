import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import svm


os.chdir('/home/mohneesh/Desktop/ML/handwritten-character-recognition-ocr/Dataset/output')
dfa= pd.read_csv('A.csv',header=None)
dfb= pd.read_csv('B.csv',header=None)
dfc= pd.read_csv('C.csv',header=None)
dfd= pd.read_csv('D.csv',header=None)
dfe= pd.read_csv('E.csv',header=None)
dff= pd.read_csv('F.csv',header=None)
dfg= pd.read_csv('G.csv',header=None)
dfh= pd.read_csv('H.csv',header=None)
dfi= pd.read_csv('I.csv',header=None)
dfj= pd.read_csv('J.csv',header=None)
dfk= pd.read_csv('K.csv',header=None)
dfl= pd.read_csv('L.csv',header=None)
dfm= pd.read_csv('M.csv',header=None)
dfn= pd.read_csv('N.csv',header=None)
dfo= pd.read_csv('O.csv',header=None)
dfp= pd.read_csv('P.csv',header=None)
dfq= pd.read_csv('Q.csv',header=None)
dfr= pd.read_csv('R.csv',header=None)
dfs= pd.read_csv('S.csv',header=None)
dft= pd.read_csv('T.csv',header=None)
dfu= pd.read_csv('U.csv',header=None)
dfv= pd.read_csv('V.csv',header=None)
dfw= pd.read_csv('W.csv',header=None)
dfx= pd.read_csv('X.csv',header=None)
dfy= pd.read_csv('Y.csv',header=None)
dfz= pd.read_csv('Z.csv',header=None)


# train = df[:60]		# Partitioning the data to training and testing sets ( 60% - 40% )
# test = df[-40:]

# plt.plot(train[:40],test)
# plt.show()

# a=np.array(df)
df = [dfa,dfb,dfc,dfd,dfe,dff,dfg,dfh,dfi,dfj,dfk,dfl,dfm,dfn,dfo,dfp,dfq,dfr,dfs,
      dft,dfu,dfv,dfw,dfx,dfy,dfz]
dfar = np.array(df)
print dfar.shape

