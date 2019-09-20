import sml
import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--table', help='table name')
@click.argument('path')
def load(table, path):
    click.echo('Initialized the table')

    translater = sml.CSVTranslater(path)

    dfn = sml.YamlDefine(translater.yaml())
    dfn.parse()

    dfn.to_structure_query_language()

cli.add_command(load)

if __name__ == '__main__':
    cli()