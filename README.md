# RainforestApp
Rainforest App assesment

For this application, the stack that I am using is Django, Docker and PostgresSQL

*Docker = 20.10.10*

The goal is to create an API as per below:
 
REST API
1. 	Add product(s) to the shop.
Product has at least the following fields:
1.1.  Id
1.2.  Name
1.3.  Unit cost
1.4.  Price
1.5.  Available Units for sell
2. 	Update product(s) information
2.1.  Available units
2.2.  Unit cost
2.3.  Price
3. 	Get product list
4. 	Create Order / Buy Product
5. 	Cancel Order
6. 	Refund
7. 	Get summary data based on selected date range and grouped next information by every product:
7.1.  Income
7.2.  Profit
7.3.  Units sold
7.4.  Orders count
7.5.  Refunds information
 
<h1>How to run application on local:</h1>

Run command:
Step 1
```
docker-compose build

```
<img src = "image/Screenshot%202021-11-26%20223410.png">

Step 2
```
docker-compose up

```
<img src = "image/Screenshot%202021-11-26%20223454.png" >


Once done with *Step 2* the application is up and ready to be use locally.

For further info on API specification please refer the link below:
https://documenter.getpostman.com/view/10701397/UVJbHdFy

