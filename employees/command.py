import click


@click.group()
def employees():
    '''Manages the employees lifecycle'''
    pass


@employees.command()
@click.pass_context
def create(ctx, name, company, email, position):
    '''Creates a new employee'''
    pass


@employees.command()
@click.pass_context
def list(ctx):
    '''List all Employees'''
    pass


@employees.command()
@click.pass_context
def update(ctx, employees_uid):
    '''Update an employee'''
    pass


@employees.command()
@click.pass_context
def delete(ctx, employees_uid):
    '''Delete an employee'''
    pass

all = employees
