from django.test import TestCase

# Create your tests here.
import jieba
import jieba.posseg as pseg #词性标注
import jieba.analyse as anls #关键词提取
seg_list = jieba.cut("红米，华为i,发烧友，999", cut_all=True)
print("【全模式】：" + "/ ".join(seg_list))  
