class Student:
    def __init__(self, name, math_score, literature_score, english_score):
        self.name = name
        self.scores = [math_score, literature_score, english_score]

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)


class Class:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_highest_average_score(self):
        return max(student.get_average_score() for student in self.students)

    def print_student_scores(self):
        for student in self.students:
            scores = ", ".join(f"{subject}: {score}" for subject, score in zip(["toan", "van", "anh"], student.scores))
            average_score = student.get_average_score()
            print(f"name: {student.name}, {scores}, avg: {average_score}")

    def get_students_with_highest_average_scores(self):
        highest_average = self.get_highest_average_score()
        return [student.name for student in self.students if student.get_average_score() == highest_average]


def main():
    classroom = Class()

    n = int(input("Nhập số lượng học sinh: "))
    for i in range(n):
        name = input("Nhập tên học sinh: ")
        scores = [float(input(f"Nhập điểm {subject}: ")) for subject in ["toan", "van", "anh"]]

        student = Student(name, *scores)
        classroom.add_student(student)

    highest_average = classroom.get_highest_average_score()
    print(f"Điểm trung bình cao nhất của lớp: {highest_average}")

    classroom.print_student_scores()

    highest_scoring_students = classroom.get_students_with_highest_average_scores()
    print("Danh sách tên học sinh có điểm trung bình cao nhất:")
    for student_name in highest_scoring_students:
        print(student_name)


main()
