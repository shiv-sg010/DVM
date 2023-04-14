import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="root",
                             database="online")
mycur=mydb.cursor()

def value():
                print("enter user_name")
                x=input()
                sql="select exists(select user_name from admin where user_name=%s)"
                mycur.execute(sql,(x,))
                if (mycur.fetchone()[0]==0):
                    print("user_name does not exists. enter again")
                    value()
                print("enter password")
                y=input()
                sql1="select password from admin where user_name= %s"
                mycur.execute(sql1,(x,))
                if (y!="".join(mycur.fetchone()[0])):
                    print("incorrect password. enter again")
                    value()
                else:
                    admin()
def  login():
    print("1. Login as admin")
    print("2. create a new admin")
    choice=input()
    if choice=="1":
            value()            
    if choice=="2":
            print("enter the user_name")
            x=input()
            print("enter the password")
            y=input()
            sql="insert into admin values(%s,%s)"
            mycur.execute(sql,(x,y,))
            mydb.commit()
    else:
        login()
    print("login to continue")
    value()
list=["id","name","class","address","ph_no","guardians_name","guardians_no","email id","DOB"]
list2=["id","first_quarter","second_quarter","third_quarter"]
list3=["tid","name","address","ph_no","email_id","DOB","subject"]
def info(id):
      sql="select * from student where id=%s"
      mycur.execute(sql,(id,))
      myr=mycur.fetchall()
      for i in myr:
          for j in range (0,len(list)):
               print (list[j]," ",i[j])
def info2(tid):
      sql="select * from teacher where tid=%s"
      mycur.execute(sql,(tid,))
      myr=mycur.fetchall()
      for i in myr:
          for j in range (0,len(list3)):
               print (list3[j]," ",i[j])               
def fee_info(id):
    sql3="select * from fees where id=%s"
    mycur.execute(sql3,(id,))
    myr=mycur.fetchall()
    for i in myr:
                   for j in range(0,len(list2)):
                           print (list2[j]," ",i[j])
def main_info():
        print("1. student_info")
        print("2. add new student")
        print("3. fees management")
        print("enter any other option to return")
        a=input()
        if a=="1":
               def input1():
                       print("1. view details")
                       print("2. edit details")
                       print("enter any other input to return")
                       s1=input()
                       if s1=="1":
                           print("enter id number of student for viewing")
                           id=input()
                           info(id)
                           
                       elif s1=="2":
                            def edit():
                             print("enter id number of student for editing")
                             id=input()
                             for k in range(1,len(list)):
                                       print(k,"for",list[k])
                             w1=input()
                             print("enter new",list[int(w1)])
                             w=input()
                             sql1="update student set "
                             sql2="=%s where id=%s"
                             mycur.execute((sql1+list[int(w1)]+sql2),(w,id,))
                             mydb.commit()
                             info(id)
                             print("enter 0 to save & exit and 1 to edit more")
                             f=input()
                             if f=="0":
                                    mydb.commit()
                             elif f=="1":
                                    mydb.commit()
                                    edit()
                             else:
                                    print("Invalid input. Try again")
                                    edit()
                            edit()
                       else:
                            main_info()
                       input1()
               input1()            
        elif a=="2":
               print ("enter details of new student")
               tuple1=()
               for k in range(0,len(list)):
                      print ("enter",list[k])
                      x=input()
                      tuple1=tuple1+(x,)
               sql2="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)"
               mycur.execute(sql2,tuple1)
               mydb.commit()
               info(tuple1[0])
        elif a=="3":
          def info1():
                       print("enter 1 for view fees status")
                       print("enter 2 for fees update")
                       print("enter any other option to return")
                       s2=input()
                       if s2=="1":
                         print("enter id_no of the student")
                         id=input()
                         fee_info(id)
                       elif s2=="2":
                         def edit1():
                                 print("enter id_no of the student")
                                 id=input()
                                 print("enter quarter no")
                                 ip=input()
                                 sql4="update fees set "
                                 sql5="='yes' where id=%s"
                                 mycur.execute((sql4 + list2[int(ip)] + sql5),(id,))
                                 mydb.commit()
                                 fee_info(id)
                                 print("enter 0 to save & exit and 1 update more")
                                 f=int(input())
                                 if f==0:
                                       mydb.commit()
                                 elif f==1:
                                       mydb.commit()
                                       edit1()
                                 else:
                                       print("Invalid input. Try again")
                                       edit1()
                         edit1()
                       else:
                              main_info()
                       info1()       
          info1()  
        else:
          admin()
        main_info()

