#This is a USSD Code Programm
#if No
def Selfregister():
  print("Thank you for choosing Qmoney")
  quit()
  Selfrgister()


#If Registration is yes
def Yes():
  print("Your number is not register,please go to the nearest Qmoney shop\n with a valid ID and register your line or send via \n whatsApp line to update your registration.")
  quit()
  Yes()



# Self Registration 
def SelfRedistration():
  print("Do you want to register for the QMoney?")
  options = input('''
1. Yes
2. No''')
  if options == '1':
   Yes()
  elif options == '2':
   Selfregister()
  else:
    print("Invalid please try again")
    quit()
    SelfRedistration()

#No. 8 to continue
def Before():
  print("_________________________")
  options = input('''
8. Customer Self Registration
9. Transaction Cost
10. My Account                             
''')
  print("__________________________")
  if options == '8':
   SelfRedistration()
  elif options == '9':
    print('Transaction Cost')
  elif options == '10':
    print('My Account')
  else:
    print('Invalid options')
    quit()
    Before()

#For The 260mb
def MB():
  amnt = '5'
  print(f"You are about to buy {amnt} LEONES to your account")
  ask = input("Please enter your password or 2 to cancel: ")
  if len(ask )== 4 and  ask.isnumeric() or ask == 2:
      print("Transction Successful")
  else:
      print("You have insaufficent balance to perform the transction")
      quit()

      MB()

#For The 70mb
def firm():
  amnt = '1'
  print(f"You are about to buy {amnt} LEONES to your account")
  ask = input("Please enter your password or 2 to cancel: ")
  if len(ask )== 4 and  ask.isnumeric() or ask == 2:
      print("Transction Successful")
  else:
      print("You have insaufficent balance to perform the transction")
      quit()

      firm()

#For The 15mb
def comfirm():
  amnt = '0.31'
  print(f"You are about to buy {amnt} LEONES to your account")
  ask = input("Please enter your password or 2 to cancel: ")
  if len(ask )== 4 and  ask.isnumeric() or ask == 2:
      print("Transction Successful")
  else:
      print("You have insaufficent balance to perform the transction")
      quit()

      comfirm()
#If Daily

def Daily():
  select = input('''
1. 15MB = Le0.31
2. 70MB = Le1
3. 260MB = Le5
''')
  if select == '1':
    comfirm()
  elif select == '2':
    print("70MB")
  elif select == '3':
    print("260MB")
  else:
    print("Invalid input")
    quit()
    Daily()

#To Buy Data Bundle for my number

def my_Number():
  Choose = input('''
1. DAILY
2. WEEKLY
3. MONTHLY                 

''')
  if  Choose == '1':
    Daily() 
  elif Choose == '2':
    firm()
  elif Choose == '3':
    MB()
  else:
    print("Invalid options")
    quit()

    my_Number()

#To Buy Data Bundle

def Bundle():
  amtt = input('''
1. Buy Data Bundle for my Number
2. Buy  Data Bundle for another Qcel Number
''')
  if amtt == '1':
    my_Number()
  elif amtt == '2':
    print("For another number")
  else:
    print("invalid option")
    quit()

    Bundle()

#To Top-Up anothoer Qcel Number

def TopUp():
  nums = input("Please enter the phone number of the customer: ")
  ammot = input("Please enter the amount OF tOP-uP you want to buy in SLE: ")
  print(f"you are about to buy Airtime of{ammot}SLE for the{nums}")
  ask = input("Please enter your password or 2 to cancel: ")
  if len(ask )== 4 and  ask.isnumeric() or ask == 2:
    print("🙌")
  else:
    print(Entryoption())
    quit()

    TopUp()

# to up my number
def mynumber():
  amout = float(input("Please enter the amount of Top-Up you want\nto buy in SLE:  "))
  print(f"You are about to buy airtime {amout} SLE")
  ask = input("Please enter your password or 2 to cancel: ")
  if len(ask )== 4 and  ask.isnumeric() or ask == 2:
    print("Complete")
  else:
   print(Entryoption())
  quit()
  mynumber()

