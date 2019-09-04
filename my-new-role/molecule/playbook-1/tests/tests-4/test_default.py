import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_1(host):
    f = host.file('/tmp/local-myna.out')

    assert f.exists, "Output file does not exist"
    assert "MUTTATHORUMAINA" == f.content_string,  "Output file does not contain the right content."
