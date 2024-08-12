import sys
import os
import subprocess
from huggingface_hub import snapshot_download

from folder_paths import models_dir

CUSTOM_NODES_PATH = os.path.dirname(os.path.abspath(__file__))
WEIGHTS_PATH = os.path.join(models_dir, "IDM-VTON")
HF_REPO_ID = "yisol/IDM-VTON"

if os.path.exists('/stable-diffusion-cache/models/IDM-VTON'):
    WEIGHTS_PATH = '/stable-diffusion-cache/models/IDM-VTON'


def build_pip_install_cmds(args):
    if "python_embeded" in sys.executable or "python_embedded" in sys.executable:
        return [sys.executable, '-s', '-m', 'pip', 'install'] + args
    else:
        return [sys.executable, '-m', 'pip', 'install'] + args

def ensure_package():
    cmds = build_pip_install_cmds(['-r', 'requirements.txt'])
    subprocess.run(cmds, cwd=CUSTOM_NODES_PATH)


if __name__ == "__main__":
    ensure_package()
<<<<<<< HEAD
    if not os.path.exists('/stable-diffusion-cache/models/IDM-VTON'):
        snapshot_download(repo_id=HF_REPO_ID, local_dir=WEIGHTS_PATH)
=======
    snapshot_download(repo_id=HF_REPO_ID, local_dir=WEIGHTS_PATH, local_dir_use_symlinks=False)
>>>>>>> ori/main
