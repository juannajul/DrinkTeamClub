# DreamTeamClub

TeamDreamClub is a web application that offers great choices of drinks and cocktails, the app will obtain the information for each 
drink/cocktail from the "Thecocktaildb" API and save all of them in the dreamTeamClub database. In this web app the user can look for a variety of cocktails by using the "Random button" or search for its favorites drinks by its cocktail name, category or ingredient. Each search will show: cocktail name, picture, category, ingredients and instructions of each drink.

The user may create an account, log in and save or delete his favorites cocktails/drinks in his "Drinks List", doing this the user should have the information right away, when it's needed.

### Files and Directories:
* `FinalProyectCS50`: Main application directory.
    * `drinkTeamClub`: drinkTeamClub App.
        *`forms.py`: forms for search drinks/cocktails.
        *`models.py`: ORM drinkTeamClub model. Models class of Drinks, Ingredients, Categories.
        *`urls.py`: All drinkTeamClub paths for get drinks form thecocktailsdb api, search cocktails/drinks, watch cocktails/drinks.
        *`views.py`: All drinkTeamClub functions views for get cocktails from thecocktailsdbapi, search cocktails, user favorites cocktails, watch favorites cocktails.
    * `finalProjectCS50`: main urls and settings.
    * `static`: static files folders.
        *`css`: css styles file.
        *`img`: static images and icons.
        *`js`: javascript files.
            *`favorite_drinks.js`: add drinks to favorites drinks list.
            *`random_drink.js`: get random drinks.
            *`remove_drinks.js`: delete drinks from favorites drinks list.
    *`templates`: all the html files.
        *`drinkTeam`: html drinks folder.
            *`cocktails_search.html`: show all drinks/cocktails searches.
            *`index.html`: index page.
            *`favorites_drinks.html`: show user favorite drinks list.
        *`users`: html users files.
            *`login.html`: log in html page.
            *`register`: Sign up html page.
        *`error_page.html`: error html page.
        *`layout.html`: layout html page.
    *`users`: Users app.
        *`models.py`: ORM users model. Model class of User.
        *`urls.py`: All Users paths for register, login, logout.
        *`views.py`: all Users functions views fot register, login and logout.

### Justification
* This app is diferent from the other projects.
* In this app thecocktailsdb Api is used and that provide us more than 500 drinks and cocktails for the app and the users and will be stored in the drinkTeamClub database.
* Uses fecth and javascript for events without reloading the page.
* Completely Mobile responsive.


### How to run this app
* To run this web app you have to install all the requirements from requirements.txt in your enviroment with: 
```pip install -r requirements.txt```
* Make the migrations:
```python manage.py makemigrations```
```python manage.py migrate```
* Run django app:
```python manage.py runserver```

### Additional information the staff should know about the project.
When your start the web app with a new database, the page needs to obtain some drinks and cocktails from the "thecocktailsdb" API. Then the app would have drinks and cocktails in the database and everyone could make all the searches. So you can obtain drinks and cocktails from de API searching cocktails by name.