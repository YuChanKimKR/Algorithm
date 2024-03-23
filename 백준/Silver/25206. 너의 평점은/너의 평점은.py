# 과목별 등급에 따른 학점을 저장하는 딕셔너리
grade_point = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

# 총 학점과 과목별 학점을 초기화
total_credit = 0
total_grade_point = 0

# 치훈이가 수강한 과목의 개수
num_courses = 20

# 각 과목에 대해 반복하면서 학점을 계산
for _ in range(num_courses):
    course, credit, grade = input().split()  # 공백 기준으로 과목명, 학점, 등급 입력 받기
    
    # 등급이 P인 과목은 계산에서 제외
    if grade != 'P':
        credit = float(credit)  # 학점은 실수형으로 변환
        total_credit += credit  # 총 학점 누적
        
        # 과목별 학점 계산하여 총 과목별 학점에 누적
        total_grade_point += credit * grade_point[grade]

# 전공평점 계산
major_GPA = total_grade_point / total_credit

# 결과 출력
print(major_GPA)