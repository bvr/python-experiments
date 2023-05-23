
import subprocess

def main():
    for file in files():
        convert(file, quality=9)

def convert(file, quality):
    """Convert m4a file downloaded from youtube to classic mp3 using specified quality."""
    file_mp3 = file.replace('.m4a', '.mp3')

    # for ffmpeg options see https://ffmpeg.org/ffmpeg.html
    cmd = [
        'ffmpeg', 
        '-y',                   # overwrite output file 
        '-i', file,             # input file
        '-c:v', 'copy',         # video codec
        '-c:a', 'libmp3lame',   # audio codec
        '-q:a', str(quality),   # audio quality 0=best, 9=worst
        file_mp3                # output file
    ]
    print(' '.join(cmd))
    subprocess.run(cmd)

def files():
    """Return list of .m4a files to convert."""
    return [
        # 'minecraft-be-together.m4a',
        # 'minecraft-doomsday.m4a',
        # 'minecraft-frame-of-mind.m4a',
        # 'minecraft-chains.m4a',
        # 'minecraft-star-glide.m4a',
        # 'minecraft-storm.m4a',
        # 'minecraft-thalleous.m4a',

        # 'gilanuv-pribeh.m4a',
        # 'smrt-hrdiny.m4a',

        'barva-kouzel.m4a'
    ]

if __name__=="__main__":
    main()
