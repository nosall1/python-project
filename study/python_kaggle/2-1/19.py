# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 使用支持向量机（分类）对手写体数字图像进行识别
"""
# 从sklearn.preprocessing里导入数据标准化模块
from sklearn.preprocessing import StandardScaler
# 从sklearn.svm里导入基于线性假设的支持向量机分类器LinearSVC
from sklearn.svm import LinearSVC
from sklearn.cross_validation import train_test_split

# 从sklearn.datasets里导入手写体数字加载器
from sklearn.datasets import load_digits

# 从通过数据加载器获得手写体数字的数码图像数据并存储在digits变量中
digits = load_digits()
# 检视数据规模和特征维度
# print digits.data.shape
# 随机选取75%的数据作为训练样本，其余25%的数据作为测试样本
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)

# 从仍然需要对训练和测试的特征数据进行标准化
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)
# 初始化线性假设的支持向量机分类器LinearSVC
lsvc = LinearSVC()
# 进行模型训练
lsvc.fit(X_train, y_train)
# 利用训练好的模型对测试样本的数字类别进行预测，预测结果存储在变量y_predict中
y_predict = lsvc.predict(X_test)
print (y_predict)
