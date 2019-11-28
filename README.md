# SDE - Assignment
The entry management system has been designed as per the requirements stated in the problem statement
Django has been used as the library to integrate web application with python

## System Requirements
1. Python
2. Django
3. Web browser
4. Postgre SQL

## Approach
The front-end has been designed as a web based interface. The data are stored at the backend in PostgreSQL. 

### User home page
![Home](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/home.png)
The above page is displayed to the user with options Check in, Check Out and Visitor details
The user must click check in to enter new visitor details

### Check in form
![Check in](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/chekin.png)
This form asks for visitor details and host details that he is about to visit as per the requirement stated in problem statement
After the details of host and visitor are entered, once check in button is clicked. It triggers an email and sms to host.

#### Email
![Email](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/mail2.png)

The mail id used as sender in this automation is rajabadhar.vidathusirippu@gmail.com which is specifically created for the purpose of assignment. The mail with visitor details is sent to host email as shown above.

#### SMS alert
![SMS](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/sms.png)

The Fast2SMS server has been used to send sms to host. The host receives visitor details through sms also as soon as he clicks Check In.

#### Back-end
![backend](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/vd.png)

The data is stored at backend in Postgre SQL database - as shown in above figure

### Check Out
![Check Out](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/checkout0.png)

The visitor before leaving the office must fill the checkout form. As prescribed in the problem statement check out time is obtained from the visitor and not automated by the system. To identify the visitor uniquely mobile number of visitor is used.
After entering it checks the database for visitor details. Upon successful return, it displays the visitor details in table format as shown below.

### Check Out- table
![CheckOut](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/checkout2.png)

After verifying the details he/she can enter checkout time and click check button. This triggers an e-mail to the vistor with the complete form asking for details as stated in the problem

### E-mail to visitor
![E-Mail](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/comail2.png)
The E-mail has a link to the form

### Details form
![Details](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/details.png)
After clicking save button. It shows details saved successfully page.
![Save](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/success.png)

### Back-end data entry
![Backend](https://github.com/latha-velmurugan123/IndividualOne/blob/master/Web%20Files/Output/vd2.png)
The data is successfully captured at the backend which could be used later for any other purpose.


This project uses Django library, HTML and CSS to design an entry management system. Development server available in Django has been used as server.

BY G. Thilakar Rajaa
