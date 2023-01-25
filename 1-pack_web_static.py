#!/usr/bin/python3
''' a fabric script that generates a .tgz archive '''
from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """ a function that generates .tgz archive """
    try:
        datename = datetime.now().strftime("%Y%B%D%M%S")
        if not isdir('versions'):
            local('mkdir versions')
        arch_name = 'versions/web_static_{}.tgz'.format(datename)
        local('tar -zcvf {} web_static'.format(arch_name))
        return arch_name
    except:
        return None
