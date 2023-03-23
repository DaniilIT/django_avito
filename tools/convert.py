import csv
import json

PATH_LOC_CSV = './datasets/location.csv'
PATH_LOC_JSON = './datasets/location.json'
PATH_USER_CSV = './datasets/user.csv'
PATH_USER_JSON = './datasets/user.json'
PATH_USER_LOC_JSON = './datasets/user_location.json'
PATH_CAT_CSV = './datasets/category.csv'
PATH_CAT_JSON = './datasets/category.json'
PATH_AD_CSV = './datasets/ad.csv'
PATH_AD_JSON = './datasets/ad.json'



def convert_csv_to_json(model, path_csv_file, path_json_file):
    json_content = []
    with open(path_csv_file, encoding='utf-8') as csv_file:
        user_loc = []
        for row in csv.DictReader(csv_file):
            row_id = int(row.pop('id') if 'id' in row else row.pop('Id'))

            if 'lat' in row:
                row['lat'] = float(row['lat'])
            if 'lng' in row:
                row['lng'] = float(row['lng'])
            if 'age' in row:
                row['age'] = int(row['age'])
            if 'location_id' in row:
                location_id = int(row.pop('location_id'))
                user_loc.append({
                    'model': 'ads.User_Location',
                    'pk': row_id,
                    'fields': {'user_id': row_id, 'location_id': location_id}})
            if 'author_id' in row:
                row['author_id'] = int(row['author_id'])
            if 'price' in row:
                row['price'] = int(row['price'])
            if 'is_published' in row:
                row['is_published'] = True if row['is_published'] == 'TRUE' else False
            if 'category_id' in row:
                row['category_id'] = int(row['category_id'])

            json_content.append({'model': model, 'pk': row_id, 'fields': row})

    with open(path_json_file, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, indent=2, ensure_ascii=False)

    if user_loc:
        with open(PATH_USER_LOC_JSON, 'w', encoding='utf-8') as json_file:
            json.dump(user_loc, json_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    convert_csv_to_json('ads.Location', PATH_LOC_CSV, PATH_LOC_JSON)
    convert_csv_to_json('ads.User', PATH_USER_CSV, PATH_USER_JSON)
    convert_csv_to_json('ads.Category', PATH_CAT_CSV, PATH_CAT_JSON)
    convert_csv_to_json('ads.Ad', PATH_AD_CSV, PATH_AD_JSON)
