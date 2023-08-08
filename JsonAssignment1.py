# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.
import json
python_dict={'employee 1':{'Name':'Nischita Kotari',
                           'DOB':'02/07/2001',
                           'Height':'5.6ft',
                           'City':'Srikakulam',
                           'State':'Andhra Pradesh'},
            'employee 2':{'Name':'Rani',
                          'DOB':'19/06/2000',
                          'Height':'6ft',
                          'City':'Srikakulam',
                          'State':'Andhra Pradesh'},
            'employee 3':{'Name':'Akanksha',
                          'DOB':'21/03/1999',
                          'Height':'5.4ft',
                          'City':'Vishakapatnam',
                          'State':'Andhra Pradesh'},
            'employee 4':{'Name':'Sai',
                          'DOB':'06/09/1998',
                          'Height':'6ft',
                          'City':'Secunderabad',
                          'State':'Telanagana'},
            'employee 5':{'Name':'Nihal',
                          'DOB':'19/10/2001',
                          'Height':'6ft',
                          'City':'Secunderabad',
                          'State':'Telanagana'}}
with open('employee.json','w') as f:
    x=json.dump(python_dict,f,indent=10)
print()

#Expected Output:
# {
#           "employee 1": {
#                     "Name": "Nischita Kotari",
#                     "DOB": "02/07/2001",
#                     "Height": "5.5ft",
#                     "City": "Srikakulam",
#                     "State": "Andhra Pradesh"
#           },
#           "employee 2": {
#                     "Name": "Rani",
#                     "DOB": "19/06/2000",
#                     "Height": "6ft",
#                     "City": "Srikakulam",
#                     "State": "Andhra Pradesh"
#           },
#           "employee 3": {
#                     "Name": "Akanksha",
#                     "DOB": "21/03/1999",
#                     "Height": "5.5ft",
#                     "City": "Vishakapatnam",
#                     "State": "Andhra Pradesh"
#           },
#           "employee 4": {
#                     "Name": "Sai",
#                     "DOB": "06/09/1998",
#                     "Height": "6ft",
#                     "City": "Secunderabad",
#                     "State": "Telanagana"
#           },
#           "employee 5": {
#                     "Name": "Nihal",
#                     "DOB": "19/10/2001",
#                     "Height": "6ft",
#                     "City": "Secunderabad",
#                     "State": "Telanagana"
#           }
# }



class Employee:
    def __init__(self,name,dob,height,city,state):
        self.name=name
        self.dob=dob
        self.height=height
        self.city=city
        self.state=state

    def __str__(self):
        return f'Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}'
    
def main():
    employee_list=[]
    with open('employee.json','r') as f:
        employee_data=json.load(f)
    for emp_id, emp_info in employee_data.items():
        employee = Employee(emp_info['Name'], emp_info['DOB'], emp_info['Height'], emp_info['City'], emp_info['State'])
        employee_list.append(employee)

    for employee in employee_list:
        print(employee)
main()

#Expected Output:
# Name: Nischita Kotari, DOB: 02/07/2001, Height: 5.6ft, City: Srikakulam, State: Andhra Pradesh
# Name: Rani, DOB: 19/06/2000, Height: 6ft, City: Srikakulam, State: Andhra Pradesh
# Name: Akanksha, DOB: 21/03/1999, Height: 5ft, City: Vishakapatnam, State: Andhra Pradesh
# Name: Sai, DOB: 06/09/1998, Height: 6ft, City: Secunderabad, State: Telanagana
# Name: Nihal, DOB: 19/10/2001, Height: 6ft, City: Secunderabad, State: Telanagana



# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

seven_states={'Telanagana':'Hyderabad','AndhraPradesh':'Amaravathi','Odisha':'Bhubaneswar','Gujarat':'GandhiNagar','Tamil Nadu':'Chennai','Haryana':'Chandighar','Jammu_Kashmir':'Srinagar'}
with open('seven_states.json','w') as f:
    x=json.dump(seven_states,f,indent=5)

#Expected Output:
# {
#      "Telanagana": "Hyderabad",
#      "AndhraPradesh": "Amaravathi",
#      "Odisha":"Bhubaneswar",
#      "Gujarat": "GandhiNagar",
#      "Tamil Nadu":"Chennai",
#      "Haryana": "Chandighar",
#      "Jammu_Kashmir": "Srinagar"
# }
