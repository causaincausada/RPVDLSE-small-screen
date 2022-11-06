import cv2
import numpy as np
import os
import easyocr
import random

class Recognition:
    def __init__(self):
        self.INPUT_WIDTH =  640
        self.INPUT_HEIGHT = 640
        self.load_model()
        #easyOCR
        self.reader = easyocr.Reader(["es"], gpu=False)
    
    def load_model(self):
        # LOAD YOLO MODEL
        try:            
            path_project = os.path.dirname(__file__)
            path = os.path.join(path_project, 'best.onnx')
        except (OSError, IOError) as e:
            print(e)

        #print(path, path_project)
        self.net = cv2.dnn.readNetFromONNX(path)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def get_detections(self,img):
        # CONVERT IMAGE TO YOLO FORMAT
        image = img.copy()
        row, col, d = image.shape

        max_rc = max(row,col)
        input_image = np.zeros((max_rc,max_rc,3),dtype=np.uint8)
        input_image[0:row,0:col] = image

        # GET PREDICTION FROM YOLO MODEL
        blob = cv2.dnn.blobFromImage(input_image,1/255,(self.INPUT_WIDTH,
                                                        self.INPUT_HEIGHT)
                                     ,swapRB=True,crop=False)
        self.net.setInput(blob)
        preds = self.net.forward()
        detections = preds[0]
        
        return input_image, detections

    def non_maximum_supression(self,input_image,detections):
        # FILTER DETECTIONS BASED ON CONFIDENCE AND PROBABILIY SCORE
        # center x, center y, w , h, conf, proba
        boxes = []
        confidences = []

        image_w, image_h = input_image.shape[:2]
        x_factor = image_w/self.INPUT_WIDTH
        y_factor = image_h/self.INPUT_HEIGHT

        for i in range(len(detections)):
            row = detections[i]
            confidence = row[4] # confidence of detecting license plate
            if confidence > 0.4:
                class_score = row[5] # probability score of license plate
                if class_score > 0.25:
                    cx, cy , w, h = row[0:4]

                    left = int((cx - 0.5*w)*x_factor)
                    top = int((cy-0.5*h)*y_factor)
                    width = int(w*x_factor)
                    height = int(h*y_factor)
                    box = np.array([left,top,width,height])

                    confidences.append(confidence)
                    boxes.append(box)

        # clean
        boxes_np = np.array(boxes).tolist()
        confidences_np = np.array(confidences).tolist()
        # NMS
        index = np.array(cv2.dnn.NMSBoxes(boxes_np,confidences_np,0.25,0.45)
                         ).flatten()
        
        return boxes_np, confidences_np, index

    def get_recognition(self,image,boxes_np,confidences_np,index):
        r = ""
        print("tam: ", len(index))

        if(len(index) == 0):
            print("No se encontro la placa vehicular.")
            return '0'
        for ind in index:
            x,y,w,h =  boxes_np[ind]
            bb_conf = confidences_np[ind]
            conf_text = 'plate: {:.0f}%'.format(bb_conf*100)
            license_text = self.extract_text(image,boxes_np[ind])
            r+=license_text + " "

        return r

    # predictions
    def yolo_predictions(self,img):
        ## step-1: detections
        input_image, detections = self.get_detections(img)
        ## step-2: NMS
        boxes_np, confidences_np, index = self.non_maximum_supression(input_image, 
                                                                      detections)
        ## step-3: getRecognition
        result = self.get_recognition(img,boxes_np,confidences_np,index)
        return result

    def extract_text(self,image,bbox):
        x, y, yh, xw = self.check_bounds_roi(bbox, image)
        roi = image[y:yh, x:xw]
        x, y, w, h = self.roi_plate(roi)
        plate_img = roi[y:y+h, x:x+w]

        if 0 in plate_img.shape:
            return '0'

        plate_binary = self.binary(plate_img)

        detections = self.reader.readtext(plate_img, 
                                          allowlist='-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                                          min_size=150)
        if len(detections) == 0:
            print("No se pueden leer los caracteres de la placa vehicular.")
            return '1'
        else:
            text = ""
            max = 0.0
            print(len(detections))
            if(len(detections)>1):
                print("####")
            for detection in detections: 
                print(detection)
                if(detection[2] > max):
                    max = detection[2]
                    text = detection[1].strip()
                    print("placa:", text)#Quitar
            return text   

    def check_bounds_roi(self,bbox, image):
        x,y,w,h = bbox
        yh=0
        xw=0
        height, width, __ = image.shape
        if(x<0): x=0
        if(y<0): y=0
        if(w<0): w=0
        if(h<0): h=0
        if(x>=width): x=width-1
        if(y>=height): y=height-1
        
        if(x+w >= width): xw = width-1
        elif(x+w<0): xw = 0
        else: xw = x+w

        if(y+h >= height): yh = height-1
        elif(y+h<0): yh = 0
        else: yh = y+h

        return x, y, yh, xw

    def roi_plate(self,image):
        height, width, __ = image.shape
        x = (int) (0.01 * width)
        y = (int) (0.10 * height)
        w = (int) (0.98 * width)
        h = (int) (0.80 * height)

        return x, y, w, h

    def binary(self,image):
        image = cv2.resize(image, None, fx=1.2, fy=1.2, 
                           interpolation=cv2.INTER_CUBIC)
        gray_plate = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.blur(gray_plate,(3,3))
        noiseless_image_bw = cv2.fastNlMeansDenoising(blur, None, 20, 7, 21)
        thresh_gauss = cv2.adaptiveThreshold(noiseless_image_bw, 255, 
                                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY, 21, 10) 
        kernel = np.ones((2, 2), np.uint8)
        erode = cv2.erode(thresh_gauss, kernel)
        return erode

