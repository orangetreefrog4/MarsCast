def prepModules() :
    print('Loading...')
    import os
    import sys
    from pathlib import Path

    listOfSrc = list(Path(os.path.realpath(sys.path[0])).glob('**/*.py'))
    
    for src in listOfSrc :
        print('Verbose: currently registering -', src)
        parent_dir = os.path.abspath(os.path.dirname(src))
        vendor_dir = os.path.join(parent_dir, 'vendor')
        sys.path.append(vendor_dir)
    
    import requests
    import urllib3
    import certifi
    import chardet
    import idna
    print('Done!')

prepModules()