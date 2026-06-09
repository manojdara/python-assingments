# 📚 Student Grading System

A comprehensive web-based **Student Grading System** built with Flask that automatically calculates grades, percentages, and pass/fail status for students across 6 subjects.

## ✨ Features

- ✅ **Student Dashboard** - View individual student grades and performance
- ✅ **6 Subjects** - Maths, English, Telugu, Science, Commerce, History
- ✅ **Automated Grading** - Automatic grade calculation based on scores
- ✅ **Comprehensive Calculations** - Total marks, average percentage, letter grades
- ✅ **Pass/Fail Logic** - Overall FAIL if any subject < 60%
- ✅ **Add New Students** - Dynamically add students to the system
- ✅ **Student Directory** - View all enrolled students
- ✅ **Color-Coded Display** - Visual representation of grades
- ✅ **Responsive Design** - Works on desktop and mobile devices
- ✅ **Grading Scale Reference** - Built-in grading scale guide

## 📋 Grading Scale

| Grade | Percentage | Description |
|-------|-----------|-------------|
| A | 90-100% | Excellent |
| B | 80-89% | Good |
| C | 70-79% | Average |
| D | 60-69% | Fair |
| F | Below 60% | Fail |

**Passing Mark:** 60% (per subject and overall)

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Storage**: In-memory dictionary (Python)
- **Styling**: Responsive CSS with gradients

## 📦 Requirements

```
Flask>=2.0.0
```

## 🚀 Installation & Setup

### Step 1: Navigate to Project Directory
```bash
cd d:\ignitz-assingment\python-assingments\class9-06-05-26
```

### Step 2: Create Virtual Environment (if not already created)
```bash
uv venv
```

### Step 3: Activate Virtual Environment
```bash
.venv\Scripts\activate
```

### Step 4: Install Flask
```bash
uv pip install flask
```

### Step 5: Run the Application
```bash
python app.py
```

The application will start at: **http://localhost:5000/**

## 💻 How to Use

### 1. **View Dashboard (Existing Student)**
   - Go to home page
   - Enter a **Student ID** (001, 002, 003, or 004)
   - Click **"View Dashboard"**
   - See complete grade analysis

### 2. **View All Students**
   - Click **"👥 View All Students"** button
   - See table of all enrolled students
   - Click **"View Dashboard"** for any student

### 3. **Add New Student**
   - Click **"+ Add New Student"** button
   - Enter student details:
     - Full Name
     - Email Address
     - Grades for 6 subjects (0-100)
   - Click **"✓ Submit & View Dashboard"**
   - New student is automatically added to system
   - Unique Student ID is auto-generated

## 📁 Project Structure

```
class9-06-05-26/
├── app.py                    # Main Flask application
├── README.md                 # This file
├── static/
│   └── favicon.svg          # App icon (book with star)
└── templates/
    ├── index.html           # Login/Home page
    ├── dashboard.html       # Student grade dashboard
    ├── add_student.html     # Add new student form
    └── students_list.html   # All students directory
```

## 🔐 Sample Test Data

Pre-loaded students for testing:

| ID | Name | Maths | English | Telugu | Science | Commerce | History | Status |
|----|------|-------|---------|--------|---------|----------|---------|--------|
| 001 | Alice Johnson | 92 | 85 | 88 | 90 | 87 | 89 | ✓ PASS |
| 002 | Bob Smith | 78 | 82 | 75 | 80 | 72 | 76 | ✓ PASS |
| 003 | Charlie Brown | 95 | 91 | 93 | 97 | 89 | 92 | ✓ PASS |
| 004 | Diana Prince | 85 | 88 | 92 | 90 | 45 | 87 | ✗ FAIL |

**Note:** Diana Prince (ID: 004) has FAILED because Commerce score (45%) is below 60%, even though average is 82%.

## 🧮 Grade Calculations

### Total Marks
```
Total = Sum of all 6 subject scores (out of 600)
```

### Average Percentage
```
Average = Total Marks / 6 subjects
```

### Letter Grade (Overall)
```
Based on average percentage using grading scale
```

### Overall Pass/Fail Status
```
PASS: All 6 subjects must have ≥ 60%
FAIL: If ANY subject < 60% (even if average is ≥ 60%)
```

### Subject-wise Status
```
Each subject individually checked for pass/fail (≥ 60%)
```

## 🎨 Dashboard Features

The dashboard displays:

1. **Student Information**
   - Student ID
   - Full Name
   - Email Address

2. **Summary Cards**
   - Total Marks (out of 600)
   - Average Percentage
   - Overall Grade (Letter)

3. **Status Indicator**
   - Large visual pass/fail icon
   - Green checkmark (✓) for PASS
   - Red X (✗) for FAIL

4. **Grading Scale Reference**
   - Quick reference guide for all grade ranges
   - Passing grade threshold highlighted

5. **Subject Cards**
   - Individual subject scores
   - Letter grades
   - Percentages
   - Pass/Fail status per subject
   - Color-coded display

## 🔄 Key Functions Explained

### `get_letter_grade(percentage)`
Converts percentage to letter grade (A, B, C, D, F)

### `get_grade_color(percentage)`
Returns color code for visual display of each grade

### `is_passing(percentage)`
Checks if individual subject score ≥ 60%

### `check_overall_status(grades_dict)`
**Important:** Checks if student passed ALL subjects
- Returns FALSE (FAIL) if ANY subject < 60%
- Returns TRUE (PASS) only if ALL subjects ≥ 60%

## 📝 Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Home/Login page |
| `/students` | GET | View all students |
| `/dashboard` | POST | Display student dashboard |
| `/add-student` | GET | Show add student form |
| `/add-student` | POST | Add new student to system |

## 🎓 Use Cases

1. **School/College Administration**
   - Track student performance across subjects
   - Identify students needing support
   - Generate grade reports

2. **Teachers**
   - View student grades at a glance
   - Track which students are failing
   - Manage multiple students easily

3. **Parents/Guardians**
   - Check children's academic performance
   - See subject-wise breakdown
   - Monitor overall progress

## 💡 Special Features

### Visual Pass/Fail Indicator
- **Green card with checkmark** for PASS
- **Red card with X** for FAIL
- Makes student status immediately clear

### Automatic ID Generation
- New students automatically get unique IDs
- IDs increment from highest existing ID
- No manual ID management needed

### Color-Coded Grades
- Each grade has its own color
- Visual feedback improves understanding
- Easy to spot weak areas at a glance

## 🌐 Browser Compatibility

- Chrome/Chromium ✓
- Firefox ✓
- Safari ✓
- Edge ✓
- Opera ✓

## 📱 Responsive Design

- Desktop: Full layout with all features
- Tablet: Optimized for medium screens
- Mobile: Single column layout for easy viewing

## 🔒 Notes

- Data is stored in memory (Python dictionary)
- Data resets when app is restarted
- For production, use database (SQLite, PostgreSQL, etc.)
- No authentication implemented (add if needed for production)

## 🚀 Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User authentication & login
- [ ] Export grades to PDF/Excel
- [ ] Parent portal
- [ ] Grade trends & analytics
- [ ] Email notifications
- [ ] Admin dashboard
- [ ] Grade appeals system

## 📧 Support

For issues or questions, please review the code comments in `app.py`

## 📄 License

This project is open source and available for educational purposes.

---

**Created:** June 2026  
**Version:** 1.0  
**Status:** Active Development
