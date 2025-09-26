# # load dataset
# # (X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()
# (X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()


# X_train = X_train.astype("float32")/255.0
# X_test = X_test.astype("float32")/255.0
# # print("hello")

# # reshape data (CNN : expect 3D: height,width,channels)
# X_train = X_train.reshape(-1,28,28,1)
# X_test = X_test.reshape(-1,28,28,1)
# # -1 means figure this dimension out automatically
# # 1 is no. of channels