#!/usr/bin/python3
import json
import os
import shutil
import sys
import time

def main(config_file="/etc/ogkeeper/config.json"):
    with open(config_file, 'r') as f:
        content = ''.join(f.readlines())

    config = json.loads(content)

    time.sleep(int(config["countdownInMinutesNotFloatingpoint"])*60)

    for i in config["keeping"]:
        with open(i["og"], 'rb') as fsrc, open(i["newfile"], 'wb+') as fdst:
            fdst.truncate()
            shutil.copyfileobj(fsrc, fdst)
    os.system(str(config["serviceRestartCmd"]))

if __name__ == '__main__':
    assert len(sys.argv) > 1
    main(sys.argv[1])
