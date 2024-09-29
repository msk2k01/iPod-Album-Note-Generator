# iPod Album Note Maker
This short Python script uses the TinyTag package to create a text note summary of album information typically not visible on iPods with monochrome screens. The output text file can be viewed using the iPod's "Notes" feature. The script makes no changes or modifications to the tag field data it reads from the files.

Fields included in the output includes:
* [Artist](#artist-tag)
* Comment (FLAC) / Description (ALAC)
* Track number
* Total album length (in format hh:mm:ss)
* Year

# Usage
[Running this script requires Python.](https://www.freecodecamp.org/news/check-python-version-how-to-check-py-in-mac-windows-and-linux/)

Run `python /path/to/script/ipod-album-note-maker.py path/to/album/folder` from the terminal. The script will pick up on any FLAC or ALAC (extension .m4a) in the given folder.
The text file will be placed in your current working directory at the time you executed the script.

To see the note on your iPod:
1. Plug iPod into computer with [disk use enabled.](https://www.copytrans.net/support/how-to-use-the-ipod-as-a-storage-drive-enable-disk-use/)
2. From File Explorer, copy the text file into the iPod's `/Notes` folder.
3. Eject iPod.
4. If not already done, on iPod go to `Settings -> Main Menu` and set "Notes" to "On." This will add the "Notes" option to the iPod's main menu, where you can then open the text files.

### Output File Example
Note that the top "xml" line is not shown when viewing on iPod.
```
<?xml encoding="UTF8"?>
RANDOM ACCESS MEMORIES by DAFT PUNK
2013
01:14:37


1. Give Life Back To Music
Daft Punk ft. Nile Rodgers

2. The Game Of Love
Daft Punk

3. Giorgio By Moroder
Daft Punk ft. Giorgio Moroder

4. Within
Daft Punk ft. Chilly Gonzales

5. Instant Crush
Daft Punk ft. Julian Casablancas

6. Lose Yourself To Dance
Daft Punk ft. Pharrell Williams

7. Touch
Daft Punk ft. Paul Williams

8. Get Lucky
Daft Punk ft. Pharrell Williams; Nile Rodgers

9. Beyond
Daft Punk

10. Motherboard
Daft Punk

11. Fragments Of Time
Daft Punk ft. Todd Edwards

12. Doin' It Right
Daft Punk ft. Panda Bear

13. Contact
Daft Punk ft. DJ Falcon

```

# "Artist" Tag
Some iPod syncing tools like foobar2000 allow remapping tag fields during iPod sync; one use case for this is to transfer "Album Artist" to "Artist" for easier organization by artist on older iPods which don't read the "Album Artist" tag field. However, this renders the original "Artist" field inacessible -- unideal for cases where, for example, the artist tag lists featured artists.

This script writes the original "Arist" tag data into the text file, so it is visible on the iPod once again.

# References
* https://wiki.yuo.be/dop:start
* http://www.kenichimaehashi.com/ipodnotereader/ipodnotereader.pdf
* https://pypi.org/project/tinytag/
