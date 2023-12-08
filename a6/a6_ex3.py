import os

def merge_csv_files(*paths, delimiter=';', only_shared_columns=False):
    data = []
    all_headers = []
    for path in paths:
        with open(path) as f:
            lines = f.read().splitlines()
            header = lines[0].split(delimiter)
            all_headers.append(header)
            dict_data = [dict(zip(header, row.split(delimiter))) for row in lines[1:]]
            for entry in dict_data:
                data.append(entry)

    merged_headers = []
    if only_shared_columns:
        merged_headers = set(all_headers[0])

        for lst in all_headers[1:]:
            merged_headers = merged_headers.intersection(lst)

        merged_headers = list(merged_headers)
    else:
        merged_headers = list(set([header for sublist in all_headers for header in sublist]))
    
    with open(r'a6/merged.csv', 'w') as f:
        print(delimiter.join(merged_headers), file=f)
        for entry in data:
            line = delimiter.join(entry.get(header, 'NaN') for header in merged_headers)
            print(line, file=f)
            
    
    
#merge_csv_files(r'a6\Examples\ex3_1.csv', r'a6\Examples\ex3_2.csv', r'a6\Examples\ex3_3.csv', only_shared_columns = False)
#merge_csv_files(r'a6\Examples\ex3_1.csv', r'a6\Examples\ex3_2.csv', r'a6\Examples\ex3_3.csv', only_shared_columns = True)
