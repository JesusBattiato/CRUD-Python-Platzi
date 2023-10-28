import click


from employees import command as employees_command

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}

cli.add_command(employees_command.all)

if __name__=='__main__':
    cli()