def cho():
  options = input('''
1. Top UP My Number
2.Top Up another Qcel number
''')
  if options == '1':
   mynumber()
  elif options == '2':
    TopUp()
  else:
    print("Try again")
    quit()
    cho 

#if the user want to buy top up or data bundle through his/her Qmoney Account
def BuytopUp():
 init = input('''
1. Top-UP
2. Data Bundle
3. Night Browse
''')
 if init == '1':
   cho()
 elif init == '2':
  Bundle()
 elif init == '3':
  print("Night Browse")
 else:
  print("Nothing")
  quit()
  BuytopUp()

#if the  User want to buy Goods

def BuyGoods():
  code = input("Please enter the merchant code: ")
  if len(code) == 4 and code.isnumeric():
    print("Transction Successful")
    quit()
  else:
    print("Invalid merchant code or you have insufficient balance, please try again.")
    quit()
  BuyGoods()

#Oversea Transfer Senegal

def Sen():
  print("Send money to: Senegal")
  name = input("Enter name of your receiver: ")
  print(f"Send Money to: Senegal Receiver {name}")
  print("------------------------")
  num = input("Enter mobile number  of your receiver: ")
  if num == 'num':
    print('Successful')
  else:
    print('Incorrect Format please try again')
    quit()


  Sen()

#Oversea Transfer Guinea

def Gui():
  print("Send money to: Guinea")
  name = input("Enter name of your receiver: ")
  print(f"Send Money to: Guinea Receiver {name}")
  print("------------------------")
  num = input("Enter mobile number  of your receiver: ")
  if num == 'num':
    print('Successful')
  else:
    print('Incorrect Format please try again')
    quit()


  Gui()
#Oversea Transfer Liberia

def Lib():
  print("Send money to: Liberia")
  name = input("Enter name of your receiver: ")
  print(f"Send Money to: Lieria Receiver {name}")
  print("------------------------")
  num = input("Enter mobile number  of your receiver: ")
  if num == 'num':
    print('Successful')
  else:
    print('Incorrect Format please try again')
    quit()


  Lib()
#Check for the Token Number

def Token():
  print("Dear Customer this service has been suspended temporaly ")
  quit()
  Token()
#Buy EDSA TOP UP

def Buy():
  amtt = input("Enter the amount you want to pay in Leones: ")
  Meternum =  input ("Please enter your 11 digits EDSA Meter number: ")
  if amtt >= '50':
   print("Successful")
  else:
   print(f"The SLE {amtt} you enter is too low please enter amount greater than SLE {amtt}.")
   quit()
   if len(Meternum) == 11 and Meternum.isnumeric():
     print("You will receive the token number by sms.")
   else:
     print(f"The {Meternum} number you enter is invalid, please try again. ")
     quit()

   Buy()
#To Buy EDSA or Check for Token Number
def Edsa():
  option = input('''
1. Buy EDSA
2. Check for EDSA Token              
''')
  if option == '1':
   Buy()
  elif option == '2':
   Token()
  else:
    print("Invalid")
    quit()
  
  Edsa()
# If the user want to make payement througn Qmoney 
def Make():
  print("----------")
  lstvalue = input('''
1. EDSA
2. TV Station
3. QCEL Services
4. Water Companies
''')
  if lstvalue == '1':
   Edsa()
  elif lstvalue == '2':
    print("TV Station") 
  elif lstvalue == '3':
    print("QCEL Services")
  elif lstvalue == '4':
    print("Water Companies")
  else:
    print("Invalid input")
    Make()
    quit()
#Menu
def menu(): 
  Entryoption()  
  quit()
  
#Oversea Transfer
def Oversea():
  list = input('''
1. BnB
---

''')

  if list == '1':
   Choose = input('''
1. Liberia
2. Guinea
3. Senegal                  
4. Mali
5. Ivory Cost
6. Ghana
7. DR Congo
8. Burkinna Faso
9. Benin
10. Guinea Bissau
11. Gambia
12. Cameroom                 
13. TOGO                 

''') 
  if Choose == '1':
   Lib() 
  elif Choose == '2':
   Gui()
  elif Choose == '3':
   Sen()
  elif Choose == '4':
    print("Mali")
  elif Choose == '5':
    print("Ivory Cost")
  elif Choose == '6':
    print("Ghana")
  elif Choose == '7':
    print("DR Congo")
  elif Choose == '8':
    print("Burkinna Faso")
  elif Choose == '9':
    print("Benin")
  elif Choose == '10':
    print("Guinea Bissau")
  elif Choose == '11':
    print("Gambia")
  elif Choose == '12':
    print("Cameroom")
  elif Choose == '13':
    print("TOGO")
  else:
    print("Invalid Input")
   

  Oversea()
