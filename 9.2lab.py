from os import listdir

def compare_files():
    with open('students1.txt') as f1, open('students2.txt') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for l1, l2 in zip(lines1, lines2):
            if l1 != l2:
                print(f"Those lines are not equal: {l1} | {l2}")
                return 
        print("Files are equal")

compare_files()
