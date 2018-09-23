from DeepLearning import *
import numpy as np
import tensorflow as tf

train, valor = getTrain()
test = getTest()

print("BUILD MODEL")

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Conv2D(32,kernel_size=(3, 3),activation='relu',input_shape=(28,28,1)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
model.add(tf.keras.layers.Dropout(0.25))
 
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
 
print("COMPILING MODEL")

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('TRAINING MODEL')

model.fit(train, valor, 
          batch_size=64, nb_epoch=2, verbose=1)
 


#score = model.evaluate(X_test, Y_test, verbose=0)
#print('Test loss ',score[0])
#print('Test accuracy ',score[1])
