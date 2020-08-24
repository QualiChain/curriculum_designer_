# Qualichain Curriculum Designer


The QualiChain Curriculum Designer finds the skills in demand by the job market that are missing from a curriculum uses association rule mining to find related skills and recommends skills to be introduced to certain courses.
An offline process is executed to find association rules which can be found to the notebook association_rules_for_curriculum_designer.ipynb.
The online part uses as input the association rules and the top skills of the job market and provides a json with the results.

Application can be accessed from the port `8080`.

## Docker Installation

Standalone Installation: 
`docker-compose -f docker-compose.dev.yml up -d --build`

Installation according to QualiChain Network Specifications:
`docker-compose up -d --build`

## Local Installation

1. Install Requirements: `pip install -r requirements.txt`
2. Go to app/views folder using the command: `cd app/views`
3. Execute the command: `python -m flask run`

## MCDSS API example

### Input
POST request to:
'http://127.0.0.1:6060/curriculum_recommendation'

### Output
```json
{
    "recommended_skills": [
        {
            "relevant_skills": [],
            "skill_title": "windows"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "git"
                }
            ],
            "skill_title": "docker"
        },
        {
            "relevant_skills": [],
            "skill_title": "r"
        },
        {
            "relevant_skills": [],
            "skill_title": "scripting"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "html5"
                }
            ],
            "skill_title": "css3"
        },
        {
            "relevant_skills": [],
            "skill_title": "api"
        },
        {
            "relevant_skills": [],
            "skill_title": "react"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "javascript"
                },
                {
                    "related_courses": [],
                    "skill_title": "html5"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 31,
                            "course_title": "Databases"
                        },
                        {
                            "course_id": 39,
                            "course_title": "Internet Programming"
                        }
                    ],
                    "skill_title": "html"
                }
            ],
            "skill_title": "css"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "rest"
                },
                {
                    "related_courses": [],
                    "skill_title": "git"
                }
            ],
            "skill_title": "json"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "css"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 18,
                            "course_title": "Multimedia Technology"
                        },
                        {
                            "course_id": 21,
                            "course_title": "Computer System Performance"
                        },
                        {
                            "course_id": 25,
                            "course_title": "Distributed Systems"
                        },
                        {
                            "course_id": 32,
                            "course_title": "Programming Languages I"
                        },
                        {
                            "course_id": 35,
                            "course_title": "Software Engineering"
                        },
                        {
                            "course_id": 37,
                            "course_title": "Compilers"
                        },
                        {
                            "course_id": 39,
                            "course_title": "Internet Programming"
                        },
                        {
                            "course_id": 44,
                            "course_title": "Programming Languages II"
                        }
                    ],
                    "skill_title": "java"
                },
                {
                    "related_courses": [],
                    "skill_title": "jenkins"
                },
                {
                    "related_courses": [],
                    "skill_title": "rest"
                },
                {
                    "related_courses": [],
                    "skill_title": "json"
                },
                {
                    "related_courses": [],
                    "skill_title": "html5"
                },
                {
                    "related_courses": [],
                    "skill_title": "javascript"
                },
                {
                    "related_courses": [],
                    "skill_title": "docker"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 41,
                            "course_title": "Advanced Topics in Database Systems"
                        }
                    ],
                    "skill_title": "nosql"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 25,
                            "course_title": "Distributed Systems"
                        },
                        {
                            "course_id": 44,
                            "course_title": "Programming Languages II"
                        },
                        {
                            "course_id": 46,
                            "course_title": "Digital Communications I"
                        }
                    ],
                    "skill_title": "python"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 15,
                            "course_title": "Operating Systems"
                        },
                        {
                            "course_id": 19,
                            "course_title": "Operating Systems Laboratory"
                        },
                        {
                            "course_id": 32,
                            "course_title": "Programming Languages I"
                        },
                        {
                            "course_id": 33,
                            "course_title": "Algorithms and Complexity"
                        },
                        {
                            "course_id": 34,
                            "course_title": "Artificial Intelligence"
                        },
                        {
                            "course_id": 37,
                            "course_title": "Compilers"
                        }
                    ],
                    "skill_title": "c"
                }
            ],
            "skill_title": "git"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "ios"
                }
            ],
            "skill_title": "android"
        },
        {
            "relevant_skills": [],
            "skill_title": "angular"
        },
        {
            "relevant_skills": [],
            "skill_title": "tcp"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "json"
                },
                {
                    "related_courses": [],
                    "skill_title": "git"
                },
                {
                    "related_courses": [],
                    "skill_title": "javascript"
                }
            ],
            "skill_title": "rest"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "android"
                }
            ],
            "skill_title": "ios"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "css"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 18,
                            "course_title": "Multimedia Technology"
                        },
                        {
                            "course_id": 21,
                            "course_title": "Computer System Performance"
                        },
                        {
                            "course_id": 25,
                            "course_title": "Distributed Systems"
                        },
                        {
                            "course_id": 32,
                            "course_title": "Programming Languages I"
                        },
                        {
                            "course_id": 35,
                            "course_title": "Software Engineering"
                        },
                        {
                            "course_id": 37,
                            "course_title": "Compilers"
                        },
                        {
                            "course_id": 39,
                            "course_title": "Internet Programming"
                        },
                        {
                            "course_id": 44,
                            "course_title": "Programming Languages II"
                        }
                    ],
                    "skill_title": "java"
                },
                {
                    "related_courses": [],
                    "skill_title": "rest"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 31,
                            "course_title": "Databases"
                        },
                        {
                            "course_id": 39,
                            "course_title": "Internet Programming"
                        }
                    ],
                    "skill_title": "html"
                },
                {
                    "related_courses": [],
                    "skill_title": "html5"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 31,
                            "course_title": "Databases"
                        }
                    ],
                    "skill_title": "sql"
                },
                {
                    "related_courses": [],
                    "skill_title": "git"
                }
            ],
            "skill_title": "javascript"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [
                        {
                            "course_id": 16,
                            "course_title": "Human- Computer Interaction"
                        }
                    ],
                    "skill_title": "ux"
                }
            ],
            "skill_title": "akka"
        },
        {
            "relevant_skills": [],
            "skill_title": "go"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "css"
                },
                {
                    "related_courses": [],
                    "skill_title": "css3"
                },
                {
                    "related_courses": [],
                    "skill_title": "javascript"
                }
            ],
            "skill_title": "html5"
        },
        {
            "relevant_skills": [],
            "skill_title": "linux"
        },
        {
            "relevant_skills": [],
            "skill_title": "aws"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_title": "git"
                }
            ],
            "skill_title": "jenkins"
        },
        {
            "relevant_skills": [],
            "skill_title": "php"
        }
    ]
}
```
