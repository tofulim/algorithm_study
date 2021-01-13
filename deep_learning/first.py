import tensorflow as tf
import matplotlib.pyplot as plt

X=[1.0,2.0,3.0]
Y=[1.0,2.0,3.0]

W= tf.constant(0.0)

w_val =[]
cost_val=[]
@tf.function
def change_W(w):
    return tf.reduce_mean(tf.square(tf.multiply(X,w)-Y))

for i in range(-30, 50):
    feed_w=i*0.1
    curr_w=feed_w
    curr_cost,curr_w=[change_W(feed_w),feed_w]
    w_val.append(curr_w)
    cost_val.append(curr_cost)

plt.plot(w_val,cost_val)
plt.show()
