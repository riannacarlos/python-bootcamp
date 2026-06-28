student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)
student_sections = ("A","B","C")
# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""
for name,score,section in zip(student_names, student_scores,student_sections):
    print(f"Student:{name} from section {section} scored {score} in the exam")
