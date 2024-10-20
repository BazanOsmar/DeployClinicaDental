const input = document.getElementById('search-input');

input.addEventListener('input', searchPatient);

function searchPatient() {
    let inputValue = input.value.toLowerCase();
    let table = document.querySelector("table tbody");
    let rows = table.getElementsByTagName("tr");
    let found = false; 

    for (let i = 0; i < rows.length; i++) {
        let cells = rows[i].getElementsByTagName("td");
        let patientName = cells[1].textContent.toLowerCase();

        if (patientName.includes(inputValue)) {
            rows[i].style.display = "";
            found = true; 
        } else {
            rows[i].style.display = "none";
        }
    }

    const message = document.getElementById("message");
    if (!found && inputValue) {
        message.textContent = "No se encontraron pacientes con ese nombre.";
    } else {
        message.textContent = ""; 
    }
}

function sortTable() {
    const table = document.getElementById('citas-table');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    const parseDateTime = (dateStr, timeStr) => {
        const [year, month, day] = dateStr.split('-');
        const [hours, minutes] = timeStr.split(':');
        
        return new Date(year, month - 1, day, hours, minutes); 
    };

    rows.sort((a, b) => {
        const dateA = a.cells[2].textContent; 
        const timeA = a.cells[3].textContent; 
        const dateB = b.cells[2].textContent; 
        const timeB = b.cells[3].textContent; 

        const dateTimeA = parseDateTime(dateA, timeA);
        const dateTimeB = parseDateTime(dateB, timeB);
        
        return dateTimeA - dateTimeB; 
    });

    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));
}

document.addEventListener('DOMContentLoaded', () => {
    sortTable();
});


