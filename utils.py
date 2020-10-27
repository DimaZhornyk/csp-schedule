import random

from model import Subject, Class, Classroom
from settings import subjects, teachers, sorted_classrooms


def schedule():
    return {"days": ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            "pairs": ["8:30-9:50", "10:00-11:20", "11:40-13:00", "13:30-14:50", "15:00-16:20", "16:30-17:50"]}


def set_up_variables():
    matrix = [[[] for time in schedule()["pairs"]] for day in schedule()["days"]]
    return matrix


def set_up_domains():
    classes = []
    for i in subjects:
        lector = list(filter(lambda t: i["name"] in t["lector"], teachers))
        practices_teachers = list(filter(lambda t: i["name"] in t["lector"] or i["name"] in t["practices"], teachers))
        classes.append(
            Class(Subject(lector[0]["name"], i["name"], i["students"], 0, i["groups"]), None))
        for j in range(i["groups"]):
            classes.append(Class(Subject(practices_teachers[random.randint(0, len(practices_teachers) - 1)]["name"],
                                         i["name"], i["students"] // i["groups"], j + 1, i["groups"]), None))
    return classes


def capacity_check(slot):
    classrooms = set()
    for c in slot:
        if c.subject.num_of_students > c.classroom.capacity:
            return False
        classrooms.add(c.classroom)
    return  len(classrooms) == len(slot)


def subject_collision_check(slot):
    classnames,cur_teachers = set(),set()
    for class_ in slot:
        classnames.add(class_.subject.name)
        cur_teachers.add(class_.subject.teacher)
    return len(slot) == len(classnames) and len(cur_teachers) == len(slot)


def groups_collision_check(slot):
    groups = set()
    for class_ in slot:
        groups.add(class_.subject.group)
    return len(groups) == len(slot)


def classroom_manager():
    classrooms = list(map(lambda c: Classroom(c[0], c[1]), sorted_classrooms))

    def get_minimum_essential_classroom(slot, capacity):
        nonlocal classrooms
        current_classrooms = list(map(lambda c: c.classroom.name, slot))
        for classroom in classrooms:
            if classroom.capacity >= capacity and classroom.name not in current_classrooms:
                return classroom
        return None

    return get_minimum_essential_classroom


def get_constraints():
    return [capacity_check, subject_collision_check, groups_collision_check]
