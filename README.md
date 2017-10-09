# yaml2eyaml
Converts hiera-yaml files to hiera-eyaml.

This was created to make the move from yaml to encrypted eyaml easier. The use case for this was with Puppet, moving unencrypted hieradata to encrypted hieradata.

## Important notes
This version does not retain comments made in original YAML files. Sorry :)

## Requirements

hiera-eyaml:
gem install hiera-eyaml

ruamel.yaml:
pip install ruamel.yaml

## Use

./yaml2eyaml /path/to/yaml/files/ /path/to/final/destination/
