# Below the list of movies is a function that will print the average of a given genre.

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
"""Potentially add a space for user to input the category they're interested in?
This function will take the list 'movies' and a designated category. Given those
it'll loop through the list, and whenever a movie fits teh category, it will add
that IMDB value to the value 'imdb_sum', it will also increment the counter by one."""

genres = ['Romance', 'Thriller', 'Suspense', 'Comedy', 'Crime', 'War', 'Adventure', 'Action']
genre = str(raw_input('What Genre are you interested in learning the average of? '))

if genre not in genres:
    print 'That\'s not one of the genres we track. You can choose from Romance, Thriller, \nSuspense, Comedy, Crime, War, Adventure, and Action'
    genre = str(raw_input('What Genre are you interested in learning the average of? ')).title()

def avg_genre(movies, genre):
    count = 0
    imdb_sum = 0
    for i in movies:
        if i['category'] == genre:
            imdb_sum += i['imdb']
            count += 1
    average = float(imdb_sum / count)
    print 'The average score for %r is %.2f' % (genre, average)
    return

avg_genre(movies, genre)

print 'Enjoy your time at the movies!'