def main_info1():
      print("1. teacher_info")
      print("2. add new teacher")
      print("enter any other option to return")
      a=input()
      if a=="1":
            def input2():
                       print("1. view details")
                       print("2. edit details")
                       print("enter any other input to return")
                       s1=input()
                       if s1=="1":
                           print("enter tid number of teacher for viewing")
                           tid=input()
                           info2(tid)
                           
                       elif s1=="2":
                            def edit3():
                             print("enter tid number of teacher for editing")
                             tid=input()
                             for k in range(1,len(list3)):
                                       print(k,"for",list3[k])
                             w1=input()
                             print("enter new",list3[int(w1)])
                             w=input()
                             sql1="update teacher set "
                             sql2="=%s where tid=%s"
                             mycur.execute((sql1+list3[int(w1)]+sql2),(w,tid,))
                             mydb.commit()
                             info2(tid)
                             print("enter 0 to save & exit and 1 to edit more")
                             f=input()
                             if f=="0":
                                    mydb.commit()
                             elif f=="1":
                                    mydb.commit()
                                    edit3()
                             else:
                                    print("Invalid input. Try again")
                                    edit3()
                            edit3()
                       else:
                            main_info1()
                       input2()
            input2()            
      elif a=="2":
               print ("enter details of new teacher")
               tuple1=()
               for k in range(0,len(list3)):
                      print ("enter",list3[k])
                      x=input()
                      tuple1=tuple1+(x,)
               sql2="insert into teacher values(%s,%s,%s,%s,%s,%s,%s)"
               mycur.execute(sql2,tuple1)
               mydb.commit()
               info2(tuple1[0])
      else:
          admin()
      main_info1()    
def admin():
    print("1. student")
    print("2. Teacher")
    print("enter any other input to go back")
    z=input()
    if   z=="1":
          main_info()
    elif z=="2":
          main_info1()
    else:
          main()
        



def teach():
    print ("enter your tid")
    tid=input()
    mycur.execute("select tid,DOB from teacher")
    myr=mycur.fetchall()
    li=[]
    ld=[]
    for i in myr:
        li.append(i[0])
        ld.append(i[1])
    if tid not in li :
        print("invalid tid")
        teach()
    print("enter your password (DOB - format - YYYY-MM-DD)")
    dob=input()
    if dob not in ld :
        print("invalid password ")
        teach()
    sql="select * from teacher where tid = %s"
    mycur.execute(sql,(tid,))
    i=mycur.fetchone()
    print("tid=",i[0]+"\n"+"name=",i[1]+"\n"+"address=",i[2]+"\n"+"ph_no=",
                  i[3]+"\n"+"email_id=",i[4]+"\n"+"DOB=",i[5]+"\n"+"subject=",i[6])
    teacher()
    
