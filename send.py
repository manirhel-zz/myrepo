#Mail Sender
import mysql.connector
from mysql.connector import Error

import smtplib

import config


mydb = mysql.connector.connect(
  host="localhost",
  user="fluxday",
  passwd="p@ssw0rd",
  database="fluxday"
)

def send_email(subject, msg, mail):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg, mail)
        server.sendmail(config.EMAIL_ADDRESS, mail, message)
        server.quit()
        
        #mycursor = mydb.cursor()  
        #insert_query = "INSERT into email (user_id,task_id,name,email_ID,status) VALUES (%s,%s,%s,%s,'1')"
       # val = (userid,taskid,username,eamilid) 
       # mycursor.execute(insert_query, val)
       # mydb.commit()
        print("Success: Email sent!") 
    except:
        #mycursor = mydb.cursor()  
        #insert_query = "INSERT into email (user_id,task_id,name,email_ID,status) VALUES (%s,%s,%s,%s,'0')"
        #val = (userid,taskid,username,eamilid) 
        #mycursor.execute(insert_query, val)
        #mydb.commit()
        print("Failed: Email not sent")
        
mycursor = mydb.cursor()

mycursor.execute("select id as userid,email,name,group_concat(taskname) as taskname  , group_concat(taskid) as taskid from (SELECT t.id as taskid,t.name as taskname,u.id,u.email, u.name ,t.start_date,t.end_date FROM users u inner join key_results r on u.id=r.user_id inner join task_key_results tkr on tkr.key_result_id =r.id inner join  tasks t on t.id =tkr.task_id where Date_Format(t.start_date,'%m/%d/%Y') =Date_Format(CURDATE(),'%m/%d/%Y') and not exists (select  * from email e  where e.user_id=u.id  and e.task_id = t.id and e.status=1 ) group by t.id,t.name,u.id,u.email,t.start_date,t.end_date) as mytable group by id")

myresult = mycursor.fetchall()

for x in myresult:

  subject = "Today's Task"
  msg = " Dear " + x[2] + "," + "\n\t\t\t" + "Please find your Today's task's" + x[3]
  mail_id = x[1]

  send_email(subject,msg,mail_id)  

mycursor.execute("SELECT t.id as taskid,t.name as taskname,u.id,u.email, u.name ,t.start_date,t.end_date FROM users u inner join key_results r on u.id=r.user_id inner join task_key_results tkr on tkr.key_result_id =r.id inner join  tasks t on t.id =tkr.task_id where Date_Format(t.start_date,'%m/%d/%Y') =Date_Format(CURDATE(),'%m/%d/%Y') and not exists (select  * from email e  where e.user_id=u.id  and e.task_id = t.id and e.status=1 ) group by t.id,t.name,u.id,u.email,t.start_date,t.end_date")

myresult1 = mycursor.fetchall()

for z in myresult1:
  userid = z[2]
  eamilid = z[3]
  username = z[4]
  taskid = z[0]
