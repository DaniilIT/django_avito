import csv
import json

PATH_ADC_CSV = './datasets/ads.csv'
PATH_ADC_JSON = './datasets/ads.json'
PATH_CAT_CSV = './datasets/categories.csv'
PATH_CAT_JSON = './datasets/categories.json'


def covert_csv_to_json(model, path_csv_file, path_json_file):
    json_content = []
    with open(path_csv_file, encoding='utf-8') as csv_file:
        for row in csv.DictReader(csv_file):
            row_id = row.pop('Id') if 'Id' in row else row.pop('id')
            row_id = int(row_id)

            if 'is_published' in row:
                row['is_published'] = True if row['is_published'] == 'TRUE' else False
            if 'price' in row:
                row['price'] = int(row['price'])

            json_content.append({'model': model, 'pk': row_id, 'fields': row})

    with open(path_json_file, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    covert_csv_to_json('ads.Ads', PATH_ADC_CSV, PATH_ADC_JSON)
    covert_csv_to_json('ads.Category', PATH_CAT_CSV, PATH_CAT_JSON)
