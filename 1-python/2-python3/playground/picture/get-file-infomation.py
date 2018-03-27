#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from playground.statistic.utils.file.attributes import FileAttributes
from ffmpy import FFmpeg


class FileAttribute:
    def __init__(self, file_path):
        self.path = file_path

    def sense_file_type(self):
        return 'jpg'

    def obtain_file_attribute(self):
        pass

    def case_jpg(self):
        pass

    def case_png(self):
        pass

    def case_mp3(self):
        pass

    def numbers_to_functions_to_strings(self):
        argument = self.sense_file_type()
        switcher = {
            0: self.case_jpg,
            1: self.case_png,
        }
        method_name = 'case_' + str(argument)
        # Get the function from switcher dictionary
        func = switcher.get(method_name, lambda: "nothing")
        # Execute the function
        return func()


if __name__ == '__main__':
    attributes = FileAttributes(
        '/home/archermind/archermind/projects/Hawaii/u36/1-培训资料/2017_OOBE_Training_Video/2017_OOBE_Training_Video'
        '/UIBC/2017_11_28_14_03_19_701.mp4')
    print(attributes.get_ctime())

    # ff = FFmpeg(
    #     inputs={
    #         '/home/archermind/archermind/projects/Hawaii/u36/1-培训资料/2017_OOBE_Training_Video/2017_OOBE_Training_Video'
    #         '/UIBC/2017_11_28_14_03_19_701.mp4': None},
    #     outputs={'fate.m3u8': '-c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 -hls_time 2'}
    # )
    # print(ff.cmd)
    ## ffmpeg -i fate.mkv -c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 -hls_time 2 fate.m3u8
    # ff.run()
