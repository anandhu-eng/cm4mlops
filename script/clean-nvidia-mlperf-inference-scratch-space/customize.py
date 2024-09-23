from cmind import utils
import os
import cmind as cm

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    clean_cmd = ''
    cache_rm_tags = ''

    if env.get('CM_MODEL', '') == 'sdxl':
        if env.get('CM_CLEAN_ARTIFACT_NAME', '') == 'downloaded_data':
            clean_cmd = f"""rm -rf {os.path.join(env['CM_NVIDIA_MLPERF_SCRATCH_PATH'], "data", "coco", "SDXL")} """
            cache_rm_tags  = "nvidia-harness,_preprocessed_data,_sdxl"
        if env.get('CM_CLEAN_ARTIFACT_NAME', '') == 'preprocessed_data':
            clean_cmd = f"""rm -rf {os.path.join(env['CM_NVIDIA_MLPERF_SCRATCH_PATH'], "preprocessed_data", "coco2014-tokenized-sdxl")} """
            cache_rm_tags  = "nvidia-harness,_preprocessed_data,_sdxl"

    if clean_cmd != '':
        env['CM_RUN_CMD'] = clean_cmd

    if cache_rm_tags:
        r = cm.access({'action': 'rm', 'automation': 'cache', 'tags': cache_rm_tags})
        if r['return'] != 0 and r['return'] != 16: ## ignore missing ones
            return r

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
