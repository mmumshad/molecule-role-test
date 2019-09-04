import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_1(host):
    original_file =  host.file('/etc/hosts')
    f = host.file('/tmp/hosts')

    assert f.exists, "File does not exist"
    assert f.content_string == original_file.content_string, "Contents don't match"