# Other Network

def Other():
  Number = input("Please enter the telephone number of the recipient: ")
  if len(Number) == 9 and Number.isnumeric():
   if Number == Number:
     Amt = float(input("Please enter the amount you want to transfer in SLE: "))
     transferfees = "1.00 "
  print(f"You are about to transfer Nle{Amt} on the account of {Number}\n Transfer fees is : {transferfees}SLE\n Total amount {Amt}\n")
  ask = input("Please enter your password or 2 to cancel: ")
  if len(ask )== 4 and  ask.isnumeric() or ask == 2:
     print("Successfiul")
  else:
   Entryoption()
 
   quit()

  Other()

#Asking the user if he want to us the Angent to transfer money #3457892

def Agent():
  code = input("Please enter the 7 digit code of the Agen: ")
  confirm = input("Please confirm your code: ")
  if confirm == code:
       if len(code) == 7 and code.isnumeric():
         print("Successful")
         quit()
  else:
      print("Sorry, the information is incorrect,please check and try angin.")
      quit()
      
  Agent() 
# Qmoney Customer
def Customer():
  phone = input("Please enter the receival phone number: ")
  confirm = input("Please confirm phone number: ")
  Amout = int(input("Please enter the amount you want to transfer: "))
  
  if confirm == phone:
       if len(phone) == 9 and phone.isnumeric():
         print(f"You will transfer Nle {Amout} ot {phone} SAMUEL SILLAH. Please enter your secret code to confirm the transfer or press 2 to cancel.")
         quit()      
  else:
       print("The phone number you enter is incorrect,please try again.")
       quit()
    
  Customer()

# Asking the user if he/she want to transfer money to another person 

def transfer():
 print("--------------")


 print(" Money Transfer")

 print("Choose option: ")
 opson = input('''
1. Qmoney Customer
2. An Agent
3. Other Network
4. Oversea Transfer
---
00: Menu
0:< 
''')
  
 if opson == '1':
   Customer()
 elif opson == '2':
  Agent()
 elif opson == '3':
  Other()
 elif opson == '4':
  Oversea()
 elif opson == '00':
  menu()
  Entryoption()
 elif opson == '0':
    print("Back")
 else:
    print("Invalid option")
 transfer()
#Asking the user to check his balance

def Balance():
  password = input("Enter your Qmoney Secret Code: ")
  if password == '4729':
    print("Your balance is Nle 1000")
    quit()
  else:
    print("Invalid Secret code, please try again")
    quit()
    Balance()

# To ask the user to enter his/her option 

def Entryoption():

 transcode = input('''
1. Check my Balance
2. Momey  Transfer
3. Make Payement
4. Buy Goods
5. Buy Top-Up / Data Bundle
6. Bank Account
---
8:->
''')
 if transcode == '1':
   Balance()
   quit()
 elif transcode == '2':
   transfer()
 elif transcode == '3':
  Make()
 elif transcode == '4':
  BuyGoods()
 elif transcode == '5':
  BuytopUp()
 elif transcode == '6':
   print("Bank Account")  
 elif transcode == '8':
  Before()
  
 elif transcode == '00':
   print("out")
 else:
   print("Invalid option")
   Entryoption()   

# Function to check the code 
def CONFIRMUSSD():


  Qmoneycode = (input("Enter the Qmoney code: "))
  if Qmoneycode == '*323#':
   print("Choose your option: ")
   Entryoption()
   quit()
  else:
    print("Invalid Qmoney code, please try again") 
    quit()
  CONFIRMUSSD()


#calling the function
CONFIRMUSSD()  

















