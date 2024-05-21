#!/usr/bin/python


import os
import sys

from pathlib import Path
from pathlib import PurePath

POST_PATH='./'
# FONT_PATH='docker_fs/hexo-page/kksworks.github.io/source/NanumSquareL.ttf'

from PIL import Image, ImageDraw, ImageFont
 
def createImg(textData, width, height):
    fontSize = 40
 
    #img = Image.new("RGB", (width, height), color = (0, 0, 0))

    img = Image.open('./aaaaa.png')
    fnt = ImageFont.truetype(FONT_PATH, fontSize, encoding="UTF-8")
 
    # 텍스트가 시작될 X, Y 좌표
    textPosition01 = 10
    textPosition02 = 10
 
    d = ImageDraw.Draw(img)
    d.text((textPosition01,textPosition02), textData, font=fnt, fill=(255,255,255))
 
    img.save("파일명22.png")


def get_fileinfo_from_folder(path_folder, ext) :
    path = Path(path_folder)

    fileinfo_dic_arr = []

    for filename in path.glob('**/' + ext):

        findinfo_dic = {}

        findinfo_dic['file_name'] = str(PurePath(filename).stem)
        findinfo_dic['file_ext'] = str(PurePath(filename).suffix)
        findinfo_dic['file_full_name'] = findinfo_dic['file_name'] + findinfo_dic['file_ext'] 
        findinfo_dic['abpath_full'] = str(PurePath(str(Path(filename).resolve())))
        findinfo_dic['abpath_folder'] = str(PurePath(findinfo_dic['abpath_full']).parent)

        # filter skip files
        # if findinfo_dic['abpath_full'].find(mdtools.TEMP_MD_FILE_NAME) != -1:
        #     continue

        fileinfo_dic_arr.append(findinfo_dic)
    return fileinfo_dic_arr

def join_path(*args) :
	path = ''
	for arg in args :
		path = PurePath(path, arg)
	return str(path)

def is_file_exist(target_path) :
	return  Path(target_path).exists()

def generate_asset_link() :
	md_files_info = get_fileinfo_from_folder(POST_PATH, '*.md')
	for md_file in md_files_info :
		target_asset_folder = join_path(md_file['abpath_folder'], md_file['file_name']+'.assets')
		target_asset_folder_link = join_path(md_file['abpath_folder'], md_file['file_name'])
		if is_file_exist(target_asset_folder) == True and is_file_exist(target_asset_folder_link) == False : 
			os.chdir(md_file['abpath_folder'])
			os.symlink(md_file['file_name']+'.assets', md_file['file_name'])


if __name__ == '__main__':
	generate_asset_link()