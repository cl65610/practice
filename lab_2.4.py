# Below the list of movies are the functions required in the lab.
# Below those is a function that should guide tehe user through the data.
#There may be a few bugs in that formula, but the required information is good, I think.
#Based on my testing, you can run this in the shell, and it works.

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#Given a certain movie title, this function will tell you if it's a good movie (> 5.5) or a bad movie (<= 5.5)
def overfivefive(movie):
    for x in movies:
        if x['name'] == movie:
            if x['imdb'] > 5.5:
                print 'That\'s a good movie. It\'s IMDB rating is %.2f.' % x['imdb']
            else:
                print 'That\'s not such a great movie.'
#Write a function that returns a sublist of movies with an imdb score above 5.5.
def overfive_list(movies):
    good_movies = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            good_movies.append(movie['name'])
    print 'Here are some pretty good movies:'
    for m in good_movies:
        print "-" , m

#Write a function that takes a category name and returns just those movies under that category.
def category_list(category, movies):
    cat_list = []
    for movie in movies:
        if movie['category'] == category:
            cat_list.append(movie['name'])
    print 'All of the %r movies are:' % category
    for m in cat_list:
        print '-', m

#Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb(movies):
    imdb_sum = 0
    for movie in movies:
        imdb_sum += movie['imdb']
    average = imdb_sum / (len(movies))
    print 'There are %d movies, and their average IMDB score is %.2f.' % (len(movies), average)

"""This function will take the list 'movies' and a designated category. Given those
it'll loop through the list, and whenever a movie fits the category, it will add
that IMDB value to the value 'imdb_sum', it will also increment the counter by one."""


def avg_genre(movies, genre):
    count = 0
    imdb_sum = 0
    for i in movies:
        if i['category'] == genre:
            imdb_sum += i['imdb']
            count += 1
    average = float(imdb_sum / count)
    print 'The average score for %r movies is %.2f' % (genre, average)
    return
def some_data(genre):
    category_list(genre, movies)
    avg_genre(movies, genre)
def single_data(movie):
    overfivefive(movie)

print 'Welcome to the Movie Info Depository. \n It\'s the one-stop shop for info about your favorite movies. \n Let\'s go!'
choice = raw_input('Are you interested in learning about \'some\' of the movies \'all\' of the movies,\n or just \'one\' of the movies? ')
choices = ['SOME', 'ALL', 'ONE']
def you_choose(choice):
    if choice.upper() not in choices:
        print 'Sorry, that\'s not an option. You can choose \'some\', \'all\', or \'one\'.'
        choice = raw_input('What\'s your choice? ')
    elif choice.upper() == 'ALL':
        print 'Here\'s a list of all our movies.'
        for movie in movies:
            print '-', movie['name']
        overfive_list(movies)
    elif choice.upper() == 'SOME':
        genres = ['Romance', 'Thriller', 'Suspense', 'Comedy', 'Crime', 'War', 'Adventure', 'Action']
        genre = str(raw_input('What Genre are you interested in learning more about? '))
        if genre not in genres:
            print 'That\'s not one of the genres we track. You can choose from Romance, Thriller, \nSuspense, Comedy, Crime, War, Adventure, and Action'
            genre = str(raw_input('What Genre are you interested in learning more about? '))
        else:
            some_data(genre)
    elif choice.upper() == 'ONE':
        single_data(raw_input('What movie do you want to hear about? '))



you_choose(choice)


print 'Enjoy your time at the movies!'
