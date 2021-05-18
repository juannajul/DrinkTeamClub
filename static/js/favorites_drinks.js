document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#favorite-drink-link').forEach(favorite_link =>{
        favorite_link.onclick = function(){
            favorite_drink(this.dataset.postid)
        }
    })
});

function favorite_drink(drink_id){
    // Put drink in user favorites or not
    const current_user = document.querySelector('#username-title').innerHTML;
    var is_linking_by_user = false;
    fetch(`/drink_favorite/${drink_id}`)
        .then(response => response.json())
        .then(drink =>{
            let drink_favorites = drink['favorites']
            if (drink_favorites.includes(current_user) === false ){
                is_linking_by_user = true;
                fetch(`/drink_favorite/${drink_id}`,{
                    method: 'PUT',
                    body: JSON.stringify({favorites:true})
                })

                if (is_linking_by_user === true){
                    let change_class = document.querySelector(`.favorite-drink-link${drink_id}`);
                    change_class.classList.replace("your-drink-button","your-drink-button-in-list");
                }
            } else if (drink_favorites.includes(current_user) === true ){
                is_linking_by_user = false;
                fetch(`/drink_favorite/${drink_id}`, {
                    method: 'PUT',
                    body: JSON.stringify({favorites:true})
                })

                if (is_linking_by_user === false){
                    let change_class = document.querySelector(`.favorite-drink-link${drink_id}`);
                    change_class.classList.replace("your-drink-button-in-list","your-drink-button");
                }
            }
        })
}