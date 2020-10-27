classrooms = [[101, 10], [102, 60], [103, 30], [104, 80], [105, 40], [201, 80], [202, 40], [203, 30],
              [204, 10], [205, 60], [206, 60], [207, 40], [301, 10], [302, 80], [303, 10], [304, 10], [305, 60]]


subjects = [
    {"name": "Differential equations", "students": 60, "groups": 2},
    {"name": "Math economics", "students": 60, "groups": 3},
    {"name": "Discrete math", "students": 60, "groups": 4},
    {"name": "Mathematical analysis", "students": 60, "groups": 3},
    {"name": "Computer networks", "students": 60, "groups": 6},
    {"name": "Electronics", "students": 60, "groups": 2},
    {"name": "Computer networks L2", "students": 60, "groups": 6},
    {"name": "OKA", "students": 60, "groups": 4},
    {"name": "Procedural programming", "students": 60, "groups": 4},
    {"name": "OOP", "students": 60, "groups": 6},
    {"name": "OOP L2", "students": 60, "groups": 12},
    {"name": "Java 1.1", "students": 60, "groups": 6},
    {"name": "Java 1.2", "students": 60, "groups": 8},
    {"name": "MMIP", "students": 60, "groups": 6},
    {"name": "InfoSearch", "students": 60, "groups": 2},
    {"name": "ISWA", "students": 20, "groups": 3},
    {"name": "IOS", "students": 20, "groups": 4},
    {"name": "Basics of AI", "students": 60, "groups": 6}
]

teachers = [
    {"name": "Drin S S", "lector": ["Differential equations", "Math economics"], "practices": []},
    {"name": "Kriukova G V", "lector": ["Discrete math"], "practices": []},
    {"name": "Mytnyk Y V", "lector": ["Mathematical analysis"], "practices": ["Differential equations"]},
    {"name": "Vozniuck Y I", "lector": ["Computer networks", "Electronics", "Computer networks L2"],
     "practices": ["OKA"]},
    {"name": "Boublyk V V", "lector": ["Procedural programming", "OOP", "OOP L2"], "practices": []},
    {"name": "Pechkurova O M", "lector": ["MMIP"], "practices": ["Java 1.1", "Java 1.2", "MMIP"]},
    {"name": "Glybovets A M", "lector": ["Java 1.1", "Java 1.2", "OKA", "InfoSearch"], "practices": []},
    {"name": "Trosha B", "lector": ["ISWA"], "practices": ["InfoSearch"]},
    {"name": "Frankiv O O", "lector": ["IOS", "Basics of AI"], "practices": []},
]

sorted_classrooms = sorted(classrooms, key=lambda x: x[1])
