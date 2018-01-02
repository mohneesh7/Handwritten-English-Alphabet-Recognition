from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets

digits = datasets.load_digits()
# print digits

X = StandardScaler().fit_transform(digits.data)
print X.shape

pca = PCA(n_components=0.99, whiten=True)
print pca

X_pca = pca.fit_transform(X)
print X_pca