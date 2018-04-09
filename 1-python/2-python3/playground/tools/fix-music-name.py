#!/etc/bin/env python3
# -*- coding:utf-8 -*-
import os


def ModifyMp3FileInfo(filename):
    mp3Id3V1 = {
        "tag": {"valuepos": (0, 3), "value": ""},
        "SongName": {"valuepos": (3, 33), "value": ""},
        "SongPeople": {"valuepos": (33, 63), "value": ""},
        "Zj": {"valuepos": (63, 93), "value": ""},
        "Year": {"valuepos": (93, 97), "value": ""},
        "Bak": {"valuepos": (97, 125), "value": ""}
    }
    try:
        f = open(filename, 'rb')
        f.seek(-128, 2)
        sdata = f.read(3)
        if sdata == b'TAG':
            f.seek(-128, 2)
            sdata = f.read(128)
            for tag, subitem in mp3Id3V1.items():
                subitem["value"] = sdata[subitem["valuepos"][0]:subitem["valuepos"][1]].replace('/00', '').strip()
                print
                '%s=' % tag, '%s' % subitem["value"], '/n'
            f.close()
            import os
            if mp3Id3V1["SongName"]["value"] != '':
                test = [os.path.dirname(filename), '//']
                test.append(mp3Id3V1["SongName"]["value"])
                test.append('.mp3')
                newfilename = ''.join(test)
                print
                newfilename
                if os.path.exists(newfilename):
                    test = ['Filename ', newfilename, ' Has Existed']
                    print
                    ''.join(test)
                else:
                    try:
                        os.rename(filename, newfilename)
                    except Exception as e:
                        if e.winerror:
                            print
                            'Modify filename failed ,maybe the file is inuse'
                        else:
                            print
                            'UnKnown error'
        else:
            print
            'Is not a MP3 file'
    except IOError:
        print
        'Open file failed'


if __name__ == '__main__':
    music_dir = '/home/alex/music/KuGou'
    results = os.walk(music_dir)
    for root, dirc, filename in results:
        # print(">>>>>>>>>root>>>>>>>>>>", root, ">>>>>>>>>dirc>>>>>>>>>>", dirc, ">>>>>>>>>filename>>>>>>>>>>",
        #       filename, "\n\n")
        for name in filename:
            p = os.path.join(root, name)
            try:
                ModifyMp3FileInfo(p)
            except:
                print("except:", p)
    print("-----------------ok-----------------")
