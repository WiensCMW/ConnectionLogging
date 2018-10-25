import os
import subprocess
import datetime
import time

# list of addresses to use in the ping test
host_list = ["www.google.com", "www.yahoo.com"]

# log directory
log_dir = "/log testing"

# ping test function that suppresses the ping results output
# https://stackoverflow.com/questions/28769023/get-output-of-system-ping-without-printing-to-the-console
def pingtest(host_name):
    with open(os.devnull, 'w') as DEVNULL:
        try:
            subprocess.check_call(
                ['ping', '-c', '3', host_name],
                stdout=DEVNULL,  # suppress output
                stderr=DEVNULL
            )
            results = True
        except subprocess.CalledProcessError:
            results = False

    return results

while True:
    # loop through host list and perform ping test until one succeeds
    pingtest_passed = False

    # check if router is reachable and only continue if it is.
    if pingtest("192.168.1.1") is True:
        i = 0
        while i < len(host_list):
            if (pingtest(host_list[i])) is True:
                pingtest_passed = True
                break
            i += 1

        # handle failed ping
        if pingtest_passed is False:
            # log results to file
            with open(log_dir + "/ping_fail_log.txt", "a") as myfile:
                myfile.write(str(datetime.datetime.now()) + "\r\n")

        time.sleep(3)
