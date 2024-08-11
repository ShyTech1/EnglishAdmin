import csv
from models import Classes, Students


def csv_reader_handler():
    r = []
    FILE_PATH = "data_file.csv"

    with open(FILE_PATH) as file:
        file.readline()  # skip the first row with the header.
        csvreader = csv.reader(file)  # creates an iterable object that reads the file properly.
        for i in csvreader:
            r.append(i)

    classes_data = data_class_handler(r)
    students_data = student_data_handler(r)

    return students_data, classes_data


def data_class_handler(rows):
    class_data_rows = {}

    for i in rows:
        c = Classes(
            # class_num=class_num,
            class_num=i[3],
            sub_class=i[4],
            educator_name=i[5]
        )

        # c = Classes(**row_data)
        # key = row_data["class_num"]+row_data["sub_class"]+row_data["educator_name"]
        # #use a dictionary to overwrite duplication

        key = c.class_num + c.sub_class + c.educator_name
        class_data_rows[key] = c
    return class_data_rows.values()


def student_data_handler(rows):
    student_data_rows = []
    for i in rows:
        # Create a dictionary for each row and append it to the data list
        # It is a dict and not a class because it has to have the class_num and the educator name in it.
        # in the database.add_student() it will be handled to match the correct class uuid.

        s = {
            "id": i[0],
            "lname": i[1],
            "fname": i[2],
            "class_num": i[3],
            "sub_class": i[4],
            "educator_name": i[5],
            "module_1": i[7],
            "module_2": i[8],
            "literature": i[9],
            "oral": i[10]
        }
        student_data_rows.append(s)
    # print(student_data_rows)
    # {'id': '217669092', 'lname': 'בן שימול', 'fname': 'בנימין ציון', 'class_num': 'יא', 'sub_class': '1',
    # 'educator_name': 'יוסי כהן', 'module_1': 'D', 'module_2': 'C', 'literature': 'E', 'oral': '4'}
    return student_data_rows


if __name__ == "__main__":
    csv_reader_handler()
