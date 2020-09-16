import json
import sys
from copy import deepcopy
from argparse import ArgumentParser

# TODO: Ord category's IDs after deletion


def return_cat_name(json_coco, category):
    """Return the category name of a category ID

    Arguments:
        json_coco {dict} -- json dict file from coco file
        category {int} -- category ID

    Returns:
        string -- category name
    Raises:
        KeyError: Category ID not found
    """
    for cat in json_coco['categories']:
        if cat['id'] == category:
            return cat['name']
    print("Categoria não encontrada: ", category)
    sys.exit()


def main():
    """Remove a category from a coco json file
    """
    parser = ArgumentParser(
        description='Category Filter: Filter a List of Categories from a JSON')
    parser.add_argument('json_file_path', help='JSON file path')
    parser.add_argument('out_file', help='Output filename')
    args = parser.parse_args()

    ann_file = open(args.json_file_path)
    category_names = ["sports ball", "cell phone", "couch", "elephant", "tie", "spoon", "skis", "apple", "giraffe", "laptop", "tennis racket", "sink", "dog", "fork", "cat", "teddy bear", "train", "skateboard", "toilet", "sandwich", "bed", "keyboard", "baseball glove", "baseball bat", "airplane", "oven", "hot dog", "refrigerator", "frisbee", "mouse", "fire hydrant", "stop sign", "bear", "snowboard", "parking meter", "toothbrush", "microwave", "scissors", "hair drier", "toaster"]

    json_coco = json.load(ann_file)
    new_json = deepcopy(json_coco)

    for ann in json_coco['annotations']:
        if return_cat_name(json_coco, ann['category_id']) in category_names:
            new_json['annotations'].remove(ann)

    for cat in json_coco['categories']:
        if cat['name'] in category_names:
            new_json['categories'].remove(cat)

    output = open(args.out_file, "w")
    json.dump(new_json, output)
    output.close()


if __name__ == "__main__":
    main()

