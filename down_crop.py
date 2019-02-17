import sys
import subprocess
import uuid


def main():
    if len(sys.argv) < 2:
        print("please provide video link and at least start/end time")
        print("USAGE:")
        print("<video_link> start_time: <mm:ss> length: <ss> remove_files: <y/n> download_from_playlist: <y/n>")
        exit(0)
    # get video link
    if sys.argv[1]:
        link = sys.argv[1]
    # get start time and end time
    if sys.argv[2] and sys.argv[3]:
        start_t = sys.argv[2]
        end_t = sys.argv[3]
    if len(sys.argv) > 4:
        remove = sys.argv[4].lower()

    if len(sys.argv) > 5:
        playlist = sys.argv[5].lower()

    # get output file name
    if playlist == 'y':
        playlist_indicator = link.rfind('&list')
        link = link[:playlist_indicator]

    file_name = subprocess.Popen(['youtube-dl', '--restrict-filenames',
                                  '--get-filename', link], stdout=subprocess.PIPE).communicate()[0]

    # strip file name from encoding
    file_name = file_name.decode("utf-8")

    # remove file extension
    last_dot = file_name.rfind('.')
    strip_file_name = file_name[:last_dot]

    # download file as wav
    command = "youtube-dl --restrict-filenames --extract-audio --audio-format wav {}".format(
        link)
    subprocess.call(command.split())

    # get portion of video
    try:
        # create a unique file name
        unique_file = str(uuid.uuid4())
        get_portion = "ffmpeg -i {}.wav -ss 00:{}.00 -t 00:00:{}.00 -c copy ./clips/{}.wav".format(
            strip_file_name, str(start_t), str(end_t), unique_file)
        # print(get_portion)
        subprocess.call(get_portion.split())
    except:
        print("error while croping video")
        exit(0)

    # remove uncropped wav segments (optional)
    if remove == 'y':
        command = "rm -f {}.wav".format(strip_file_name)


if __name__ == '__main__':
    main()
