class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'

comedy = Comedy()
comedy_print_ready = comedy.add_movie('Большой куш')
print(comedy_print_ready)

drama = Drama()
drama_print_ready =drama.add_movie('Оружейный барон')
print(drama_print_ready)