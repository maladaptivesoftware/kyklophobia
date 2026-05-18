# entry
import os
import sys
import subprocess

l = os.path.join(os.path.dirname(os.path.abspath(__file__)), "client", "launch.py")
sys.exit(subprocess.call([sys.executable, l] + sys.argv[1:]))
