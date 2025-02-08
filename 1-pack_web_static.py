#!/usr/bin/python3
from fabric.api import local
from time import strftime


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