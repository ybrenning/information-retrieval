import jsonlines

data = []

def concatStrings(line):
    string = ''
    for key,value in line.items():
        if key != 'id':
            if isinstance(value, list):
                for item in value:
                    string += item + ' '
            else:
                string += str(value) + ' '
    return string

with jsonlines.open('ir-anthology-07-11-2021-ss23.jsonl') as f:

    for line in f.iter():
        data.append({'doc_id': line['id'], 'text': concatStrings(line)})
print(data[0])

with jsonlines.open('output.jsonl', mode='w') as writer:
    for item in data:
        writer.write(item)
