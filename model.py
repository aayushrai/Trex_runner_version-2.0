from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPool2D,Flatten,Activation,Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import RMSprop
import cv2
img = cv2.imread("data_resize\\jump\\1411.jpg")
img_gen = ImageDataGenerator(rescale=1/255)


model = Sequential()

model.add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same',
                 activation ='relu', input_shape = (img.shape[0], img.shape[1],1)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(filters = 32, kernel_size = (3,3),padding = 'Same',
                 activation ='relu'))
model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))

model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same',
                 activation ='relu'))
model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.4))
model.add(Dense(2, activation = "sigmoid"))

optimizer = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
model.compile(optimizer=optimizer,loss="binary_crossentropy",metrics=["accuracy"])

train_image_gen = img_gen.flow_from_directory("data_resize",target_size=(img.shape[0], img.shape[1]),batch_size= 100,shuffle=True,color_mode="grayscale" )
print(train_image_gen.class_indices)
results = model.fit_generator(train_image_gen,epochs=40,steps_per_epoch=30)
model.save("trex-v5.h5")
