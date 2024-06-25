from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] != 'windows':
        return {'return':1, 'error': 'Platforms other than windows is not supported in this script yet'}

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']
    print(env["CM_GCC_DOWNLOAD_URL"])

    return {'return':0}

def postprocess(i):
    env = i['env']

    print(f"GCC installed in path:{env["CM_GCC_BIN_WITH_PATH"]}")

    return {"return":0}