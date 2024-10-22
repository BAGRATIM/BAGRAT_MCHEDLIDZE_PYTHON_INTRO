#striqonis savarjisho

input_date=input("Please Enter Time: ")

if int(input_date[11:13])>12:
    hour=int(input_date[11:13])-12
else:
    hour=int(input_date[11:13])


print (input_date[8:10]+"-"+input_date[5:7]+"-"+input_date[0:4]+" "+str(hour)+":"+input_date[14:16]+":"+input_date[17:19]+" "
       +input_date[-6:-7:-1]+str(int(input_date[27:29])))