# import sklearn
from sklearn import StratifiedKFold, KFold 
import numpy as np 
X, y = np.ones((50, 1)), np.hstack(([0] * 45, [1] * 5)) 
skf = StratifiedKFold(n_splits=3) 
for train, test in skf.split(X, y): 
    print('train - {} | test - {}'.format( np.bincount(y[train]), np.bincount(y[test]))) 

kf = KFold(n_splits=3) 
for train, test in kf.split(X, y): 
    print('train - {} | test - {}'.format( np.bincount(y[train]), np.bincount(y[test]))) 
