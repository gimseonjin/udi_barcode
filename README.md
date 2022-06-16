# ✨ UDI Barcode ✨

## **description : Input UDI Barcode image, Interpret it!**

<img src = "https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/logo.png" width = "100%">

<br/>

# **Why pick this?**

## **1. It is necessary**

### In Koreat, **UDI barcodes must be attached to medical devices**

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/reason_1.png)

## **2. UDI barcode scanner is expensive**

### UDI barcode scanner is too expensive!!

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/reason_2.png)

## **3. Practice Open CV!**

### To Recognize UDI barcode, should use Open CV!

<img src = "https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/reason_3.png" width = "100%">

<br/>

# **ERD Diagram**

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/erd.png)

<br/>

# **Project Structure**

## Infra Structure
![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/structure.jpg)

## Folder Structure
<p align="center">
  <img src = "https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/folder_structure.png" width = "50%">
</p>

<br/>

# **Project Logic and Views**

## **Login & Register**

### Before use this service, Login First!!

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_1.png)

### If you first, Register before!

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_2.png)

## **Main Page**

### After Login, you can enter main page

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_3.png)

### Input your UDI barcode, and send image using click me button!

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_4.png)

### Then, return UDI barcode and result!

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_5.png)

### If you input wrong image or b**arcode difficult to recognize, return None and False**

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_6.png)

## **Dashboard Page**

### You can see histories in Dashboard page

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_7.png)

### If you want see history, Click one!

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_8.png)

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_9.png)

## My Page

### Update your personal data!

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_10.png)

<br/>

# Something Special

<br/>
<br/>

## ✨Using only gray scale is the best performance, and improved about 12% performance.✨

<br/>
<br/>

## How to improve recognition performance??

### In various articles about barcode recognition, They use "gray-scale, sharpening, threshold" to improve performance!

gray-scale
<p align="center">
  <img src = "https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/gray_scale.png" width = "80%">
</p>

sharpening
<p align="center">
  <img src = "https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/sharpening.png" width = "80%">
</p>

threshold
<p align="center">
  <img src = "https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/threshold.png" width = "80%">
</p>

<br/>

## So, Let's preprocess the image using "gray-scale, sharpening, threshold" before recognition!

### First - Make cases about pre-processing

~~~python
    # "case Num" : ["gray-scale", "sharpening", "threshold"]
    cases = {
        "case 1" : [True, True, True],
        "case 2" : [True, True, False],
        "case 3" : [True, False, True],
        "case 4" : [False, True, True],
        "case 5" : [True, False, False],
        "case 6" : [False, True, False],
        "case 7" : [False, False, True],
        "case 8" : [False, False, False],
    }
~~~

### Second - Make test targets - (I made 25 img for test)

~~~python
    targets = []
    for i in range(1,25):
        targets.append("barcode_" + str(i) + ".jpeg")
    }
~~~

### Third - For each target, Calculate rate!!
~~~python
for target in targets:

  img = cv2.imread('sample_udi/' + target)
  
  preprocessed_img = service.preprocessing(img=img, gray=case[0], sharpen= case[1], threshold= case[2])
  
  result = service._read_frame(preprocessed_img)
  
    if result.get("msg") :
      success_case += 1
      
# Divide success case and targets length
rate = success_case / len(targets)

result_list[k] = rate
~~~

### Fourth - Sorting results, and Show!
~~~python
result_list = sorted(result_list.items(), key=lambda x : x[1], reverse=True)
    
# then
for result in result_list:
  case = cases[result[0]]
  print()
  print(f"{result[0]} gray = {case[0]}, shrpen = {case[1]}, threshold = {case[2]}")
  print(f"==> {result[1]}")
  print()
~~~

<br/>

### Result - Improve performance 66% to 79% (about 12%!!!)
<p align="center">
  <img src = "https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/test_result.jpg" width = "80%">
</p>
<br/>
<br/>
<br/>

# How To Run

## **Warning! - This is sample repo! So It is not connected with mysql and Sentry, Just run server with dev version! (Using sqlite3 and manage.py run server)**

### Requirement

```
//If you want just run, only required docker!
Docker : 20.10.16

//If you want code edit, At leats required below
Python : 3.10.0
Django : 4.0.5
Opencv-python : 4.6.0.66
Pyzbar : 0.1.9
Zbar : anything

```

### Build Setup

```
1. $ sudo git clone {this repo}
2. $ sudo docker build -t udi_barcode .
3. $ sudo docker run -p 8000:8000 udi_barcode

```