def teacher():
    print("enter 1 for no of students in class")
    print("enter 2 for details of specific student")
    print("enter 3 for uploading books and study material ")
    print("enter 4 for uploading video classes ")
    print("enter 5 for uploading tests ")
    print("enter 6 to view doubts and answer")
    print("enter any other input to go back")
    a=input()
    ch=0
    if a=="1" :
        while (ch==0):
            print ("enter class")
            cl=(input())
            sql1="select id , name from student where class =%s"
            mycur.execute(sql1 , (cl,))
            myr=mycur.fetchall()
            for i in myr:
                print("id=",i[0]+"\t"+"name=",i[1])
            sql1="select count(*) from student where class =%s "
            mycur.execute(sql1 , (cl,))
            myr1=mycur.fetchall()
            print( " total number of students =", myr1)
            print("enter 0 to repeat the same and 1 to go back ")
            ch=int(input())
        teacher()    
        
    elif a=="2":
        while(ch==0):
            print("enter the id_no of th student")
            id=input()
            sql1="select * from student where id=%s"
            mycur.execute(sql1,(id,))
            myr=mycur.fetchall()
            for i in myr:
                print("id=",i[0]+"\n"+"name=",i[1]+"\n"+"class=",i[2]+"\n"+"address=",i[3]+"\n"+"ph_no=",i[4]+"\n"+"guardans_name=",i[5]+"\n"+"guardians_no=",i[6]+"\n"+"email_id=",i[7]+"\n"+"DOB=",i[8])
            print("enter 0 to repeat the same and 1 to go back ")
            ch=int(input())
        teacher()
    elif a=="3":
        while(ch==0):
            f=open("book.txt","a+")
            f.seek(0)
            print ("enter class for which book is meant")
            cl=input()
            print ("enter subject")
            sub=input()
            print("enter link with book name")
            link=input()
            str=cl +" " + sub + " " + link+".pdf"
            f.write(str)
            f.close()
            print("enter 0 to repeat the same and 1 to go back ")
            ch=int(input())
        teacher()
    elif a=="4":
        while (ch==0):
            f=open("video.txt","a+")
            f.seek(0)
            print ("enter class for which video is meant")
            cl=input()
            print ("enter subject")
            sub=input()
            print("enter chapter")
            ch=input()
            print ("enter link")
            link=input()
            str=cl +" " + sub + " " +ch + " " +link+".mp4"
            f.write(str)
            f.close()
            print("enter 0 to repeat the same and 1 to go back ")
            ch=int(input())
        teacher()
    elif a=="5":
        while (ch==0):
            f=open("test.txt","a+")
            f.seek(0)
            print ("enter class for which test is meant")
            cl=input()
            print ("enter subject")
            sub=input()
            print("enter chapter")
            ch=input()
            print("enter link")
            link=input()
            str=cl +" " + sub + " " +ch + " " + link
            f.write(str)
            f.close()
            print("enter 0 to repeat the same and 1 to go back ")
            ch=int(input())
        teacher()
    elif a=="6":
        while (ch==0):
            f=open("doubt.txt","a+")
            f.seek(0)
            f1=open("solution.txt","a+")
            f1.seek(0)
            print ("enter class")
            cl=input()
            print("enter subject")
            sub=input()
            l=[]
            s=cl+" "+sub
            for x in f:
                if s in x:
                    l=x.split()
                    print("doubt=",l[3])
                    print("Enter your answer")
                    ans=input()
                    l.append(ans)
                    str=str.join(l)
                    f1.write(str)
            f1.close()
            f.close()
            print("enter 0 to repeat the same and 1 to go back ")
            ch=int(input())
        teacher()
    else:
        main()
import PyPDF2
def pdf(pdfName):
    read_pdf=PyPDF2.PdfFileReader(pdfName)
    for i in range(read_pdf.getNumPages()):
        page=read_pdf.getPage(i)
        print ("page no=",str(1+read_pdf.getPageNumber(page)))
        page_content=page.extractText()
        print (page_content)

def PlayVideo(video_path):
        import cv2
        import numpy as py
        from ffpyplayer.player import MediaPlayer
        import time
        video=cv2.VideoCapture(video_path)
        player = MediaPlayer(video_path)
        print("enter q to stp the video")
        while True:
            grabbed,frame=video.read()
            audio_frame,val=player.get_frame()
            if not grabbed:
                print ("end of video")
                break
            if cv2.waitKey(36) & 0xFF == ord("q"):
                break
            cv2.imshow("Video",frame)
            if val=="eof":
                    break
            elif audio_frame is None:
                    time.sleep(0.01)
            else:
                    img,t=audio_frame
        video.release()
        cv2.destroyAllWindows()
def student():
    print ("enter your id")
    id=input()
    sql=""
    mycur.execute("select id,DOB from student")
    myr=mycur.fetchall()
    li=[]
    ld=[]
    for i in myr:
        li.append(i[0])
        ld.append(i[1])
    if id not in li :
        print("invalid id")
        student()
    print("enter your password (DOB - format - YYYY-MM-DD)")
    dob=input()
    if dob not in ld :
        print("invalid password ")
        student()
    sql="select * from student where id = %s"
    mycur.execute(sql,(id,))
    trx=mycur.fetchone()
    print("id=",trx[0]+"\n"+"name=",trx[1]+"\n"+"class=",trx[2]+"\n"+"address=",trx[3]+"/n"+"ph_no=",
                  trx[4]+"\n"+"guardans_name=",trx[5]+"\n"+"guardians_no=",trx[5]+"\n"+"email_id=",trx[6]+"\n"+"DOB=",trx[7]+"\n")
    choice(trx[2],trx[0])
