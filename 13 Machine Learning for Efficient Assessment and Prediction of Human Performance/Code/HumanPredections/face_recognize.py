# facerec.py
import cv2, sys, numpy, os
import time
size = 4
capture_duration = 10
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'database'
# Part 1: Create fisherRecognizer
print('Training...')
# Create a list of images and a list of corresponding names
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '\\' + filename
            #print("Path = ",path)
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(width, height) = (130, 100)
# Create a Numpy array from the two lists above
(images, lables) = [numpy.array(lis) for lis in [images, lables]]
# OpenCV trains a model from the images
# NOTE FOR OpenCV2: remove '.face'
#model = cv2.createFisherFaceRecognizer()
def faceDetectStatus():
    try:
        # model = cv2.face.FisherFaceRecognizer_create()
        # model = cv2.face.LBPHFaceRecognizer_create()
        # create our LBPH face recognizer
        model = cv2.face.LBPHFaceRecognizer_create()
        # or use EigenFaceRecognizer by replacing above line with
        # model = cv2.face.EigenFaceRecognizer_create()
        # or use FisherFaceRecognizer by replacing above line with
        # model = cv2.face.FisherFaceRecognizer_create()
        model.train(images, lables)
    except Exception as e:
        print(str(e))
        pass
    # Part 2: Use fisherRecognizer on camera stream
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)
    # save current time
    prev_time = time.time()
    # start webcam feed
    start_time = time.time()
    # while True:
    while (int(time.time() - start_time) < capture_duration):
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        rslt = []
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))

            # Try to recognize the face
            prediction = model.predict(face_resize)
            print('Predection is ', prediction)
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
            if prediction[1] > 90:
                rslt.append('True')
                cv2.putText(im, '%s - %.0f' % (names[prediction[0]], prediction[1]), (x - 10, y - 10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                break

            else:
                rslt.append('False')
                cv2.putText(im, 'not recognized', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                break

        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == 27:
            # if key == -1:
            break
    cv2.destroyAllWindows()
    return rslt