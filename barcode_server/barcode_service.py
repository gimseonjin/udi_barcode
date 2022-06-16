"""
This module has barcode service
"""
from pathlib import Path

from pyzbar import pyzbar
import cv2
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent

class BarcodeService:
    '''
    Title : BarcodeService

    This class is used to recognize to barcode

    Attributes:
        uploadSerivce (function) : This Function is used to recognize barcode default!
    '''
    def uploadSerivce(self, path:str):
        """
        Title : uploadSerivce

        This is Function which is used for recognize barcode!

        Args:
            path (string): input your img path

        Returns:
           if success :
                return dict : {"msg" : True, "data": result }
           if fail :
                return {"msg" : False, "data": "None" }

        Raises:
            Notfound: If there is wrong img path, raise not found image!

        Note:
            Please use this function only!!!
        """

        img = cv2.imread(path)

        i = self.preprocessing(img)

        itemResultDto = self._read_frame(i, path)

        return itemResultDto

    def preprocessing(self, img, gray=True, sharpen=False, threshold=False):
        """
        Title : preprocessing

        This Function is preporcessing img

        Args:
            img (Object) : input img Object from opencv
            gray (boolean) : If you want control gray scale, input here
                             default True
            sharpen (boolean) : If you want control gray scale, input here
                                default False
            threshold (boolean) : If you want control gray scale, input here
                                  default False

        Returns:
            result (Object) : preporcessing result

        Raises:
            -

        Note:
            Please use uploadSerivce logic
        """
        if gray:
            result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        if sharpen:
            kernel_sharpen_1 = np.array([[1,-2,1],[-2,5,-2],[1,-2,1]])
            result = cv2.filter2D(result,-1,kernel_sharpen_1)

        if threshold :
            thresh_result = cv2.threshold(result, 100, 255, cv2.THRESH_BINARY)
            result = thresh_result[1]

        return result

    def _read_frame(self, img, path:str):
        """
        Title : _read_frame

        This is read frame form preprocessed img

        Args:
            img (Object) : input img object from opencv
            path (string) : input your img path to save img

        Returns:
           if success :
                return dict : {"msg" : True, "data": result }
           if fail :
                return {"msg" : False, "data": "None" }

        Raises:
            -

        Note:
            Please use uploadSerivce logic
        """
        try:
            decorded = pyzbar.decode(img)

            value = decorded[0].data.decode('utf-8')

            for d in decorded:
                cv2.rectangle(img, (d.rect[0], d.rect[1]), (d.rect[0] + d.rect[2], d.rect[1] + d.rect[3]), (0, 0, 255), 5)

            cv2.imwrite("./"+path, img)

            result = self._read_barcode(value)

            return {"msg" : True, "data": result }

        except IndexError :
            return {"msg" : False, "data": "None" }

    def _read_barcode(self, value:str):
        """
        Title : _read_barcode

        This is serializate from img to udi barcode

        Args:
            value (string): get data from barcode

        Returns:
           if success :
                return string : uid data
           if fail :
                return string : "

        Raises:
            -

        Note:
            Please use uploadSerivce logic
        """
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
