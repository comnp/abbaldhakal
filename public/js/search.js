document.addEventListener('DOMContentLoaded', function() {
    const scholarships = []; // This will hold our scholarship data

    // Fetch the scholarships data
    fetch('/data/scholarships.json')
        .then(response => response.json())
        .then(data => {
            scholarships.push(...data.scholarships);
            displayScholarships(scholarships);
        });

    // Function to display scholarships
    function displayScholarships(scholarships) {
        const results = document.getElementById('results');
        results.innerHTML = '';
        scholarships.forEach(scholarship => {
            const div = document.createElement('div');
            div.classList.add('scholarship');
            div.innerHTML = `
                <h3>${scholarship['Name of Scholarship']}</h3>
                <p><strong>University:</strong> ${scholarship['Name of University']}</p>
                <p><strong>Type:</strong> ${scholarship['Scholarship Attribute 1']}</p>
                <p><strong>Coverage:</strong> ${scholarship['Scholarship Attribute 2']}</p>
                <p><a href="${scholarship['Scholarship Link']}">More Info</a></p>
            `;
            results.appendChild(div);
        });
    }

    // Event listener for the search form
    document.getElementById('search-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const query = document.getElementById('query').value.toLowerCase();
        const type = document.getElementById('type').value;
        const coverage = document.getElementById('coverage').value;

        const filtered = scholarships.filter(scholarship => {
            return (
                (scholarship['Name of Scholarship'].toLowerCase().includes(query) ||
                scholarship['Name of University'].toLowerCase().includes(query)) &&
                (type === '' || scholarship['Scholarship Attribute 1'] === type) &&
                (coverage === '' || scholarship['Scholarship Attribute 2'] === coverage)
            );
        });
        displayScholarships(filtered);
    });
});
