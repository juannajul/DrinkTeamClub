document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#watchlist-link').forEach(watchlist_link =>{
        watchlist_link.onclick = function(){
            watchlist_drink(this.dataset.postid)
        }
    })
});

function watchlist_drink(drink_id){
    // Put drink in user watchlist or not
    const current_user = document.querySelector('#username-title').innerHTML;
    console.log(current_user)
    var is_linking_by_user = false;
    fetch(`/drink_watchlist/${drink_id}`)
        .then(response => response.json())
        .then(drink =>{
            let drink_favorites = drink['favorites']
            if (drink_favorites.includes(current_user) === false ){
                is_linking_by_user = true;
                fetch(`/drink_watchlist/${drink_id}`,{
                    method: 'PUT',
                    body: JSON.stringify({favorites:true})
                })

                if (is_linking_by_user === true){
                    let change_class = document.querySelector(`.watchlist-link${drink_id}`);
                    change_class.classList.replace("your-drink-button","your-drink-button-in-list");
                }
            } else if (drink_favorites.includes(current_user) === true ){
                is_linking_by_user = false;
                fetch(`/drink_watchlist/${drink_id}`, {
                    method: 'PUT',
                    body: JSON.stringify({favorites:true})
                })

                if (is_linking_by_user === false){
                    let change_class = document.querySelector(`.watchlist-link${drink_id}`);
                    change_class.classList.replace("your-drink-button-in-list","your-drink-button");
                }
            }
        })
}