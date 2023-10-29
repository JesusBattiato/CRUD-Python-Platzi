import click
from employees import commands as employees_command


EMPLOYEES_TABLE = '.employees.csv'


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['employees_table'] = EMPLOYEES_TABLE

cli.add_command(employees_command.all)

if __name__=='__main__':
    cli()