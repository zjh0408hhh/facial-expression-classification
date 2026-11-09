# 以独立脚本启动训练，便于为每张 GPU 启动单独的训练进程。
import os
import signal
import subprocess
import sys

process = subprocess.Popen(
    [sys.executable, '-u', '/kaggle/working/fer_v3_accuracy.py'],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    text=True, bufsize=1, start_new_session=True,
)
try:
    for line in process.stdout:
        print(line, end='', flush=True)
    return_code = process.wait()
    if return_code:
        raise RuntimeError(f'Training exited with code {return_code}; inspect the log above.')
except BaseException:
    if process.poll() is None:
        os.killpg(process.pid, signal.SIGTERM)
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
    raise
