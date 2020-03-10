# Changelog Generator

A module that generates changelogs based on git tags.
It uses conventional commits (https://www.conventionalcommits.org) to read and scope commits.
Markdown is used for formating.

## Commands

pychangelog generate
* generates new CHANGELOG.md file at repo root
* overrides old CHANGELOG.md

pychangelog add
* ceeps the content of the old CHANGELOG.md while adding new version logs

pychangelog printout
* prints the generated changelog in terminal instead of writing it in the CHANGELOG.md
* does not touch the CHANGELOG.md

## Options

--types     |comma seperated list   |commit types to show in changelog
--bodytags  |comma seperated list   |body tags that schould be shown in changelog
