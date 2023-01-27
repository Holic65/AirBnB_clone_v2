#!/usr/bin/python3
''' a fabric script that creates and distributes an archive to server '''
from fabric.api import env, put, run, local
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['ubuntu@54.85.93.141', 'ubuntu@34.201.165.179']


def do_pack():
    ''' a script that creates an archive '''
    try:
        if not isdir('versions'):
            local('mkdir versions')
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = 'versions/web_static_{}.tgz'.format(date)
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except:
        return None


def do_deploy(archive_path):
    ''' a script that distributes archive to servers '''
    if exists(archive_path) is False:
        return False

    try:
        filename = archive_path.rsplit('/', 1)[-1]
        non_ext = filename.rsplit('.', 1)[0]
        filepath = '/data/web_static/releases/{}/'.format(non_ext)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(filepath))
        run('tar -xzf /tmp/{} -C {}'.format(filename, filepath))
        run('rm /tmp/{}'.format(filename))
        run('mv {}web_static/* {}'.format(filepath, filepath))
        run('rm -rf {}web_static'.format(filepath))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(filepath))
        return True
    except:
        return False


def deploy():
    ''' a script that creates and distributes archive to servers '''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
