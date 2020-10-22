import sys
from utils import utils
import pandas as pd

from sqlalchemy import create_engine

from settings import ENGINE_STRING

engine = create_engine(ENGINE_STRING)


def recommend():
    courses_for_skills = get_courses_for_skills(
        find_skills_associated_to_missing_skills(
            find_missing_skills_from_curriculum()))
    # print(courses_for_skills)
    json_dict = utils.transform_courses_for_skills_API_form(courses_for_skills)
    return json_dict


def get_curriculum_coverage():
    skills_df = utils.read_skills()
    top_skills = find_top_skills(skills_df)
    missing_skills = find_missing_skills_from_top_skills(top_skills)

    return 1-len(missing_skills)/len(skills_df)


def get_courses_for_skills(relevant_skills_dict):
    query = """select cdc.course_title, cdc.id from curriculum_designer_skill
        inner join curriculum_designer_course_course_skills cdccs on curriculum_designer_skill.id = cdccs.skill_id
        inner join curriculum_designer_course cdc on cdc.id = cdccs.course_id
    where skill_type='computer/ data science' and lower(skill_label)='{}';"""

    courses_for_skill_dict = {}
    for key in relevant_skills_dict:
        all_courses_for_skill = {}
        for rs in relevant_skills_dict[key]:
            courses_for_skill = get_table(sql_command=query.format(rs))
            all_courses_for_skill[rs] = courses_for_skill.values.tolist()

        courses_for_skill_dict[key] = all_courses_for_skill

    scored_courses_for_skill_dict = add_score_for_courses(courses_for_skill_dict)
    for key in courses_for_skill_dict:
        if key in scored_courses_for_skill_dict:
            courses_for_skill_dict[key]['scored_courses'] = scored_courses_for_skill_dict[key]
        else:
            courses_for_skill_dict[key]['scored_courses'] = {}
    return courses_for_skill_dict


def add_score_for_courses(courses_for_skill_dict):
    courses_with_score = {}
    course_list_dict = {}
    for key in courses_for_skill_dict:
        course_list = []
        for key2 in courses_for_skill_dict[key]:
            course_list.extend(courses_for_skill_dict[key][key2])

        course_list_dict[key] = course_list
        if key in course_list_dict:
            courses_with_score[key] = find_score_for_courses(course_list_dict[key])
    return courses_with_score


def find_skills_associated_to_missing_skills(missing_skills):
    sorted_rules = utils.read_association_rules()
    skill_dict = {}
    skills_idx_dict = utils.read_skills_dict_from_json()
    for s in missing_skills.iterrows():
        skill = str(s[1]['column1'])

        skill_dict[skill] = []

        for r in sorted_rules.iterrows():
            antecedents = get_list_of_ints_from_string(r[1][0])
            consequents = get_list_of_ints_from_string(r[1][1])

            for c in consequents:
                if skill == skills_idx_dict[str(c)].lower():
                    skill_dict[skill].extend(antecedents)

    relevant_skills_dict = {}
    for key in skill_dict:
        skill_list = []
        for s in skill_dict[key]:
            skill_list.append(skills_idx_dict[str(s)].lower())

        relevant_skills_dict[key] = list(set(skill_list))
    return relevant_skills_dict


def find_score_for_courses(course_list):
    counter = find_hits_for_courses(course_list)
    max_hits = find_max_hits(counter)
    score_dict = {}
    if max_hits > 0:
        for key in counter:
            score_dict[key] = counter[key]/max_hits
    return score_dict


def find_hits_for_courses(course_list):
    counter = {}
    for c in course_list:
        if str(c) in counter:
            counter[str(c)] += 1
        else:
            counter[str(c)] = 1
    return counter


def find_max_hits(counter_dict):
    max_hits = 0
    for key in counter_dict:
        if counter_dict[key] > max_hits:
            max_hits = counter_dict[key]
    return max_hits


def find_missing_skills_from_curriculum():
    skills_df = utils.read_skills()
    top_skills = find_top_skills(skills_df)
    missing_skills = find_missing_skills_from_top_skills(top_skills)
    return missing_skills


def get_table(**kwargs):
    """
    This function is used to load the provided table as a Pandas DataFrame

    :param kwargs: provided kwargs
    :return: pandas DataFrame
    """
    if 'sql_command' in kwargs.keys():
        sql_command = kwargs['sql_command']
        table_df = pd.read_sql_query(sql_command, engine)
    elif 'table' in kwargs.keys():
        table = kwargs['table']
        table_df = pd.read_sql_table(table, engine)
    else:
        table_df = pd.DataFrame()
    return table_df


def find_top_skills(skills_df):
    skills_to_recommend = skills_df[skills_df['kind']!='topic']
    top30_skills = skills_to_recommend.sort_values('occurences', ascending=False).head(30)
    return top30_skills


def find_missing_skills_from_top_skills(top_skills):
    query = build_query(top_skills)
    missing_skills = get_table(sql_command=query)
    return missing_skills


def build_query(top_skills):
    top30_skill_names = list(top_skills['string'])
    top30_skill_names_lower = [s.lower() for s in top30_skill_names]
    strn = ""
    for s in top30_skill_names_lower:
        strn += '(\'' + str(s) + '\'),'
    strn = strn[:-1]
    query = """VALUES {}
            EXCEPT ALL
                SELECT lower(skill_label)
                FROM   curriculum_designer_skill 
                where skill_type='computer/ data science'""".format(strn)
    return query


def get_list_of_ints_from_string(strn):
    vals = strn[strn.index('{') + 1: strn.index('}')].split(',')
    int_vals = [int(v) for v in vals]
    return int_vals


# print(get_courses_for_skills(
#     find_skills_associated_to_missing_skills(
#         find_missing_skills_from_curriculum())))
