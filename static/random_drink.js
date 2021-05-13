document.addEventListener('DOMContentLoaded', function() {
    //document.querySelector('#edit-post-link').addEventListener('click', () => load_edit_page('edit_post'));
    document.querySelector('#random-button').addEventListener('click', () => random_cocktail())
    console.log('algo')
});

function random_cocktail(){
    fetch('/random_cocktail/')
    .then(response => response.json())
    .then(drink => {
        // create cocktail
         document.querySelector('.drink-img-random-container').innerHTML = `<img src="${drink.drink_image}" alt="cocktail">`;
        const ingredients = drink.ingredients.join(', ');
        document.querySelector('.drink-name-title').innerHTML = `<h3>${drink.drink_name}</h3>`;
        document.querySelector('.drink-ingredients').innerHTML = `<p><em>Ingredients: </em>${ingredients}</p>`;
        document.querySelector('.drink-category').innerHTML = `<p><em>Category:</em> ${drink.category}</p>`;
        document.querySelector('.drink-instructions').innerHTML = `<p><em>Instructions: </em>${drink.drink_instructions}</p>`;
        document.querySelector('.close-random-drink').innerHTML = `<button id="close-random-button">Close</button>`;
        document.querySelector('#random-modal-content').style.display = 'block';
        document.querySelector('#close-random-button').addEventListener('click', () =>{
            document.querySelector('#random-modal-content').style.display = 'none';
        })
    });
}