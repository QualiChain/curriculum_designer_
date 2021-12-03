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

## Curriculum Designer API example

### Input
POST request to:
'http://127.0.0.1:6060/curriculum_recommendation'

### Output
```json
{
    "recommended_skills": [
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 793,
            "skill_title": "windows"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 752,
                    "skill_title": "git"
                }
            ],
            "scored_courses": [],
            "skill_id": 1305,
            "skill_title": "docker"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 462,
            "skill_title": "r"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 244,
            "skill_title": "scripting"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 902,
                    "skill_title": "html5"
                }
            ],
            "scored_courses": [],
            "skill_id": 1202,
            "skill_title": "css3"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 1215,
            "skill_title": "api"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 810,
            "skill_title": "react"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 902,
                    "skill_title": "html5"
                },
                {
                    "related_courses": [],
                    "skill_id": 1174,
                    "skill_title": "javascript"
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
                    "skill_id": 109,
                    "skill_title": "html"
                }
            ],
            "scored_courses": [
                {
                    "course_id": 31,
                    "course_title": "Databases",
                    "score": 1.0
                },
                {
                    "course_id": 39,
                    "course_title": "Internet Programming",
                    "score": 1.0
                }
            ],
            "skill_id": 1017,
            "skill_title": "css"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 752,
                    "skill_title": "git"
                },
                {
                    "related_courses": [],
                    "skill_id": 1288,
                    "skill_title": "rest"
                }
            ],
            "scored_courses": [],
            "skill_id": 1244,
            "skill_title": "json"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 1174,
                    "skill_title": "javascript"
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
                    "skill_id": 68,
                    "skill_title": "java"
                },
                {
                    "related_courses": [],
                    "skill_id": 1244,
                    "skill_title": "json"
                },
                {
                    "related_courses": [],
                    "skill_id": 589,
                    "skill_title": "jenkins"
                },
                {
                    "related_courses": [],
                    "skill_id": 902,
                    "skill_title": "html5"
                },
                {
                    "related_courses": [],
                    "skill_id": 1305,
                    "skill_title": "docker"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 41,
                            "course_title": "Advanced Topics in Database Systems"
                        }
                    ],
                    "skill_id": 213,
                    "skill_title": "nosql"
                },
                {
                    "related_courses": [],
                    "skill_id": 1017,
                    "skill_title": "css"
                },
                {
                    "related_courses": [],
                    "skill_id": 1288,
                    "skill_title": "rest"
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
                    "skill_id": 1075,
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
                    "skill_id": 678,
                    "skill_title": "c"
                }
            ],
            "scored_courses": [
                {
                    "course_id": 18,
                    "course_title": "Multimedia Technology",
                    "score": 0.5
                },
                {
                    "course_id": 21,
                    "course_title": "Computer System Performance",
                    "score": 0.5
                },
                {
                    "course_id": 25,
                    "course_title": "Distributed Systems",
                    "score": 1.0
                },
                {
                    "course_id": 32,
                    "course_title": "Programming Languages I",
                    "score": 1.0
                },
                {
                    "course_id": 35,
                    "course_title": "Software Engineering",
                    "score": 0.5
                },
                {
                    "course_id": 37,
                    "course_title": "Compilers",
                    "score": 1.0
                },
                {
                    "course_id": 39,
                    "course_title": "Internet Programming",
                    "score": 0.5
                },
                {
                    "course_id": 44,
                    "course_title": "Programming Languages II",
                    "score": 1.0
                },
                {
                    "course_id": 41,
                    "course_title": "Advanced Topics in Database Systems",
                    "score": 0.5
                },
                {
                    "course_id": 46,
                    "course_title": "Digital Communications I",
                    "score": 0.5
                },
                {
                    "course_id": 15,
                    "course_title": "Operating Systems",
                    "score": 0.5
                },
                {
                    "course_id": 19,
                    "course_title": "Operating Systems Laboratory",
                    "score": 0.5
                },
                {
                    "course_id": 33,
                    "course_title": "Algorithms and Complexity",
                    "score": 0.5
                },
                {
                    "course_id": 34,
                    "course_title": "Artificial Intelligence",
                    "score": 0.5
                }
            ],
            "skill_id": 752,
            "skill_title": "git"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 930,
                    "skill_title": "ios"
                }
            ],
            "scored_courses": [],
            "skill_id": 656,
            "skill_title": "android"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 817,
            "skill_title": "angular"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 1137,
            "skill_title": "tcp"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 1244,
                    "skill_title": "json"
                },
                {
                    "related_courses": [],
                    "skill_id": 1174,
                    "skill_title": "javascript"
                },
                {
                    "related_courses": [],
                    "skill_id": 752,
                    "skill_title": "git"
                }
            ],
            "scored_courses": [],
            "skill_id": 1288,
            "skill_title": "rest"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 656,
                    "skill_title": "android"
                }
            ],
            "scored_courses": [],
            "skill_id": 930,
            "skill_title": "ios"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 752,
                    "skill_title": "git"
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
                    "skill_id": 68,
                    "skill_title": "java"
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
                    "skill_id": 109,
                    "skill_title": "html"
                },
                {
                    "related_courses": [],
                    "skill_id": 902,
                    "skill_title": "html5"
                },
                {
                    "related_courses": [],
                    "skill_id": 1288,
                    "skill_title": "rest"
                },
                {
                    "related_courses": [
                        {
                            "course_id": 31,
                            "course_title": "Databases"
                        }
                    ],
                    "skill_id": 663,
                    "skill_title": "sql"
                },
                {
                    "related_courses": [],
                    "skill_id": 1017,
                    "skill_title": "css"
                }
            ],
            "scored_courses": [
                {
                    "course_id": 18,
                    "course_title": "Multimedia Technology",
                    "score": 0.5
                },
                {
                    "course_id": 21,
                    "course_title": "Computer System Performance",
                    "score": 0.5
                },
                {
                    "course_id": 25,
                    "course_title": "Distributed Systems",
                    "score": 0.5
                },
                {
                    "course_id": 32,
                    "course_title": "Programming Languages I",
                    "score": 0.5
                },
                {
                    "course_id": 35,
                    "course_title": "Software Engineering",
                    "score": 0.5
                },
                {
                    "course_id": 37,
                    "course_title": "Compilers",
                    "score": 0.5
                },
                {
                    "course_id": 39,
                    "course_title": "Internet Programming",
                    "score": 1.0
                },
                {
                    "course_id": 44,
                    "course_title": "Programming Languages II",
                    "score": 0.5
                },
                {
                    "course_id": 31,
                    "course_title": "Databases",
                    "score": 1.0
                }
            ],
            "skill_id": 1174,
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
                    "skill_id": 632,
                    "skill_title": "ux"
                }
            ],
            "scored_courses": [
                {
                    "course_id": 16,
                    "course_title": "Human- Computer Interaction",
                    "score": 1.0
                }
            ],
            "skill_id": 74,
            "skill_title": "akka"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 1297,
            "skill_title": "go"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 1202,
                    "skill_title": "css3"
                },
                {
                    "related_courses": [],
                    "skill_id": 1017,
                    "skill_title": "css"
                },
                {
                    "related_courses": [],
                    "skill_id": 1174,
                    "skill_title": "javascript"
                }
            ],
            "scored_courses": [],
            "skill_id": 902,
            "skill_title": "html5"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 1201,
            "skill_title": "linux"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 709,
            "skill_title": "aws"
        },
        {
            "relevant_skills": [
                {
                    "related_courses": [],
                    "skill_id": 752,
                    "skill_title": "git"
                }
            ],
            "scored_courses": [],
            "skill_id": 589,
            "skill_title": "jenkins"
        },
        {
            "relevant_skills": [],
            "scored_courses": [],
            "skill_id": 1048,
            "skill_title": "php"
        }
    ]
}
```
