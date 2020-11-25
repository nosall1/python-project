# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/3/2
 使用Tensorflow完成一次线性函数的计算
"""
import tensorflow as tf

# 声明matrix1位Tensorflow的一个1*2的行向量
matrix1 = tf.constant([[3., 3.]])
# 声明matrix2位Tensorflow的一个2*1的列向量
matrix2 = tf.constant([[2.], [2.]])

# product将上述两个算子相乘，作为新算例
product = tf.matmul(matrix1, matrix2)
# 继续将product与一个标量2.0求和拼接，作为最终的linear算例
linear = tf.add(product, tf.constant(2.0))

# 直接在会话中执行linear算例，相当于将上面所有的单独算例拼接成流程图来执行
with tf.Session() as sess:
    result = sess.run(linear)
    print (result)
