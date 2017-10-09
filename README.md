# yaml2eyaml
Converts hiera-yaml files to hiera-eyaml.

This was created to make the move from yaml to encrypted eyaml easier. The use case for this was with Puppet, moving unencrypted hieradata to encrypted hieradata.

## Requirements

hiera-eyaml:
gem install hiera-eyaml

ruamel.yaml:
pip install ruamel.yaml
