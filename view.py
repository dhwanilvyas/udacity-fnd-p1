import webbrowser, os.path

# The main container content
viewContent = '''
<!DOCTYPE html>
<html>
    <title>Favourite Movies</title>
    <head>
        <link rel="stylesheet" href="https://bootswatch.com/flatly/bootstrap.min.css">
        <link rel="stylesheet" href="./style.css">
        <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
        <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
        <script src="./scripts.js"></script>
    </head>
    <body>
        <div class="padding-top-container"></div>
        <div class="container">
            {movie_tiles}
        </div>
    </body>
</html>
'''

# A single movie tile
movieTile = '''
<div class="col-md-3 movie_tile" data-movie-id="{id}">
    <div class="panel panel-default">
        <div class="panel-body">
            <img src={poster_path} class="img-responsive" />
            <h5 class="movie-title">{title}</h5>
        </div>
    </div>
</div>
'''

# Creates a file by the name given in parameter and
# writes the content in it
def strToFile(text, filename):
    output = open(filename, "w")
    output.write(text)
    output.close()

# Generates an array of movie tiles
def generateTiles(movies):
    content = ''

    for movie in movies:
        content += movieTile.format(
            title = movie.title,
            poster_path = "http://image.tmdb.org/t/p/w300" + movie.poster_path,
            id = movie.id
        )

    return content

# Opens the browser with the webpage 
# after the content has been rendered to the file
def generateOutput(content, movies, filename='list.html'):

    rendered_content = content.format(
        movie_tiles = generateTiles(movies)
    )

    strToFile(rendered_content, filename)

    # open the output file in the browser
    webbrowser.open("file:///" + os.path.abspath(filename))

# Calls the generateOutput function to generate HTML file
# with the movies received as param from index file
def main(movies):
    generateOutput(viewContent, movies)
