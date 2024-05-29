from color_matcher import ColorMatcher
from color_matcher.io_handler import load_img_file, save_img_file, FILE_EXTS
from color_matcher.normalizer import Normalizer
import os

img_ref = load_img_file('blur-input/normal n.png')

src_path = 'color-input'
filenames = [os.path.join(src_path, f) for f in os.listdir(src_path)
                     if f.lower().endswith(FILE_EXTS)]

cm = ColorMatcher()
for i, fname in enumerate(filenames):
    img_src = load_img_file(fname)
    img_res = cm.transfer(src=img_src, ref=img_ref, method='mkl')
    img_res = Normalizer(img_res).uint8_norm()
    save_img_file(img_res, os.path.join(os.path.dirname(fname), str(i)+'.png'))