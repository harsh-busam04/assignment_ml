def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        grade = "A"
    elif 80 <= average < 90:
        grade = "B"
    elif 70 <= average < 80:
        grade = "C"
    else:
        grade = "Fail"
    return grade

def main():
    print("Enter marks for three subjects:")
    try:
        marks = []
        for i in range(1, 4):
            mark = float(input(f"Subject {i} marks: "))
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return
            marks.append(mark)
        grade = calculate_grade(marks)
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
