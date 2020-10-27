import prettytable
from utils import schedule


def print_pretty_matrix(matrix):
    col_labels = ['slot/day', 'Mon', 'Tu', 'Wed', 'Thur', 'Fri']
    table_vals = [[schedule()["pairs"][i], '', '', '', '', ''] for i in range(6)]

    table = prettytable.PrettyTable(col_labels, hrules=prettytable.ALL)

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):
            text = ''
            teachers = set()
            for c in matrix[i][j]:
                teachers.add(c.subject.teacher)
                text += '[subject: {}; tutor: {}; room: {}]\n'.format(c.subject.__repr__(), c.subject.teacher, c.classroom)
            table_vals[j][i + 1] = text
            if len(teachers) < len(matrix[i][j]):
                print("error")

    for row in table_vals:
        table.add_row(row)

    print(table)
