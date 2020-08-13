from subprocess import call as run_command, check_call as try_to_run_command ,Popen as run_background_command, check_output, CalledProcessError, DEVNULL, PIPE
from distutils.dir_util import copy_tree as webpage_set
from time import sleep as wait
from os import path, system, chmod, stat, mkdir, remove, chdir, replace, getuid
from shutil import rmtree, copyfile
from pathlib import Path as pathlib_Path
from pyngrok import ngrok
import re as regular_expression
import getpass, base64, socket, requests
from platform import system as platform_os
import requests
