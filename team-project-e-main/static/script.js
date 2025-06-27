// This file was written by generative AI (5/16/25) for the interactive HTML search ingredients form
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('search-form');
    const includeInput = document.getElementById('include-input');
    const excludeInput = document.getElementById('exclude-input');
    const includeHidden = document.getElementById('include-hidden');
    const excludeHidden = document.getElementById('exclude-hidden');
    
    // Store ingredients
    const includedIngredients = [];
    const excludedIngredients = [];
    
    // Handle form submission
    form.addEventListener('submit', function(e) {
        // Update hidden inputs with comma-separated values
        includeHidden.value = includedIngredients.join(',');
        excludeHidden.value = excludedIngredients.join(',');
        
        // Form will submit normally with POST
    });
    
    // Add ingredient to include list
    includeInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            const ingredient = this.value.trim().toLowerCase();
            if (ingredient && !includedIngredients.includes(ingredient)) {
                includedIngredients.push(ingredient);
                addIngredientTag(ingredient, 'include');
                this.value = '';
            }
        }
    });
    
    // Add ingredient to exclude list
    excludeInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            const ingredient = this.value.trim().toLowerCase();
            if (ingredient && !excludedIngredients.includes(ingredient)) {
                excludedIngredients.push(ingredient);
                addIngredientTag(ingredient, 'exclude');
                this.value = '';
            }
        }
    });
    
    function addIngredientTag(ingredient, type) {
        const container = document.getElementById(`${type}-container`);
        const tag = document.createElement('div');
        tag.className = `ingredient-tag ${type}-tag`;
        tag.innerHTML = `
            ${ingredient}
            <button type="button" class="delete-btn" data-type="${type}">&times;</button>
        `;
        container.appendChild(tag);
        
        tag.querySelector('.delete-btn').addEventListener('click', function() {
            const ingredients = type === 'include' ? includedIngredients : excludedIngredients;
            const index = ingredients.indexOf(ingredient);
            if (index > -1) ingredients.splice(index, 1);
            tag.remove();
        });
    }
});
