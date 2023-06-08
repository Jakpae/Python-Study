# 실습 13.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : June 8, 2023

# 필요한 라이브러리 및 모듈을 Import
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Scikit-learn datasets  모듈의 load_iris() 메소드를 사용하여 붓꽃 데이터 세트를 Load
dset_iris = load_iris()

# 데이터셋의 정보를 출력
print("type(dset_iris) =\n", type(dset_iris))
print("dset_iris['DESCR'] =\n", dset_iris['DESCR'])
print("dset_iris['data'] =\n", dset_iris['data'])

# Scikit-learn datesets 모듈의 load_iris(return_X_y = True) 메소드를 사용하여 X(data), y(target)을 Load 하고 출력
target_class = dset_iris['target']
print("dset_iris['target'] =\n", target_class)
target_names = dset_iris['target_names']
print("dset_iris['target_names'] = ", target_names)
X, y = load_iris(return_X_y = True)
print("X (data) = \n", X)
print("y (target) = \n", y)

# 데이터셋을 훈련용 세트와 테스트용 세트로 분리 (비율: 훈련 70%, 테스트 30%)
X_train, X_test, y_train, y_test =\
train_test_split(X, y, random_state=0, train_size=0.7)
X_train = X_train[:, :5]
X_test = X_test[:, :5]

# 분리된 데이터셋의 크기를 출력
print("X_train.shape = ", X_train.shape)
print("X_test.shape = ", X_test.shape)
print("y_train.shape = ", y_train.shape)
print("y_test.shape = ", y_test.shape)
print("Train_X/X, Test_X/X = {}, {}".format(len(X_train)/len(X), len(X_test)/len(X)))

# 로지스틱 회귀 모델 객체를 생성하고 학습
lgst_reg = LogisticRegression(random_state=0, max_iter=200)
print("lgst_reg = ", lgst_reg)
lgst_reg.fit(X_train, y_train)

# 훈련된 모델의 가중치와 편향을 출력
print("lgst_reg.coef_ = ", lgst_reg.coef_)
print("lgst_reg.intercept_ = ", lgst_reg.intercept_)

# 훈련 세트와 테스트 세트에서의 정확도를 출력
print("lgst_reg.score(X_train, y_train) = ", lgst_reg.score(X_train, y_train))
print("lgst_reg.score(X_test, y_test) = ", lgst_reg.score(X_test, y_test))

# 테스트 케이스를 이용해 예측을 하고 결과를 출력
index_test_cases = [1, 51, 101]
for index in index_test_cases:
    print("-------")
    print("Predict with X[{}]: target_name={}".format(index, target_names[target_class[index]]))
    pred = lgst_reg.predict(X[index:index+1, :5])
    print("lgst_reg.predict(X[{}:{}, :5]) = {} : {}".\
          format(index, index+1, lgst_reg.predict(X[index:index+1, :5]), target_names[pred[0]]))
    print("lgst_reg.predict_proba(X[{}:{}, :5]) = {}".\
          format(index, index+1, lgst_reg.predict_proba(X[index:index+1, :5])))