#!/usr/bin/python3
"""Fabric Script that distributes an archive to web servers using Fabric 3.x"""

from fabric import Connection
from invoke import UnexpectedExit
from os.path import exists

# Define the remote hosts and user
hosts = ['3.92.214.122', '3.88.21.35']
user = 'ubuntu'

def do_deploy(archive_path):
    """Distributes the archive to web servers"""
    if not exists(archive_path):
        print(f"Archive path {archive_path} does not exist.")
        return False

    file_n = archive_path.split("/")[-1]
    no_ext = file_n.split(".")[0]
    remote_path = "/data/web_static/releases/"

    try:
        for host in hosts:
            print(f"Connecting to {host}...")
            c = Connection(host=host, user=user)

            print(f"Uploading {file_n} to /tmp/...")
            c.put(archive_path, f'/tmp/{file_n}')

            print(f"Creating directory {remote_path}{no_ext}/...")
            c.run(f'mkdir -p {remote_path}{no_ext}/')

            print(f"Extracting archive...")
            c.run(f'tar -xzf /tmp/{file_n} -C {remote_path}{no_ext}/')

            print(f"Removing uploaded archive...")
            c.run(f'rm /tmp/{file_n}')

            print(f"Moving contents...")
            c.run(f'mv {remote_path}{no_ext}/web_static/* {remote_path}{no_ext}/')

            print(f"Cleaning up extra folder...")
            c.run(f'rm -rf {remote_path}{no_ext}/web_static')

            print(f"Updating symbolic link...")
            c.run('rm -rf /data/web_static/current')
            c.run(f'ln -s {remote_path}{no_ext}/ /data/web_static/current')

            print(f"Deployment to {host} successful!")

        return True

    except UnexpectedExit as e:
        print(f"Command failed: {e.result.stderr}")
        return False

    except Exception as e:
        print(f"Deployment error: {e}")
        return False
