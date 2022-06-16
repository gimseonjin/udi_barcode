# ✨ UDI Barcode ✨

## **description : Input UDI Barcode image, Interpret it!**

<img src = "https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/logo.png" width = "100%">

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

# **ERD Diagram**

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/erd.png)

# **Project Structure**

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/structure.jpg)

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

## My Page

### Update your personal data!

![UDI%20Barcode%20f9c2e002d6f74ae5abb4d4931a6c8c7a/Untitled.png](https://github.com/gimseonjin/udi_barcode/blob/main/readme_img/example_9.png)

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
