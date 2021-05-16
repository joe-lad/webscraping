try:
    import conda.cli.python_api as Conda
    import sys
    import subprocess
except:
    try:
        import os
    except:
        subprocess.run('python3 -m pip pillow install os sys conda')
    os.system('python3 -m pip install conda sysctl')