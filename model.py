class Class:

    def __init__(self, subject, classroom):
        self.subject = subject
        self.classroom = classroom
        self.time = None

    def __str__(self):
        return f"{self.subject.__repr__()}"

    def __repr__(self):
        return str(self)


class Classroom:

    def __init__(self, name, capacity, busy=False):
        self.name = name
        self.capacity = capacity
        self.busy = busy

    def __str__(self):
        return "{} - {}".format(self.name, self.capacity)

    def __repr__(self):
        return str(self)


class Subject:

    def __init__(self, teacher, name, num_of_students, group, total_groups):
        self.teacher = teacher
        self.name = name
        self.num_of_students = num_of_students
        self.group = group
        self.total_groups = total_groups

    def __repr__(self):
        return self.name + " - lecture" if self.group == 0 else self.name + f" group - {self.group}"
