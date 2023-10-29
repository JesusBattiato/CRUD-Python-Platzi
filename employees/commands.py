import click
from employees.services import EmployeeService
from employees.models import Employee

@click.group()
def employees():
    '''Manages the employees lifecycle'''
    pass


@employees.command()
@click.option('-n','--name',
                type=str,
                prompt=True,
                help='The Employee name'
                )
@click.option('-c','--company',
                type=str,
                prompt=True,
                help='The Employee company'
                )
@click.option('-e','--email',
                type=str,
                prompt=True,
                help='The Employee email'
                )
@click.option('-p','--position',
                type=str,
                prompt=True,
                help='The Employee position'
                )   
                
@click.pass_context
def create(ctx, name, company, email, position):
    '''Creates a new employee'''
    employee = Employee(name, company, email, position)
    employee_service = EmployeeService(ctx.obj['employees_table'])

    employee_service.create_employee(employee)

@employees.command()
@click.pass_context
def list(ctx):
    '''List all Employees'''
    employee_service = EmployeeService(ctx.obj['employees_table'])

    employees_list = employee_service.list_employees()
    
    click.echo(' ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('-' * 100)

    for employee in employees_list:
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = employee['uid'],
            name = employee['name'],
            company = employee['company'],
            email = employee['email'],
            position = employee['position']
        ))


@employees.command()
@click.argument('employee_uid',
                type=str)   
@click.pass_context
def update(ctx, employee_uid):
    '''Update an employee'''
    employees_service = EmployeeService(ctx.obj['employees_table'])

    employee_list = employees_service.list_employees()

    employee = [employee for employee in employee_list if employee['uid'] == employee_uid]

    if employee:
        employee = _update_employee_flow(Employee(**employee[0]))
        employees_service.update_employee(employee)
    else:
        click.echo('Employee not found')

def _update_employee_flow(employee):
    click.echo('Leave empty if you dont want to modify the value')

    employee.name = click.prompt('New Name', type=str, default=employee.name)
    employee.company = click.prompt('New company', type=str, default=employee.company)
    employee.email = click.prompt('New email', type=str, default=employee.email)
    employee.position = click.prompt('New position', type=str, default=employee.position)

    return employee


@employees.command()
@click.argument('employees_uid',
                type=str)
@click.pass_context
def delete(ctx, employees_uid):
    '''Delete an employee'''
    employees_service = EmployeeService(ctx.obj['employees_table'])
    employees_list = employees_service.list_employees()

    employee = [employee for employee in employees_list if employee['uid'] == employees_uid ]

    if employee:
        employees_service.delete_employee(Employee(**employee[0]))
    else:
        click.echo('Employee not found')


all = employees
