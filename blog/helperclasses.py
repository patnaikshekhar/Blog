from calendar import month_name

class ArchiveItem:

    def __init__(self, article):
        self.year = article.date.year
        self.month = article.date.month
        self.display = month_name[article.date.month] + ' ' + str(article.date.year)
        self.key = int(str(article.date.year) + str(article.date.month))
        self.articles = []
        self.articles.append(article)

class Archive:

    def __init__(self):
        self.items = []

    def add(self, article):
        key = int(str(article.date.year) + str(article.date.month))
        for item in self.items:
            if item.key == key:
                item.articles.append(article)
                return

        item = ArchiveItem(article)
        self.items.append(item)

    def sort(self):
        self.items = sorted(self.items, key=lambda x: x.key, reverse=True)
