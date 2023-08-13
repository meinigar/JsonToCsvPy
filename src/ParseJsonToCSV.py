import json
import pandas


def read_json(filename: str) -> dict:
    print('Msg1: Inside read json method\n)
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
            print('Msg2: read the file')
    except:
        raise Exception(f'error reading file: {filename}\n')
    return data


def create_dataframe(data: list) -> pandas.DataFrame:
    print('Msg3: inside dataframe method\n'')
    dataframe = pandas.DataFrame()
    for d in data:
        record = pandas.json_normalize(d)
        dataframe = dataframe._append(record, ignore_index=False)
        #dataframe = dataframe.append(record, ignore_index=False)
        print('Msg4: inside loop data\n')
    return dataframe


def main():
    print('Msg01: Enter main\n')
    data = read_json(filename="../data/data.json")
    print('Msg02: main ln 2\n')
    dataframe = create_dataframe(data=data['employees'])
    print('Normalised Columns: ', dataframe.columns.to_list())
    dataframe.rename(columns={
        "results.school": "school",
        "results.high_school": "high_school",
        "results.graduation": "graduation",
        "education.graduation.major": "grad_major",
        "education.graduation.minor": "grad_minor"
    }, inplace=True)
    print("Renamed Columns:", dataframe.columns.to_list())
    dataframe.to_csv("../data/data.csv", index=False)
if __name__ == '__main__':
    main()