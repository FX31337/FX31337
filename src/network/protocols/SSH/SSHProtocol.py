import subprocess
import sys

# @file
# Implements SSH.
# Refs:
# - https://gist.github.com/bortzmeyer/1284249
# Notes:
# - Ports are handled in ~/.ssh/config since we use OpenSSH.

class SSHProtocol():
    _host = "www.example.org"

    def exeCmd(self, cmd):

        ssh = subprocess.Popen(["ssh", "%s" % self._host, cmd],
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        result = ssh.stdout.readlines()
        if result == []:
            error = ssh.stderr.readlines()
            print("ERROR: %s" % error)
        else:
            print(result)