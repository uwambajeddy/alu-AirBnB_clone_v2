#!/usr/bin/python3
import re
from time import strftime
from fabric.context_managers import cd
from fabric.api import env, put, sudo, local
from os.path import join, exists, splitext

env.hosts = ["54.242.215.110", "34.229.154.33"]


def do_pack():
    """
    Generates a .tgz file from the contents of the web_static folder

    Returns:
        str: The file path of the generated .tgz file if successful else None.
    """

    date_time = strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date_time)
    try:
        local("mkdir -p versions")
        local("tar -zcvf {} web_static".format(file_name))
        return file_name
    except Exception as err:
        return None


def do_deploy(archive_path):
    """
    Deploy a compressed archive to a remote server.
    Args:
        archive_path (str): The path to the compressed archive.
    Returns:
        bool: True if the deployment is successful, False otherwise.
    """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = re.search(r'[^/]+$', archive_path).group(0)
        deploy_path = join("/data/web_static/releases/",
                           splitext(file_name)[0])
        sudo("mkdir -p {}".format(deploy_path))

        sudo("tar -xzf /tmp/{} -C {}".format(file_name, deploy_path))

        with cd(deploy_path):
            sudo("mv web_static/* .")
            sudo("rm -rf web_static")

        sudo("rm /tmp/{}".format(file_name))
        sudo("rm -rf /data/web_static/current")

        sudo('ln -sf {} /data/web_static/current'.format(deploy_path))
    except Exception as err:
        return False

    return True


def deploy():
    """
    Deploys the web_static content to the web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
