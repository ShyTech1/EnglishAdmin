import csv
from models import Classes


def convert_class_num(s):
    if s == "ט":
        return '9'
    elif s == "י":
        return '10'
    elif s == "יא":
        return '11'
    elif s == "יב":
        return '12'
    else:
        return s


def csv_reader_handler():
    r = []
    FILE_PATH = "data_file.csv"

    with open(FILE_PATH) as file:
        file.readline()  # skip the first row with the header.
        csvreader = csv.reader(file)  # creates an iterable object that reads the file properly.
        for i in csvreader:
            r.append(i)

    classes_data = data_class_handler(r)
    # students_data = student_data_handler(r)

    return classes_data
    # return students_data, classes_data


def data_class_handler(rows):
    class_data_rows = {}

    for i in rows:
        # Create a dictionary for each row and append it to the data list
        # row_data = {
        #     "class_num": i[3],
        #     "sub_class": i[4],
        #     "educator_name": i[5]
        # }

        class_num = convert_class_num(i[3])

        c = Classes(
            class_num=class_num,
            sub_class=i[4],
            educator_name=i[5]
        )
        # c = Classes(**row_data)
        # key = row_data["class_num"]+row_data["sub_class"]+row_data["educator_name"] #use a dictionary to overwrite duplication

        key = c.class_num + c.sub_class + c.educator_name
        class_data_rows[key] = c
    return class_data_rows.values()


def student_data_handler(rows):
    student_data_rows = []
    for i in rows:
        class_num = convert_class_num(i[3])
        # Create a dictionary for each row and append it to the data list
        s = Students(
            id= i[0],
            lname= i[1],
            fname= i[2],
            module_1= i[7],
            module_2= i[8],
            literature= i[9],
            oral= i[10]
        )
        student_data_rows.append(row_data)
    return student_data_rows


if __name__ == "__main__":
    csv_reader_handler()
