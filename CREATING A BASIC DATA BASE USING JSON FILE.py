#CREATING A BASIC DATA BASE PROGRAM
import json
global name
global data
def setup():
    while(1):
       print("1.CREATE\n2.UPDATE\n3.RETRIVE\n4.DELETE DATA\n5.EXIT")
       choice = int(input("ENTER YOUR CHOICE:"))
       if choice==1:
          details()
       elif choice==2:
          updating()
       elif choice==3:
          retreiving_data()
       elif choice==4:
            delete_data()
       elif choice==5:
          exit(1)

def details():
    global data
    data  = {
           'name' : input('name:'),
           'age': int(input("age:")),
           'relaionship status' : input("relation status:"),
           'loving person' : input("loving person:")
           }
    storing_data()
    print("@@@@DATA BASE IS CREATED@@@@")
    print("***DATA IS STORED IN DATA BASE***")
def updating():
    global data
    value_par = input("ENTER PARAMETER :")
    value_data  = input("ENTER DATA : ")
    data[value_par] = value_data
    data.update({value_par:value_data})
    storing_data()
    print("****DATA BASE IS UPDATED***")
def storing_data():
    global data
    with open("data_base.json",'w') as file:
        database = json.dump(data,file)
def retreiving_data():
    with open("data_base.json",'r') as file:
        retrive_data = json.load(file)
        print("****DATA STORED IN THE DATA BASE*****")
        print(retrive_data)
def delete_data():
    global data
    with open("data_base.json",'r') as file :
        data = json.load(file)
        print(data.keys())
        del_data = input("Enter key :")
        data.pop(del_data)
        storing_data()
        #print(data)
#DRIVER CODE
if __name__ == '__main__':
    setup()

    
    
