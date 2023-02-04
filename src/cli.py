import click

@click.group()
def prisma2mermaid():
    pass

@click.command()
def generate():
    pass

prisma2mermaid.add_command(generate)
