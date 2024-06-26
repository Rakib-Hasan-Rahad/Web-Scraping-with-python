import csv
from os.path import exists

from fb_scraper import get_profile

from constants import PROFILE_HEADER_NAMES

PROFILE_IDS = ['100089632299605', '100069502939023', 'mirjawakil', 'tanzim.taher']
COOKIES_NAME = ['nila.txt']
FILE_NAME = 'profiles.csv'

profile_count = 0
next_url = None

if not exists(f'files/{FILE_NAME}'):
    with open(f'files/{FILE_NAME}', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(PROFILE_HEADER_NAMES)


for profile_id in PROFILE_IDS:
    cookie_index = profile_count % len(COOKIES_NAME)
    print(f'Cookie Using: {COOKIES_NAME[cookie_index]}')

    data = get_profile(profile_id, f'cookies/{COOKIES_NAME[cookie_index]}')

    profile_count += 1
    print(f'Profile Scraped: {profile_count}')

    if data:
        profile_info = data

        copy_dict = {}

        for header in PROFILE_HEADER_NAMES:
            if header in list(profile_info.keys()):
                copy_dict[header] = profile_info[header]
            else:
                copy_dict[header] = profile_id if header == 'id' else None

        if exists(f'files/{FILE_NAME}'):
            with open(f'files/{FILE_NAME}', 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=copy_dict.keys())
                writer.writerow(copy_dict)
        else:
            with open(f'files/{FILE_NAME}', 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=copy_dict.keys())
                writer.writeheader()
                writer.writerow(copy_dict)
