import csv
from employees.models import Employee
import os





class EmployeeService:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_employee(self, employee):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Employee.schema())
            writer.writerow(employee.to_dict())

    def list_employees(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f,fieldnames=Employee.schema())
            
            return list(reader)
        
    def update_employee(self, updated_employee):
        employees = self.list_employees()

        updated_employees = []
        for employee in employees:
            if employee['uid'] == updated_employee.uid:
                updated_employees.append(updated_employee.to_dict())
            else: 
                updated_employees.append(employee)

        self._save_to_disk(updated_employees)
    
    def _save_to_disk(self, employees):
        tmp_table_name = self.table_name + '.tmp'

        with open(tmp_table_name, mode='w') as f:
              writer = csv.DictWriter(f, fieldnames=Employee.schema())
              writer.writerows(employees)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)

    def delete_employee(self, deleted_employee):
        employees = self.list_employees()
        employees.remove(deleted_employee.to_dict())
        self._save_to_disk(employees)
