document.addEventListener('DOMContentLoaded', function() {
    //const watchlist_link = document.querySelector('#watchlist-link');
    document.querySelectorAll('#watchlist-link').forEach(watchlist_link =>{
        watchlist_link.onclick = function(){
            watchlist_drink(this.dataset.postid)
        }
    })
});

function watchlist_drink(post_id){
    // Put drink in user watchlist or not
    const current_user = document.querySelector('#username-title').innerHTML;
    console.log(current_user)
}
