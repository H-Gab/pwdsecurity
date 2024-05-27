const fs = require('fs');

function printValue(inputId) {
    var inputValue = document.getElementById(inputId).value;
    var displayElement = document.getElementById(inputId + '_display');
    if (displayElement.innerText) {
        displayElement.innerText += ', ' + inputValue;
    } else {
        displayElement.innerText = inputValue;
    }
}

function exportCSV() {
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('email').value;
    var username = document.getElementById('username').value;

    var csvContent = 'First Name,Last Name,Email,Username\n';
    csvContent += `${fname},${lname},${email},${username}`;

    fs.writeFile('test.csv', csvContent, (err) => {
        if (err) {
            console.error('Error writing to CSV file', err);
        } else {
            console.log('CSV file written successfully.');
        }
    });
}