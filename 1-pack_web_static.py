#!/usr/bin/python3
"""scr_ipt that gen_erates a .tgz ar_chive from the cont_ents of the web_static
fol_der of your AirBnB Clone repo, using the func__tion do_pack.
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ gene__rates a .tgz arc_hive from the con_tents of the web_static

    All files in the folder web_static must be added to the final archive.
    All arc_hives must be sto_red in the folder versions.
    The name of the archive created must be:
        web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the arc_hive has
    been correctly gen_erated. Otherwise, it shou_ld return N_one.

    Returns:
        fabric.oper_ations._AttributeString: arch_ive path.
    """
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

if __name__ == "__main__":
    do_pack()
