students_db = {
    'grading_scales': {
        'percentage': {
            'Math': {'min': 97, 'max': 100, 'grade': 'A'},
            'Science': {'min': 93, 'max': 96, 'grade': 'A+'},
            'English': {'min': 90, 'max': 92, 'grade': 'A++'},
            'History': {'min': 87, 'max': 89, 'grade': 'B'},
            'Physics': {'min': 83, 'max': 86, 'grade': 'B+'},
        }
    }
}
subject  = input("Enter the subject : ")
print(f"in order {subject} to  score {students_db['grading_scales']["percentage"][subject]["grade"]} you need to score between {students_db['grading_scales']["percentage"][subject]["min"]} and {students_db['grading_scales']["percentage"][subject]["max"]}")
