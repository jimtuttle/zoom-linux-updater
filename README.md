# Update Linux Zoom client

Compares versions between locally-installed Zoom client and latest online version and attempts to download and install the latest version if it's not already installed.  

I added a job to root's crontab to run 5 after each hour between 7AM and 3PM:

$ sudo crontab -e

```
# m h  dom mon dow   command

# Zoom client updates
5 7-15 * * * python /path/to/zoom-linux-updater.py
```

 Althought Zoom specifies several distributions, there are only two packages.  The URLs for those are:
 
* Mint, Ubuntu, and Debian:  https://zoom.us/client/latest/zoom_amd64.deb
* Oracle, CentOS, and Redhate: https://zoom.us/client/latest/zoom_x86_64.rpm

Notes:
* I've only tested this on Debian.
* It's running as root.  No warranty expressed or implied.
* Debian doesn't provide a python binary in the standard path.  If you get an error about python not found, change the crontab line to python3 or install [python-is-python3](https://packages.debian.org/forky/python-is-python3).
