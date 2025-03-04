const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, content) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = content.split('\n').filter(line => line.trim() !== '');
            if (lines.length < 2) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const students = lines.slice(1).map(line => line.split(','));
            const studentGroups = {};
            let totalStudents = 0;

            students.forEach(student => {
                if (student.length > 1) {
                    const field = student[student.length - 1].trim();
                    const firstName = student[0].trim();
                    if (!studentGroups[field]) {
                        studentGroups[field] = [];
                    }
                    studentGroups[field].push(firstName);
                    totalStudents++;
                }
            });

            console.log(`Number of students: ${totalStudents}`);
            Object.entries(studentGroups).forEach(([field, names]) => {
                console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
            });

            resolve();
        });
    });
}

module.exports = countStudents;
