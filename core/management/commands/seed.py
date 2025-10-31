from django.core.management.base import BaseCommand
from categories.models import Category
from authors.models import Author
from posts.models import Post

class Command(BaseCommand):
    help = "Carga datos de ejemplo iniciales"

    def handle(self, *args, **options):
        # Categorías
        Category.objects.get_or_create(name="Tecnología")
        Category.objects.get_or_create(name="Ciencia")
        Category.objects.get_or_create(name="Arte")

        # Autores
        Author.objects.get_or_create(name="Matías", email="matias@example.com")
        Author.objects.get_or_create(name="Edgar", email="edgar@example.com")

        # Posts
        Post.objects.get_or_create(
            title="Primer Post",
            content="Este es el primer post de prueba.",
            author=Author.objects.first(),
            category=Category.objects.first(),
        )

        self.stdout.write(self.style.SUCCESS('✅ Datos iniciales cargados correctamente'))
