import six
import subprocess

def Settings( **kwargs ):
    return {
        'interpreter_path': (subprocess.check_output(['which', 'python3'])).decode('utf8').strip()
    }

