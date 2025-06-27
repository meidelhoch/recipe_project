// This was written with the help of Gemeni

document.addEventListener('DOMContentLoaded', function() {
    const inputField = document.getElementById('recipe_search');
    const suggestionsList = document.getElementById('suggestions');

    inputField.addEventListener('input', function() {
        const query = this.value;
        console.log(query);
        if (query.length >= 2) { // Or your desired minimum characters
            fetch(`/autocomplete?cur_search=${query}`)
                .then(response => response.json())
                .then(data => {
                    displaySuggestions(data);
                })
                .catch(error => {
                    console.error('Error fetching autocomplete suggestions:', error);
                });
        } else {
            clearSuggestions();
        }
    });

    function displaySuggestions(suggestions) {
        suggestionsList.innerHTML = ''; // Clear previous suggestions
        if (suggestions && suggestions.length > 0) {
            suggestions.forEach(suggestion => {
                const listItem = document.createElement('p');
                listItem.textContent = suggestion;
                listItem.className = 'suggestion-item';
                listItem.addEventListener('click', function() {
                    inputField.value = suggestion;
                    clearSuggestions();
                });
                suggestionsList.appendChild(listItem);
            });
        } else {
            clearSuggestions(); // Clear if no suggestions
        }
    }

    function clearSuggestions() {
        suggestionsList.innerHTML = '';
    }
});
