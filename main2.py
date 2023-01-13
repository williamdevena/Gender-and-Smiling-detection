# import logging
# from sklearn.decomposition import PCA
# #from lazypredict.Supervised import LazyClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.cluster import KMeans, MiniBatchKMeans
# from sklearn.metrics import confusion_matrix
# import numpy as np
# import matplotlib.pyplot as plt
# import random
# import os
import torch
import torch.optim as optim
from torch import nn
from torchvision import models
# import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import cv2

from src import (
    data_loading,
    # data_preparation,
    data_visualization,
    costants,
    # image_manipulation,
    seeds,
    training
)

from baselines import face_feature_detector

from baselines.knn import knn_for_every_dataset
from baselines.svm import svm_for_every_dataset
from baselines import svm

from models.smile_cnn import SmileCNN

from assignment_dataset import AssignmentDataset
from pytorch_dataset import PytorchDataset

#logging.basicConfig(format="%(message)s", level=logging.INFO)


def main():
    '''
    SET SEEDS FOR REPRODUCABILITY
    '''
    seeds.set_seeds()

    '''
    DATA PREPARATION
    '''
    # data_preparation.data_preparation()

    '''
    DATA VISUALIZATION
    '''
    # data_visualization.data_visualization()

    '''
    DATA LOADING
    '''
    # dataset = "cropped_eyes_celeba"
    # label = "smiling"
    # width = 98
    # height = 38
    # image_dimensions = (width, height)
    # X_train_scaled, Y_train_scaled, X_test_scaled, Y_test_scaled = data_loading.load_X_Y_train_test(
    #     dataset, label, image_dimensions, scaling=True
    # )
    # X_train, Y_train, X_test, Y_test = data_loading.load_X_Y_train_test(
    #     dataset, label, image_dimensions, scaling=False
    # )
    # print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)
    # print(X_train_scaled.shape, Y_train_scaled.shape,
    #       X_test_scaled.shape, Y_test_scaled.shape)

    # print(X_train[0], X_train_scaled[0])

    """
    KNN
    """
    # knn_for_every_dataset()

    '''
    KNN CROSS VALIDATION
    '''
    # k_fold_params = range(5, 11)
    # array_possible_hyperparameter = range(10, 101, 10)
    # k_fold_params = range(5, 7)
    # array_possible_hyperparameter = range(10, 31, 10)
    # knn.knn_k_fold_cross_validation_for_every_dataset(
    #     k_fold_params, array_possible_hyperparameter
    # )

    '''
    PCA
    '''
    # pca = PCA()

    # dataset = "celeba"
    # label = "smiling"
    # width = 178
    # height = 218
    # image_dimensions = (width, height)
    # X_train, Y_train, X_test, Y_test = data_loading.load_X_Y_train_test(
    #     dataset, label, image_dimensions
    # )
    # pca.fit(X_train)
    # print(pca.explained_variance_ratio_)
    # print(pca.singular_values_)

    '''
    CROPPING DATASET FOR 'SMILING' or for 'EYE_COLOR'
    '''
    # path_original_folder = costants.PATH_CARTOON_TEST_IMG
    # path_cropped_folder = '../Datasets/cartoon_set_test/img_eye'
    # crop_y = slice(248, 277)
    # crop_x = slice(283, 308)
    # extension_image = ".png"
    # image_manipulation.crop_images_dataset(
    #     path_original_folder, path_cropped_folder, extension_image, crop_y, crop_x)

    '''
    LAZY PREDICT
    '''
    # dataset = "cropped_eye_cartoon"
    # label = "eye_color"
    # width = 25
    # height = 29
    # image_dimensions = (width, height)
    # X_train, Y_train, X_test, Y_test = data_loading.load_X_Y_train_test(
    #     dataset, label, image_dimensions
    # )
    # clf = LazyClassifier(verbose=1, ignore_warnings=True, custom_metric=None)

    # # # X_train = X_train[:20]
    # # # Y_train = Y_train[:20]
    # # # X_test = X_test[:10]
    # # # Y_test = Y_test[:10]
    # models, predictions = clf.fit(X_train, X_test, Y_train, Y_test)
    # print(models)

    """
    COUNT PUPIL COLORS
    """
    # data_preparation.count_pupil_colors(
    #     costants.PATH_CARTOON_TRAIN_IMG, pixel_y=260, pixel_x=294)

    # path = costants.PATH_CARTOON_TRAIN_CROPPED_EYE_IMG
    # dict_colors = data_preparation.count_pupil_colors_colorthief(path)
    # X = np.array([np.array(color) for color in dict_colors])
    # print(X.shape)
    # kmeans = KMeans(n_clusters=6)
    # kmeans.fit(X)

    # # Getting the cluster labels
    # labels = kmeans.predict(X)
    # centroids = kmeans.cluster_centers_
    # array_centroids = [(int(centroid[0]), int(centroid[1]), int(centroid[2]))
    #                    for centroid in centroids]
    # print(array_centroids)
    # labels = kmeans.predict(X)

    # fig = plt.figure(figsize=(20, 10))
    # ax = fig.add_subplot(111, projection='3d')

    # c0 = np.array(labels == 0)
    # c1 = np.array(labels == 1)
    # c2 = np.array(labels == 2)
    # c3 = np.array(labels == 3)
    # c4 = np.array(labels == 4)
    # c5 = np.array(labels == 5)

    # ax.scatter(X[c0][:, 0], X[c0][:, 1], X[c0][:, 2])
    # ax.scatter(X[c1][:, 0], X[c1][:, 1], X[c1][:, 2])
    # ax.scatter(X[c2][:, 0], X[c2][:, 1], X[c2][:, 2])
    # ax.scatter(X[c3][:, 0], X[c3][:, 1], X[c3][:, 2])
    # ax.scatter(X[c4][:, 0], X[c4][:, 1], X[c4][:, 2])
    # ax.scatter(X[c5][:, 0], X[c5][:, 1], X[c5][:, 2])
    # ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2],
    #            marker='x', s=169, linewidths=10,
    #            color='black', zorder=50)
    # ax.set_xlabel('R')
    # ax.set_ylabel('G')
    # ax.set_zlabel('B')
    # plt.show()

    """
    DOMINANT COLOR SOLUTION 
    """
    # X_train_transformed, Y_train_transformed = image_manipulation.create_dominant_colors_dataset(
    #     costants.PATH_CARTOON_TRAIN_CROPPED_EYE_IMG,
    #     costants.PATH_CARTOON_TRAIN_LABELS
    # )

    # X_test_transformed, Y_test_transformed = image_manipulation.create_dominant_colors_dataset(
    #     costants.PATH_CARTOON_TEST_CROPPED_EYE_IMG,
    #     costants.PATH_CARTOON_TEST_LABELS
    # )

    # score = knn.knn(k=20, X_train=X_train_transformed, Y_train=Y_train_transformed,
    #                 X_test=X_test_transformed, Y_test=Y_test_transformed)
    # print(score)
    # print(X_train_transformed.shape, Y_train_transformed.shape)
    # print(X_train_transformed, Y_train_transformed)

    # print(X_test_transformed.shape, Y_test_transformed.shape)
    # print(X_test_transformed, Y_test_transformed)

    """
    SVM
    """
    # dataset_name = "cropped_mouth_celeba"
    # label_name = "smiling"
    # dataset = Dataset(name=dataset_name, label=label_name)

    # X_train, Y_train, X_test, Y_test = data_loading.load_X_Y_train_test(
    #     dataset_object=dataset, scaling=True
    # )
    # score = svm.svm(kernel='linear', C=1.0, X_train=X_train,
    #                 Y_train=Y_train, X_test=X_test, Y_test=Y_test)
    # print(score)

    """
    SVM ON ALL DATASETS
    """
    # svm_for_every_dataset(use_canny_filter=False)

    """
    SIMPLE NN
    """
    # batch_size = 4
    # input_size = 58*33
    # output_size = 1
    # hidden_layers = [10000, 10000]
    # activation = torch.nn.ReLU()
    # model = SimpleNN(input_size=input_size, ouput_size=output_size,
    #                  hidden_layers=hidden_layers, activation=activation)

    # x = torch.rand(batch_size, input_size)
    # out = model(x)
    # print(out)

    """
    TEST PYTORCH DATASET
    """
    # dataset = PytorchDataset("celeba", "smiling", train_or_test="train")
    # for x in range(10):
    #     image, label = dataset.__getitem__(x)
    #     print(image.dtype)
    #     print(image.shape, label)

    """
    TEST TRAINING NN
    """
    # dataset_name = "celeba"
    # label_name = "smiling"

    # train_set = PytorchDataset(
    #     dataset_name=dataset_name, label_name=label_name, train_or_test="train")
    # test_set = PytorchDataset(
    #     dataset_name=dataset_name, label_name=label_name, train_or_test="test")

    # batch_size = 4
    # num_epochs = 30
    # train_dataloader = torch.utils.data.DataLoader(train_set,
    #                                                batch_size=batch_size,
    #                                                shuffle=True)
    # test_dataloader = torch.utils.data.DataLoader(test_set,
    #                                               batch_size=1,
    #                                               shuffle=False)

    # # loss = nn.CrossEntropyLoss()
    # loss = nn.BCELoss()

    # #model = models.efficientnet_b0()
    # model = SmileCNN()

    # optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=0.001)

    # # acc = training.testing(model=model, test_dataloader=test_dataloader)
    # # print(acc)

    # training.training_epochs(model=model,
    #                          num_epochs=num_epochs,
    #                          loss_function=loss,
    #                          optimizer=optimizer,
    #                          train_dataloader=train_dataloader,
    #                          test_dataloader=test_dataloader)

    """
    TEST LOADING IMAGES (NON FLAT)
    """
    # dataset_name = "cartoon"
    # label_name = "eye_color"
    # dataset = AssignmentDataset(name=dataset_name, label=label_name)
    # x1 = data_loading.load_images_from_folder(
    #     ds_path=costants.PATH_CARTOON_TRAIN_IMG, image_dimensions=dataset.image_dimensions)
    # x2 = data_loading.load_flatten_images_from_folder(
    #     ds_path=costants.PATH_CARTOON_TRAIN_IMG, image_dimensions=dataset.image_dimensions)
    # print(x1.shape, x2.shape)

    """
    FACE DETECTOR LANDMARKS
    """
    # import cv2
    # import numpy as np
    # import dlib

    # # Load the detector
    # detector = dlib.get_frontal_face_detector()

    # # Load the predictor
    # predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # # read the image
    # img = cv2.imread("9.jpg", cv2.IMREAD_COLOR)

    # # Convert image into grayscale
    # gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    # landmarks_array = []

    # # Use detector to find landmarks
    # faces = detector(gray)
    # for face in faces:
    #     x1 = face.left()  # left point
    #     y1 = face.top()  # top point
    #     x2 = face.right()  # right point
    #     y2 = face.bottom()  # bottom point

    #     # Create landmark object
    #     landmarks = predictor(image=gray, box=face)
    #     # print(landmarks)

    #     # Loop through all the points
    #     for n in range(0, 68):
    #         x = landmarks.part(n).x
    #         y = landmarks.part(n).y

    #         landmarks_array.append((x, y))

    #         # Draw a circle
    #         cv2.circle(img=img, center=(x, y), radius=2,
    #                    color=(0, 255, 0), thickness=-1)

    # cv2.imwrite(filename="./test_landmarks.jpg", img=img)

    """
    FACE DETECTOR TEST SVM AND KNN
    """
    # # Load the detector
    # detector = dlib.get_frontal_face_detector()

    # # Load the predictor
    # predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # label = "face_shape"
    # image_dimensions = (500, 500)
    # #image_dimensions = (178, 218)

    # # range_features = range(0, 68) # ALL
    # #range_features = range(37, 68) # EYES AND MOUTH
    # #range_features = range(37, 48) # EYES
    # #range_features = range(49, 68) # MOUTH
    # range_features = range(0, 17) # CHIN

    # X_train, Y_train = face_feature_detector.create_face_features_dataset(ds_path=costants.PATH_CARTOON_TRAIN_IMG,
    #                                                 csv_path=costants.PATH_CARTOON_TRAIN_LABELS,
    #                                                 label=label,
    #                                                 image_dimensions=image_dimensions,
    #                                                 detector=detector,
    #                                                 predictor=predictor,
    #                                                 range_features=range_features)

    # X_test, Y_test = face_feature_detector.create_face_features_dataset(ds_path=costants.PATH_CARTOON_TEST_IMG,
    #                                             csv_path=costants.PATH_CARTOON_TEST_LABELS,
    #                                             label=label,
    #                                             image_dimensions=image_dimensions,
    #                                             detector=detector,
    #                                             predictor=predictor,
    #                                             range_features=range_features)

    # score = svm.svm(kernel='rbf', C=1.0, X_train=X_train,
    #                 Y_train=Y_train, X_test=X_test, Y_test=Y_test)
    # print(score[1], score[2])

    # score = knn.knn(k=30, X_train=X_train,
    #                 Y_train=Y_train, X_test=X_test, Y_test=Y_test)
    # print(score[1], score[2])

    """
    CROP WITH FACE DETECTOR
    """
    # import dlib
    # # Load the detector
    # detector = dlib.get_frontal_face_detector()

    # # Load the predictor
    # predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # # range_features = range(49, 68)
    # # resized_shape = (48, 25)

    # range_features = range(0, 68)
    # resized_shape = (125, 140)

    # face_feature_detector.crop_images_dinamycally_using_face_features(costants.PATH_CARTOON_TEST_IMG,
    #                                                                   costants.PATH_CARTOON_TEST_DYN_CROPPED_FACE_IMG,
    #                                                                   ".png",
    #                                                                   detector,
    #                                                                   predictor,
    #                                                                   range_features,
    #                                                                   resized_shape
    #                                                                   )

    """
    CREATE AND WRITE FACE FEATURES DATASETS
    """

    # import dlib

    # # Load the detector
    # detector = dlib.get_frontal_face_detector()

    # # Load the predictor
    # predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # label = "face_shape"
    # image_dimensions = (500, 500)
    # train_ds_path = costants.PATH_CARTOON_TRAIN_IMG
    # train_csv_path = costants.PATH_CARTOON_TRAIN_LABELS
    # test_ds_path = costants.PATH_CARTOON_TEST_IMG
    # test_csv_path = costants.PATH_CARTOON_TEST_LABELS

    # label = "gender"
    # image_dimensions = (178, 218)
    # train_ds_path = costants.PATH_CELEBA_TRAIN_IMG
    # train_csv_path = costants.PATH_CELEBA_TRAIN_LABELS
    # test_ds_path = costants.PATH_CELEBA_TEST_IMG
    # test_csv_path = costants.PATH_CELEBA_TEST_LABELS

    # range_features = range(0, 68)  # ALL
    # # range_features = range(37, 68) # EYES AND MOUTH
    # # range_features = range(37, 48) # EYES
    # # range_features = range(49, 68) # MOUTH
    # # range_features = range(0, 17) # CHIN

    # CREATE AND WRITE FACE FEATURES DATASETS
    # face_feature_detector.create_and_write_face_features_dataset(detector=detector,
    #                                                              predictor=predictor,
    #                                                              range_features=range_features)

    """
    MLP and SVM ON FACE FEATURES
    """
    # from sklearn.neural_network import MLPClassifier

    # # LOAD DS FROM CSV OF FEATURE FACE
    # label = 'face_shape'
    # train_csv_path = costants.PATH_CARTOON_TRAIN_FACE_FEATURES
    # test_csv_path = costants.PATH_CARTOON_TEST_FACE_FEATURES

    label = 'gender'
    train_csv_path = costants.PATH_CELEBA_TRAIN_FACE_FEATURES
    test_csv_path = costants.PATH_CELEBA_TEST_FACE_FEATURES

    # # (0, 136) for all features
    # # (0, 34) for chin features

    feature_slice = slice(0, 136)
    # #feature_slice = slice(0, 136)

    train_dataset_dict = data_loading.load_entire_ds_from_csv(
        csv_path=train_csv_path)
    test_dataset_dict = data_loading.load_entire_ds_from_csv(
        csv_path=test_csv_path)

    X_train = train_dataset_dict['X'][:, feature_slice]
    X_test = test_dataset_dict['X'][:, feature_slice]
    print(X_train.shape, X_test.shape)

    Y_train = train_dataset_dict['Y'][label]
    Y_test = test_dataset_dict['Y'][label]

    Y_pred, training_acc, testing_acc = svm.svm(kernel='rbf', C=1.0,
                                                X_train=X_train,
                                                Y_train=Y_train,
                                                X_test=X_test,
                                                Y_test=Y_test)

    print(testing_acc)

    # Y_train = np.where(Y_train == -1, 0, Y_train)
    # Y_test = np.where(Y_test == -1, 0, Y_test)
    #self.Y = np.where(self.Y == -1, 0, self.Y)

    # for face shape
    # mlp = MLPClassifier(hidden_layer_sizes=(300, 600, 300, 100),
    #                     random_state=1, max_iter=100,
    #                     verbose=False, solver="lbfgs",
    #                     warm_start=True)

    # for gender --> 0.926 acc
    # mlp = MLPClassifier(hidden_layer_sizes=(20),
    #                     random_state=1, max_iter=200,
    #                     verbose=True, solver="adam",
    #                     early_stopping=True,
    #                     n_iter_no_change=50,
    #                     #warm_start=True,
    #                     learning_rate_init=0.01,  # 0.01
    #                     alpha=0.0001)

    # for smiling
    # mlp = MLPClassifier(hidden_layer_sizes=(100),  # 100
    #                     random_state=1, max_iter=1000,
    #                     verbose=True, solver="adam",
    #                     early_stopping=False,
    #                     n_iter_no_change=500,
    #                     # warm_start=True,
    #                     alpha=0.1,
    #                     learning_rate_init=0.01)

    # for face shape
    # mlp = MLPClassifier(hidden_layer_sizes=(100, 100, 100, 100),  # 100
    #                     random_state=1, max_iter=1000,  # a 1500 si ferma
    #                     verbose=True, solver="adam",
    #                     early_stopping=True,
    #                     validation_fraction=0.2,
    #                     n_iter_no_change=1000,
    #                     # warm_start=True,
    #                     alpha=0.1,
    #                     learning_rate_init=0.01)

    # mlp.fit(X_train, Y_train)

    # plt.plot(mlp.loss_curve_)
    # plt.savefig("loss_curve")
    # plt.close()

    # plt.plot(mlp.validation_scores_)
    # plt.savefig("validation scores")
    # plt.close()

    # training_acc = mlp.score(X_train, Y_train)
    # score = mlp.score(X_test, Y_test)
    # Y_pred = mlp.predict(X_test)
    # print(training_acc, score)

    # data_visualization.plot_confusion_matrix(
    #     Y_test, Y_pred, ["0", "1", "2", "3", "4"], "confusion_matrix")

    """
    MLP on images
    """
    # from sklearn.neural_network import MLPClassifier

    # dataset_name = "dyn_cropped_eyes_celeba"
    # label_name = "gender"

    # dataset = AssignmentDataset(name=dataset_name, label=label_name)
    # X_train, Y_train, X_test, Y_test = data_loading.load_X_Y_train_test(
    #     dataset_object=dataset
    # )

    # print(X_train.shape, Y_train.shape)

    # # for gender
    # mlp = MLPClassifier(hidden_layer_sizes=(1000),
    #                     random_state=1, max_iter=100,
    #                     verbose=True, solver="adam",
    #                     early_stopping=True,
    #                     n_iter_no_change=100,
    #                     warm_start=True,
    #                     alpha=0.001)

    # mlp.fit(X_train, Y_train)

    # plt.plot(mlp.loss_curve_)
    # plt.savefig("loss_curve_")
    # plt.close()

    # plt.plot(mlp.validation_scores_)
    # plt.savefig("validation scores")
    # plt.close()

    # training_acc = mlp.score(X_train, Y_train)
    # score = mlp.score(X_test, Y_test)
    # print(training_acc, score)

    """
    TEST CANNY FILTER
    """
    # img = cv2.imread("face4.jpg", cv2.IMREAD_GRAYSCALE)
    # min_threshold = np.mean(img)*0.66
    # max_threshold = np.mean(img)*1.33

    # img = cv2.Canny(image=img, threshold1=min_threshold,
    #                 threshold2=max_threshold)

    # cv2.imshow(mat=img, winname="Edges")
    # # cv2.imshow(winname="Face", mat=img)

    # # # Delay between every fram
    # cv2.waitKey(delay=0)

    # # # Close all windows
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()