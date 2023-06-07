from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# preparation of dataset, train_set, test_set

dset_iris = load_iris()
print("type(dset_iris) =\n", type(dset_iris))
print("dset_iris['DESCR'] =\n", dset_iris['DESCR'])
print("dset_iris['data'] =\n", dset_iris['data'])
target_class = dset_iris['target']
print("dset_iris['target'] =\n", target_class)
target_names = dset_iris['target_names']
print("dset_iris['target_names'] = ", target_names)
X, y = load_iris(return_X_y = True)
print("X (data) = \n", X)
print("y (target) = \n", y)
X_train, X_test, y_train, y_test =\
    train_test_split(X, y, random_state=0, train_size=0.7)
X_train = X_train[:, :5]
X_test = X_test[:, :5]
print("X_train.shape = ", X_train.shape)
print("X_test.shape = ", X_test.shape)
print("y_train.shape = ", y_train.shape)
print("y_test.shape = ", y_test.shape)
print("Train_X/X, Test_X/X = {}, {}".\
      format(len(X_train)/len(X), len(X_test)/len(X)))


lgst_reg = LogisticRegression(random_state=0)
print("lgst_reg = ", lgst_reg)
lgst_reg.fit(X_train, y_train)
print("lgst_reg.coef_ = ", lgst_reg.coef_)
print("lgst_reg.intercept_ = ", lgst_reg.intercept_)
print("lgst_reg.score(X_train, y_train) = ", lgst_reg.score(X_train, y_train))
print("lgst_reg.score(X_test, y_test) = ", lgst_reg.score(X_test, y_test))
# predictions with test cases
index_test_cases = [1, 51, 101]
for index in index_test_cases:
    print("-------")
    print("Predict with X[{}]: target_name={}".format(index, target_names[target_class[index]]))
    pred = lgst_reg.predict(X[index:index+1, :5])
    print("lgst_reg.predict(X[{}:{}, :5]) = {} : {}".\
          format(index, index+1, lgst_reg.predict(X[index:index+1, :5]), target_names[pred[0]]))
    print("lgst_reg.predict_proba(X[{}:{}, :5]) = {}".\
          format(index, index+1, lgst_reg.predict_proba(X[index:index+1, :5])))