import click
import os
import git

from changelog.gitrepo import Repo

filename = 'CHANGELOG.md'

@click.group()
def generator():
    pass

@generator.command()
@click.argument('repopath', default='.')
@click.option("--types", default='feat,fix,refactor,docs', help="commit types to show in changelog")
@click.option("--bodytags", default='BREAKING CHANGE,MAJOR', help="body tags that schould be shown in changelog")
def generate(repopath, types, bodytags):
    repo = Repo(repopath)
    types = types.split(',')
    bodytags = bodytags.split(',')
    text = repo.generate_changelog(types, bodytags)
    if text:
        with open(repopath + '/' + filename, 'w') as out_file:
            out_file.write(text)
        print('Done!')

@generator.command()
@click.argument('repopath', default='.')
@click.option("--types", default='feat,fix,refactor,docs', help="commit types to show in changelog")
@click.option("--bodytags", default='BREAKING CHANGE,MAJOR', help="body tags that schould be shown in changelog")
def add(repopath, types, bodytags):
    repo = Repo(repopath)
    types = types.split(',')
    bodytags = bodytags.split(',')
    try:
        with open(os.path.join(repopath, filename), 'r') as in_file:
            old_text = in_file.read()
    except FileNotFoundError:
        print("No CHANGELOG.md found")
        return
    text = repo.add_changelog(old_text, types, bodytags)
    if text:
        with open(os.path.join(repopath, filename), 'w') as out_file:
            out_file.write(text)
        print('Done!')

@generator.command()
@click.argument('repopath', default='.')
@click.option("--types", default='feat,fix,refactor,docs', help="commit types to show in changelog")
@click.option("--bodytags", default='BREAKING CHANGE,MAJOR', help="body tags that schould be shown in changelog")
def printout(repopath, types, bodytags):
    repo = Repo(repopath)
    types = types.split(',')
    bodytags = bodytags.split(',')
    print(repo.generate_changelog(types, bodytags))

if __name__ == '__main__':
    generator()
    