def choice(trx,id):
        print ( "Enter 1 for seeing the books "+"\n"+"Enter 2 for seeing the video lecture"+"\n"+"Enter 3 for giving test"+"\n"+
            "Enter 4 for asking doubts"+"\n"+"Enter 5 for viewing the answers of the doubt"+"\n"+"Enter any other choice to exit")
        ch=input()
        if ch=="1" :
            print("enter subject")
            sub=input()
            f=open(r"C:\Users\Chirag\Desktop\book.txt","a+")
            f.seek(0)
            c=0
            l=[]
            lb=[]
            for x in f :
                s=trx+" "+sub
                if s in x :
                    c=1
                    l=x.split()
                    st=""
                    for k in range(2,len(l)):
                        st=st+l[k]+" "
                    lb.append(st)
            if c==0 :
                print ("No book has been uploaded for that particular subject")
                choice(trx,id)
            for x in range (0,len(lb)):
                print ("Book no =",(x+1))
                print("Book link=",lb[x])
            print( "Enter the book number you want to see ")
            b=int(input())
            st=lb[b-1]
            pdf(st)
            choice(trx,id)
        elif ch=="2" :
            print("enter subject")
            sub=input()
            print("enter chapter")
            chap=input()
            f=open(r"C:\Users\Chirag\Desktop\video.txt","a+")
            f.seek(0)
            c=0
            l=[]
            lb=[]
            str=""
            for x in f :
                s=trx+" "+sub+" "+chap
                if s in x :
                    c=1
                    l=x.split()
                    for k in range(3,len(l)):
                        str=str+l[k]+" "
                    lb.append(str)
            if c==0 :
                print ("No video has been uploaded for that particular chapter")
                choice(trx,id)
            for i in range (0,len(lb)):
                print ("video no =", (i+1))
                print("video link=",lb[i])
            print( "Enter the video number you want to see ")
            b=int(input())
            s=lb[b-1]
            PlayVideo(s)
            choice(trx,id)
        elif ch=="3" :
            print("enter subject")
            sub=input()
            print("enter chapter")
            chap=input()
            f=open("test.txt","a+")
            f.seek(0)
            c=0
            l=[]
            lb=[]
            for x in f :
                s=trx+" "+sub+" "+chap
                if s in x :
                    c=1
                    l=x.split()
                    lb.append(l[3])
            if c==0 :
                print ("No test has been uploaded for that particular chapter")
                choice(trx,id)
            for i in range (0,len(lb)):
                print ("test no =", (i+1)+"\n"+"test link=",lb[i])
            print( "Enter the test number you want to solve ")
            b=int(input())
            s=lb[b-1]
            pdf(s)
            choice(trx,id)
        elif ch=="4" :
            print("enter subject")
            sub=input()
            f=open("doubt.txt","a+")
            f.seek(0)
            print("enter your doubt")
            do=input()
            f.write(id+trx+sub+do)
            f.close()
            choice(trx,id)
        elif ch=="5" :
            print("enter subject")
            sub=input()
            f=open("solution.txt","a+")
            f.seek(0)
            s=id+trx+sub
            ld=[]
            for x in f:
                if s in f :
                    ld=x.split()
                    if len(ld)!=5 :
                        print("Doubt not answered")
                        choice(trx,id)
                    print(ld[4])
                    choice(trx,id)
            print("no doubt found")
            choice(trx,id)
        else :
            main()
            
            
            
            
        
def main():
    print("enter 1 for admin")
    print("enter 2 for teacher")
    print("enter 3 for student")
    chu=input()
    if(chu=="1"):
        login()
    elif(chu=="2"):
        teach()
    elif(chu=="3"):
        student()
    else:
        print("invalid")
main()
