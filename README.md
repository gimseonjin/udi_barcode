# UDI Barcode

# **Title :** UDI Barcode

## **description : Input UDI Barcode image, Interpret it!**

# **Why pick this?**

## **1. It is necessary**

### In Koreat, **UDI barcodes must be attached to medical devices**


## **2. UDI barcode scanner is expensive**

### UDI barcode scanner is too expensive!!



## **3. Practice Open CV!**

### To Recognize UDI barcode, should use Open CV!



# **ERD Diagram**



# **Project Structure**



# **Project Logic and Views**

## **Login & Register**

### Before use this service, Login First!!



### If you first, Register before!



## **Main Page**

### After Login, you can enter main page



### Input your UDI barcode, and send image using click me button!



### Then, return UDI barcode and result!



### If you input wrong image or b**arcode difficult to recognize, return None and False**



## **Dashboard Page**

### You can see histories in Dashboard page



### If you want see history, Click one!





## My Page

### Update your personal data!



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