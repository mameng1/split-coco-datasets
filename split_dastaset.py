from pycocotools.coco import COCO
from pycocotools import mask as cocomask
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import random
import os
from pycococreatortools import pycococreatortools as pt
import json
import random
root_dir='/home/mameng/dataset/mapping_challenge/train'

INFO = {
    "description": "Example Dataset",
    "url": "https://github.com/waspinator/pycococreator",
    "version": "0.1.0",
    "year": 2018,
    "contributor": "waspinator",
}

LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License",
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
    }
]

CATEGORIES = [
    {
        'id': 1,
        'name': 'square',
        'supercategory': 'shape',
    },
    {
        'id': 2,
        'name': 'circle',
        'supercategory': 'shape',
    },
    {
        'id': 3,
        'name': 'triangle',
        'supercategory': 'shape',
    },
]
coco_output = {
        "info": INFO,
        "licenses": LICENSES,
        "categories": CATEGORIES,
        "images": [],
        "annotations": []
    }
annotation_root_path='/home/mameng/dataset/mapping_challenge/val'
annotation_name=os.path.join(annotation_root_path,"annotation-small.json")
coco=COCO(annotation_name)
catogry_info=coco.loadCats(coco.getCatIds())
coco_output['categories']=catogry_info
image_ids = coco.getImgIds(catIds=coco.getCatIds())
image_ids=random.sample(image_ids,500)
for image_id in image_ids:
    image_info = coco.loadImgs(image_id)[0]
    coco_output["images"].append(image_info)
    annotation_ids = coco.getAnnIds(imgIds=image_id)
    for annotation_id in annotation_ids:
        annotation_info = coco.loadAnns(annotation_id)[0]
        coco_output["annotations"].append(annotation_info)

with open('{}/annotation-little.json'.format(annotation_root_path), 'w') as output_json_file:
    json.dump(coco_output, output_json_file)

