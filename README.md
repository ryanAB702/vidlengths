# vidlengths

This script traverses a given directory tree and outputs a csv file containing a table of all the
.mp4 files and their lengths in seconds.

## usage

```
$: python vidlengths root_dir output.csv [-nomov] [-nomp4]
```

The -nomov and -nomp4 flags are optional. If passed to the script, they tell it to either ignore mov files or ignore mp4 files. If you pass both, it won't find any files whatsoever.

The /data directory has nested .mp4 files that you can test the script with.

For example:

```
$: python vidlengths data output_test.csv -nomov
```

## dependencies

The script depends on an FFmpeg binary (ffprobe) to decode the .mp4 metadata. Prebuilt binaries can be found
[here](https://www.ffmpeg.org/download.html) in the "Get the packages" section. For Macs, select "Static builds for OS X Intel 64-bit"
and then scroll down to the link for ffprobe. After extracting the download, place the binary somewhere in your $PATH, like /usr/local/bin

The script also depends on a python wrapper for ffprobe which has been included in this repository called ffprobe.py. The original source of this script is [here](https://github.com/simonh10/ffprobe)
