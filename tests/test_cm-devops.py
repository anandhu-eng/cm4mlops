from __future__ import print_function

try:
    import cmind as cm

    r = cm.access({'action':'run', 'automation':'script', 'tags': 'python,src,install,_shared', 'version': '3.9.10'})
    if 'return' not in r:
        raise Exception('CM access function should always return key \'return\'!')
    
    r = cm.access({'action':'search', 'automation':'cache', 'tags': 'python,src,install,_shared', 'version': '3.9.10'})
    if 'return' not in r:
        raise Exception('CM access function should always return key \'return\'!')
    if len(r['list']) <= 1:
        raise Exception('CM search failed for the cached installation!')
    
    exit(0)

except ImportError as e:
    from sys import stderr
    from subprocess import call
    retcode = call(['cm', 'run', 'script', '--tags=python,src,install,_shared --version=3.9.10'])
    exit(retcode)
