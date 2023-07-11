# obj,parent,obj_type,size
import csv
import json
import pickle
from os import walk, path


def walk_dir(addr):
    tree = list(walk(addr))
    tree.reverse()

    results = []

    for obj in tree:
        address, folders, files = obj
        *_, parent, name = address.split('/')

        total_size = 0
        for fold in folders:
            for result in results:
                if result["obj"] == fold:
                    total_size += result["size"]

        for f in files:
            size = path.getsize(address + "/" + f)
            total_size += size
            file = {
                "obj": f,
                "parent": name,
                "obj_type": "file",
                "size": size
            }
            results.append(file)

        folder = {
            "obj": name,
            "parent": parent,
            "obj_type": "dir",
            "size": total_size
        }
        results.append(folder)

    with (open('results.csv', 'w') as csv_file,
          open('results.json', 'w') as json_file,
          open('results.pickle', 'wb') as pickle_file):
        csv_write = csv.DictWriter(csv_file, fieldnames=list(results[0].keys()))
        csv_write.writeheader()
        for row in results:
            csv_write.writerow(row)

        json.dump(results, json_file)

        pickle.dump(results, pickle_file)


walk_dir("/Users/andrejlebedev/Documents/Geekbrains/Python_Deep_HomeWork/HW8/dir1")
