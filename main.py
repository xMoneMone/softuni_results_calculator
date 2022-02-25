from scraper import names
from credentials import task_per_person


def main():
    total = 0
    max_result = 0

    tasks_names = {}

    for ind, name in enumerate(names):
        tasks_names[ind] = name

    tasks_rarity = {}

    tasks_total_score = {}

    grades = open("auto_grades.txt", "r")
    for line in grades:
        student = str(line).replace("[", "").replace("]", "").replace(" ", "").replace("\n", "")
        student = student.split(",")
        total += 1
        three = 0
        for ind, task in enumerate(student):
            if task != "-":
                if task == "100":
                    three += 1
                if ind in tasks_rarity.keys():
                    tasks_rarity[ind] += 1
                else:
                    tasks_rarity[ind] = 1
                if ind in tasks_total_score.keys():
                    tasks_total_score[ind] += int(task)
                else:
                    tasks_total_score[ind] = int(task)
        if three == task_per_person:
            max_result += 1

    average = sum(tasks_total_score.values()) // total
    rarest_task = tasks_names[min(tasks_rarity, key=tasks_rarity.get)]
    most_common_task = tasks_names[max(tasks_rarity, key=tasks_rarity.get)]
    hardest_task = tasks_names[min(tasks_total_score, key=tasks_total_score.get)]
    hardest_average = min(tasks_total_score.values()) // tasks_rarity[min(tasks_total_score, key=tasks_total_score.get)]
    easiest_task = tasks_names[max(tasks_total_score, key=tasks_total_score.get)]
    easiest_average = max(tasks_total_score.values()) // tasks_rarity[max(tasks_total_score, key=tasks_total_score.get)]
    # print(total, average, rarest_task, hardest_task, easiest_task_task)

    print(f"""
------------------------------------------------------------------------
Total examinees: {total}
Examinees with max result: {max_result}
Average score: {average}/{task_per_person * 100}
Rarest task: {rarest_task} (Got: {min(tasks_rarity.values())})
Most common task: {most_common_task} (Got: {max(tasks_rarity.values())})
Hardest task: {hardest_task} (Average score: {hardest_average}/100)
Easiest task: {easiest_task} (Average score: {easiest_average}/100)
------------------------------------------------------------------------""")


if __name__ == "__main__":
    main()