from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# Grading scale
def get_letter_grade(percentage):
    """Convert percentage to letter grade"""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def get_grade_color(percentage):
    """Get color for grade display"""
    if percentage >= 90:
        return '#00c896'  # Green for A
    elif percentage >= 80:
        return '#667eea'  # Blue for B
    elif percentage >= 70:
        return '#f5a623'  # Orange for C
    elif percentage >= 60:
        return '#ff9f43'  # Light Orange for D
    else:
        return '#e74c3c'  # Red for F

def is_passing(percentage):
    """Check if student is passing (>= 60%)"""
    return percentage >= 60

def check_overall_status(grades_dict):
    """Check if student passed overall (all subjects must be >= 60%)"""
    for marks in grades_dict.values():
        if marks < 60:
            return False
    return True

# Sample student data with 6 subjects
students = {
    '001': {
        'name': 'Alice Johnson',
        'email': 'alice@example.com',
        'grades': {
            'Maths': 92,
            'English': 85,
            'Telugu': 88,
            'Science': 90,
            'Commerce': 87,
            'History': 89
        }
    },
    '002': {
        'name': 'Bob Smith',
        'email': 'bob@example.com',
        'grades': {
            'Maths': 78,
            'English': 82,
            'Telugu': 75,
            'Science': 80,
            'Commerce': 72,
            'History': 76
        }
    },
    '003': {
        'name': 'Charlie Brown',
        'email': 'charlie@example.com',
        'grades': {
            'Maths': 95,
            'English': 91,
            'Telugu': 93,
            'Science': 97,
            'Commerce': 89,
            'History': 92
        }
    },
    '004': {
        'name': 'Diana Prince',
        'email': 'diana@example.com',
        'grades': {
            'Maths': 85,
            'English': 88,
            'Telugu': 92,
            'Science': 90,
            'Commerce': 45,
            'History': 87
        }
    }
}

@app.route('/')
def home():
    return render_template('index.html', student_count=len(students))

@app.route('/students')
def view_students():
    """Display all available students with their IDs"""
    students_list = []
    for student_id, student_data in students.items():
        students_list.append({
            'id': student_id,
            'name': student_data['name'],
            'email': student_data['email']
        })
    return render_template('students_list.html', students=students_list, total_students=len(students_list))

@app.route('/dashboard', methods=['POST'])
def dashboard():
    student_id = request.form.get('student_id')
    
    if student_id in students:
        student = students[student_id]
        
        # Calculate totals and averages
        total_marks = sum(student['grades'].values())
        num_subjects = len(student['grades'])
        average_percentage = total_marks / num_subjects
        
        # Check overall status - FAILED if any subject is below 60%
        overall_status_passed = check_overall_status(student['grades'])
        overall_grade = get_letter_grade(average_percentage)
        
        # Prepare grades with letter grades and colors
        grades_with_details = {}
        for subject, marks in student['grades'].items():
            grades_with_details[subject] = {
                'marks': marks,
                'grade': get_letter_grade(marks),
                'color': get_grade_color(marks),
                'status': 'Pass' if is_passing(marks) else 'Fail'
            }
        
        return render_template('dashboard.html', 
                             student_id=student_id,
                             student=student,
                             total_marks=total_marks,
                             average_percentage=round(average_percentage, 2),
                             overall_grade=overall_grade,
                             passing_status=overall_status_passed,
                             num_subjects=num_subjects,
                             grades_with_details=grades_with_details)
    else:
        return render_template('index.html', error='Student ID not found. Please try again.', student_count=len(students))

@app.route('/add-student')
def add_student_form():
    return render_template('add_student.html')

@app.route('/add-student', methods=['POST'])
def add_student():
    name = request.form.get('name')
    email = request.form.get('email')
    maths = int(request.form.get('maths', 0))
    english = int(request.form.get('english', 0))
    telugu = int(request.form.get('telugu', 0))
    science = int(request.form.get('science', 0))
    commerce = int(request.form.get('commerce', 0))
    history = int(request.form.get('history', 0))
    
    # Generate unique student ID
    student_id = str(int(max(students.keys(), key=int)) + 1).zfill(3)
    
    # Add new student
    students[student_id] = {
        'name': name,
        'email': email,
        'grades': {
            'Maths': maths,
            'English': english,
            'Telugu': telugu,
            'Science': science,
            'Commerce': commerce,
            'History': history
        }
    }
    
    # Calculate totals and averages
    student_data = students[student_id]
    total_marks = sum(student_data['grades'].values())
    num_subjects = len(student_data['grades'])
    average_percentage = total_marks / num_subjects
    
    # Check overall status - FAILED if any subject is below 60%
    overall_status_passed = check_overall_status(student_data['grades'])
    overall_grade = get_letter_grade(average_percentage)
    
    # Prepare grades with letter grades and colors
    grades_with_details = {}
    for subject, marks in student_data['grades'].items():
        grades_with_details[subject] = {
            'marks': marks,
            'grade': get_letter_grade(marks),
            'color': get_grade_color(marks),
            'status': 'Pass' if is_passing(marks) else 'Fail'
        }
    
    return render_template('dashboard.html',
                         student_id=student_id,
                         student=student_data,
                         total_marks=total_marks,
                         average_percentage=round(average_percentage, 2),
                         overall_grade=overall_grade,
                         passing_status=overall_status_passed,
                         num_subjects=num_subjects,
                         grades_with_details=grades_with_details,
                         new_student=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
