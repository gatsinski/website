from parler.managers import TranslatableManager


class PostManager(TranslatableManager):

    def published(self, language_code=None):
        return self.filter(is_published=True)
