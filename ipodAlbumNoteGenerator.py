from tinytag import TinyTag
import os, math, sys, re

# get folder from command line. sanitize by removing trailing quote mark if needed
folder = os.path.normpath(sys.argv[1])
if folder[-1] == '"':
    print("Errant escaped quote character \" detected. Removing.")
    folder = folder[:-1]
    print("Folder path is now:", folder)

tracks = []
totalLength = 0
albumTitle = "NOT DEFINED"
overallArtist = "NOT DEFINED"
albumYear = "NOT DEFINED"

for filename in os.listdir(folder):
    if not (filename.endswith(".flac") or filename.endswith(".m4a")):
        continue

    path = folder + "\\" + filename
    tag = TinyTag.get(path)

    print("parsing file: " + path)

    # per-track tags
    entry = {
        "title": tag.title,
        "artist": tag.artist,
        "comment": tag.comment,
        "trackNumber": tag.track
    }
    tracks.append(entry)

    # tags that should be the same for each track
    albumTitle = tag.album
    overallArtist = tag.albumartist
    albumYear = tag.year

    totalLength += tag.duration

print("parsing complete") 

# sort tracks by track number
tracks = sorted(tracks, key=lambda d: int(d['trackNumber']))

# parsing album duration in seconds into hours and minutes
hrs = math.floor(totalLength/60/60)
mins = math.floor( (totalLength/60) - (hrs*60) )
secs = math.floor( (totalLength) - (hrs*60*60 + mins*60) )

# writing to text file
filename = re.sub('[^A-Za-z0-9]+', '', albumTitle) + (".txt") # .sub removes special characters from album name (like : and < )
print("writing to output: " + os.getcwd() + "\\" + filename)
with open(filename, "w", encoding="utf-8") as file:
    file.write("<?xml encoding=\"UTF8\"?>")
    file.write("\n")
    file.write(albumTitle.upper() + " by " + overallArtist.upper() + "\n")
    file.write(albumYear + "\n")
    file.write(str(hrs).zfill(2) + ":" + str(mins).zfill(2) + ":" + str(secs).zfill(2) + "\n"+ "\n") # zfill adds trailing zero to single digit values
    for i in tracks:
        # print(i)
        file.write("\n")
        file.write(i.get('trackNumber') + ". " + i.get('title') + "\n")
        file.write(i.get('artist') + "\n")

        if i.get('comment') != None: 
            file.write(i.get('comment') + "\n")
print("write complete")

# with terminal in same folder as script: foreach($i in (gci F:\media\music\  -Directory)){foreach($j in (gci $i.fullname -Directory )){python .\album-note-maker.py "$($j.fullname)"}}