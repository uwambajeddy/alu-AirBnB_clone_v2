#!/usr/bin/python3

import os.path
from fabric.api import *
from fabric.operations import run, put
from datetime import datetime


env.hosts = ['172.29.16.1', '192.168.1.3']
env.user = "ubuntu"


def do_pack():
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # create folder versions if it doesn’t exist
    local("mkdir -p versions")

    # extract the contents of a tar archive
    result = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(now))
    if result.failed:
        return None
    else:
        return result


def do_deploy(archive_path):
    """distributes an archive to your web servers.

    Args:
        archive_path (string): path to archive

    Returns:
        Boolean: whether the archive is distributed or not
    """
    if not os.path.exists(archive_path):
        return False
    # Uncompress the archive to the folder,
    # /data/web_static/releases/<archive filename without extension>
    # on the web server
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(file_name))

        # Create new directory for release
        run("mkdir -p {}".format(folder_path))

        # Untar archive
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))

        # Delete the archive from the web server
        run("rm -rf /tmp/{}".format(file_name))

        # Move extraction to proper directory
        run("mv {}web_static/* {}".format(folder_path, folder_path))

        # Delete first copy of extraction after move
        run("rm -rf {}web_static".format(folder_path))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create new the symbolic link /data/web_static/current on web server,
        # linked to the new version of your code,
        # (/data/web_static/releases/<archive filename without extension>
        run("ln -s {} /data/web_static/current".format(folder_path))

        print('New version deployed!')
        success = True

    except Exception:
        success = False
        print("Could not deploy")
    return success
