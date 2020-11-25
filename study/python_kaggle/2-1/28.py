# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 对K近邻分类器在iris数据上的预测性能进行评估
"""
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
# 导入标准化模块
from sklearn.preprocessing import StandardScaler
# 导入K近邻分类器
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report

# 使用加载器读取数据并且存入变量iris
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=33)

# 对训练和测试的特征数据进行标准化
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

# 使用K近邻分类器对测试数据进行类别预测，预测结果储存在变量y_predict中
knc = KNeighborsClassifier()
knc.fit(X_train, y_train)
y_predict = knc.predict(X_test)
print ('The accuracy of K-Nearest Neighbor classifier is', knc.score(X_test, y_test))
print (classification_report(y_test, y_predict, target_names=iris.target_names))
