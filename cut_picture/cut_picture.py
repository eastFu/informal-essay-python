#!/usr/bin/python
# coding=utf-8
# Create: 2018-09-04 09:25:15
# Author: eastFu
# Desc: 将一张图片填充为正方形后切为9张图

from PIL import Image
class CutPicture():

    # 将图片填充为正方形
    @staticmethod
    def fill_image(img):
        width, height = img.size
        # 选取长和宽中较大值作为新图片的
        new_image_length = width if width > height else height
        # 生成新图片[白底]
        new_image = Image.new(img.mode, (new_image_length, new_image_length), color='white')
        '''将之前的图粘贴在新图上，居中'''
        if width > height:
            # 原图宽大于高，则填充图片的竖直维度
            # (x,y)二元组表示粘贴上图相对下图的起始位置
            new_image.paste(img, (0, int((new_image_length - height) / 2)))
        else:
            new_image.paste(img, (int((new_image_length - width) / 2),0))
        return new_image

    # 切图
    @staticmethod
    def cut_image(img):
        width, height = img.size
        item_width = int(width / 3)
        box_list = []
        # (left, upper, right, lower)
        for i in range(0, 3):
            # 两重循环，生成9张图片基于原图的位置
            for j in range(0,3):
                box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
                box_list.append(box)
        return [img.crop(box) for box in box_list]

    # 保存
    @staticmethod
    def save_images(img, out_path):
        index = 1
        for image in img:
            out_name = out_path+'/cut-'+str(index) + '.png'
            image.save(out_name, 'PNG')
            print "save img : %s" % out_name
            index += 1

    @staticmethod
    def cut_and_save(img_path, out_path):
        print "start :  %s" % img_path
        img = CutPicture.fill_image(Image.open(img_path))
        img = CutPicture.cut_image(img)
        CutPicture.save_images(img, out_path)
        print "end : cut picture success"

if __name__ == '__main__':
    file_path = "e://cut/py.jpg"
    out_path = "e://cut/result"
    CutPicture.cut_and_save(file_path, out_path)
