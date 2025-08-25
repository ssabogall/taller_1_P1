
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from collections import Counter
import matplotlib.pyplot as plt
import io
import urllib, base64

def home(request):
    q = request.GET.get('searchMovie', '') or ''
    movies = Movie.objects.filter(title__icontains=q) if q else Movie.objects.all()
    return render(request, "home.html", {"movies": movies, "searchTerm": q})

def about (request):
    return render(request, 'about.html', { 'name': 'Santiago Sabogal Lozano' })


def _plot_to_base64(labels, values, title, xlabel):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(range(len(labels)), values, align="center")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Number of movies")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=90 if len(labels) > 8 else 0, ha="right")
    fig.tight_layout()

    buffer = io.BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close(fig)

    png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(png).decode("utf-8")


def statistics_view(request):
    # 1) Conteo por año (igual a tu lógica, pero con Counter)
    all_movies = Movie.objects.all()
    years = [m.year if m.year else "None" for m in all_movies]
    by_year = Counter(years)

    # Ordena años numéricamente y deja "None" al final
    def _year_key(y):
        return (1, 0) if y == "None" else (0, int(y))
    year_labels = sorted(by_year.keys(), key=_year_key)
    year_values = [by_year[y] for y in year_labels]
    graphic_year = _plot_to_base64(year_labels, year_values, "Movies per year", "Year")

    # 2) Conteo por género (nuevo)
    # Si un registro tiene varios géneros separados por coma, se cuentan por separado.
    genres = []
    for m in all_movies:
        if m.genre:
            parts = [p.strip() for p in str(m.genre).split(",") if p.strip()]
            genres.extend(parts if parts else ["None"])
        else:
            genres.append("None")

    by_genre = Counter(genres)
    # Ordena por cantidad (desc) y nombre (asc) para que se vea bonito
    genre_items = sorted(by_genre.items(), key=lambda kv: (-kv[1], kv[0]))
    genre_labels = [k for k, _ in genre_items]
    genre_values = [v for _, v in genre_items]
    graphic_genre = _plot_to_base64(genre_labels, genre_values, "Movies per genre", "Genre")

    return render(
        request,
        "statistics.html",
        {"graphic_year": graphic_year, "graphic_genre": graphic_genre},
    )
