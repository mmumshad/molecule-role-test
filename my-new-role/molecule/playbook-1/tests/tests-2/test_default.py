import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_1(host):
    original_file =  host.file('/etc/hosts')
    f = host.file('/tmp/hosts')

    assert f.exists, "Copy file does not exist"
    assert re.search('10.10.10.10\s+phantom-server', original_file.content_string) is not None,  "New line not in new file"
