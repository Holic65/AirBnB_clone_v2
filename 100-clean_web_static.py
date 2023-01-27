#!/usr/bin/python3
''' a script that deletes out of date archives '''
from fabric.api import *
import os
env.hosts = ['ubuntu@54.85.93.141', 'ubuntu@34.201.165.179']


def do_clean(number=0):
    '''delete outofdate archives using num to count archives to delete'''
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    for i in range(number):
        archives.pop()
    with lcd("versions"):
        for a in archives:
            local("rm ./{}".format(a))

    with cd("/data/web_static/releases"):
        archives = run('ls -tr').split()
        archives = [a for a in archives if 'web_static_' in a]
        for i in range(number):
            archives.pop()
        [run('rm -rf ./{}'.format(a)) for a in archives]
