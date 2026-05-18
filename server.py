# entry
import os
import sys
import subprocess

s = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server", "server.py")
sys.exit(subprocess.call([sys.executable, s] + sys.argv[1:]))
