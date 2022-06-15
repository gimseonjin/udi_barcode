from unittest import result
import pyzbar.pyzbar as pyzbar
import cv2
from datetime import datetime
import numpy as np

class BarcodeService:

    def uploadSerivce(self, path:str):

        img = cv2.imread(path)

        i = self.preprocessing(img)

        itemResultDto = self.read_frame(i)

        return itemResultDto
            

    def preprocessing(self, img):

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        kernel_sharpen_1 = np.array([[1,-2,1],[-2,5,-2],[1,-2,1]])

        f_image = cv2.filter2D(gray,-1,kernel_sharpen_1)

        ret, i = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

        return gray
    
    def read_frame(self, img):
        try:
            decorded = pyzbar.decode(img)

            value = decorded[0].data.decode('utf-8')
            
            result = self.read_barcode(value)

            return {"msg" : True, "data": result }

        except Exception as e:

            return {"msg" : False, "data": None }
    
    def read_barcode(self, value):
        value = value.replace('\u001d', '')
        count = 2
        str_list = []
        while count != len(value):
            if value[0:count] == "01":
                str_list.append(value[count:count+14])
                count = count+14
            elif value[count:count+2] == "10":
                str_list.append(value[count+2:count+8])
                count = count + 8
            elif value[count:count+2] == "11":
                str_list.append(value[count+2:count+8])
                count = count + 8
            elif value[count:count+2] == "17":
                str_list.append(value[count+2:count+8])
                count = count + 8
            elif value[count:count+2] == "21":
                str_list.append(value[count+2:])
                count = len(value)

        result = "-".join(str_list)
        
        return result