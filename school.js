const classList = [];

function enrollStudent(s_firstName, s_lastName, s_age, s_currentMark) {
    const student = {
        firstName: s_firstName,
        lastName: s_lastName,
        age: s_age,
        currentMark: s_currentMark
    };
    classList.push(student);
};

// Test student enrollment
enrollStudent('John', 'Doe', 15, 5);
