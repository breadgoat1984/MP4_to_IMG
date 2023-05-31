Breadgoat - Breadgoat.com

This Python script is just a simple script that uses opencv to read
a local video file and then output images(screenshots) of every 30 frames.
It only keeps a new screen shot if the current image is different
from the previous one by a value of '5'.
this value can be changed in the script, there is a comment stating where.

the value is not arbitrary but would need to be adjusted to suit
your usage.
the higher the value the more difference that has to be
for the file to left in the folder and viceversa.

you can also change the extension jpg to png for higher quality.
jpg resolution of output file from a 720p video are 1034x720.

The .data/test.jpg file is there just for the initial frame comparison
instead of figuring out how to skip it, i just made it work with a throwaway file.

Version 1 - may 2023 creates every 30th frame and if the difference between this file and
the previous one is lower than 5 it deletes the file, if the difference is higher than 5 it keeps the file.
