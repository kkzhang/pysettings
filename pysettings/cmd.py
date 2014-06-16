"""
Usage:
    pysettings init [<env_name>...] [--dir=<dir_name>] [--default=<def_env>]

"""

import os

from docopt import docopt

def main():
    opts = docopt(__doc__)
    print opts
    if opts["init"]:
        # Initialize settings template
        dir_name = (opts["--dir"] or "settings")
        if (not os.path.exists(dir_name)) or os.path.isdir(dir_name):

            envs = opts["<env_name>"] or ["development","production"]

            if (not os.path.exists(dir_name)):
                os.mkdir(dir_name)

            for e in envs:
                e_path =os.path.join(dir_name,e+".py")
                if os.path.exists(e_path):
                    raise Exception("File existed: {path}".format(path=e_path))
                else:
                    with open(e_path, "a+") as f:
                        f.write("""
from .settings import SettingsBase

class Settings(SettingsBase):
    pass
    """)
            with open(os.path.join(dir_name, "settings.py"), "a+") as f:
                default_envname = opts["--default"]
                if not default_envname:
                    default_envname = envs[0]

                f.write("""
import importlib
default_env = "{default_envname}"

class SettingsBase:
    pass

settings = importlib.import_module('..'+default_env, __name__).Settings
    """.format(default_envname=default_envname))

            with open(os.path.join(dir_name, "__init__.py"), "a+") as f:
                f.write("from .settings import settings")



        else:
            raise Exception("A file named {fn} exists, change another directory name".format(fn=dir_name))
