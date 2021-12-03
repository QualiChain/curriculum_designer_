import json
import pandas as pd


def read_skills_ids_dict_from_json():
    with open('data/skills_ids_dict.json', 'r') as f:
        dct = json.load(f)
    return dct


skills_ids_dict = read_skills_ids_dict_from_json()


def read_skills_dict_from_json():
    with open('data/skills_idx_dict.json', 'r') as f:
        dct = json.load(f)
    return dct


def read_association_rules():
    return pd.read_csv("data/association_rules.csv", index_col=0)


def read_skills():
    return pd.read_csv('data/skills_with_occurences.csv')


def transform_courses_for_skills_API_form(courses_for_skills):
    recommended_skills = []
    for rec_skill in courses_for_skills:
        relevant_skills = []
        for rel_skill in courses_for_skills[rec_skill]:
            if rel_skill != 'scored_courses':
                related_courses = []
                for rel_course in courses_for_skills[rec_skill][rel_skill]:
                    if len(rel_course) >= 2:
                        course = {'course_title': rel_course[0], 'course_id': rel_course[1]}
                        related_courses.append(course)

                rel_courses = {'skill_title': rel_skill, 'related_courses': related_courses,
                               'skill_id': skills_ids_dict[rel_skill]}
                relevant_skills.append(rel_courses)
        scored_courses = courses_for_skills[rec_skill]['scored_courses']
        sc_courses = []
        for key in scored_courses:
            crs = eval(key)
            c = {'course_title': crs[0], 'course_id': crs[1], 'score': scored_courses[key]}
            sc_courses.append(c)
        rec_skill_dict = {'skill_title': rec_skill, 'relevant_skills': relevant_skills, 'scored_courses': sc_courses,
                          'skill_id': skills_ids_dict[rec_skill]}
        recommended_skills.append(rec_skill_dict)
    rec_skills_dict = {'recommended_skills': recommended_skills}
    return rec_skills_dict
