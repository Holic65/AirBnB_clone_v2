#!/usr/bin/python3
''' a fabric script that distributes an archive to a server '''
from fabric.api import put, sudo, env, run
from os.path import exists
env.hosts = ['ubuntu@54.85.93.141', 'ubuntu@34.201.165.179']


def do_deploy(archive_path):
    ''' function that uploads to server and uncompress the archive file '''
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.rsplit('/', 1)[-1]
        filenamextn = filename.rsplit('.', 1)[0]
        filepath = '/data/web_static/releases/{}/'.format(filenamextn)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(filepath))
        run("tar -xzf /tmp/{} -C {}".format(filename, filepath))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(filepath, filepath))
        run("rm -rf {}web_static".format(filepath))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(filepath))
        return True
    except:
        return False
