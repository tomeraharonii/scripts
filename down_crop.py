import sys
import subprocess
import uuid

import csv


def main():
    link = None
    start_t = None
    segment_length = None
    boring_charismatic = None
    playlist = 'n'
    b_c = None
    remove_originals = False

    with open('input.csv', mode='r') as input_file:
        # employee_writer = csv.writer(
        #     employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        # employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
        # employee_writer.writerow(['Tomer Meyers', 'IT', 'March'])
        file_reader = csv.reader(input_file)
        next(file_reader)
        for row in file_reader:
            link, start_t, segment_length, boring_charismatic, playlist = str(
                row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])

        if len(sys.argv) > 1:
            if sys.argv[1] == 'y':
                remove_originals = True

        # need to add:
        # wav file name
        # video title
        # original file name
    # print("LINK: ")
    # print(link)

    # print("start_t: ")
    # print(start_t)
    # print("segment_length: ")
    # print(segment_length)
    # print("boring_charismatic: ")
    # print(boring_charismatic)
    # print("playlist: ")
    # print(playlist)

    # # get video link
    # if sys.argv[1]:
    #     link = sys.argv[1]
    # # get start time and end time
    # if sys.argv[2] and sys.argv[3]:
    #     start_t = sys.argv[2]
    #     length = sys.argv[3]
    # if len(sys.argv) > 4:
    #     remove = sys.argv[4].lower()

    # if len(sys.argv) > 5:
    #     playlist = sys.argv[5].lower()

    # if len(sys.argv > 6):
    #     b_c = sys.argv[7]

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
            strip_file_name, start_t, segment_length, unique_file)
        print(get_portion)
        subprocess.call(get_portion.split())
    except:
        print("error while croping video")
        exit(0)

    # Export data to csv:
    # [video_title, video_link, start_time, segment_length, wav_file_name, original_file_name, boring/charismatic, from_playlist]

    row = [strip_file_name, link, start_t, segment_length,
           strip_file_name + ".wav", boring_charismatic, playlist]
    with open('output.csv', mode='a') as outpuf_file:
        csv_write = csv.writer(
            outpuf_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(row)

    # remove uncropped wav segments(optional)
    if remove_originals:
        command = "rm -f {}.wav".format(strip_file_name)


if __name__ == '__main__':
    main()
