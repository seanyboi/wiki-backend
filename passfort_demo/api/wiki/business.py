from passfort_demo.database import db
from passfort_demo.database.models import Content, Titles


# Used for posting requests up to the contents database
def create_wiki_content(data):
    body = data.get('body')
    title_name = data.get('titles')
    titles = Titles.query.filter(Titles.name == title_name).one()
    content = Content(body, titles)
    db.session.add(content)
    db.session.commit()

# Used for posting up titles to the titles database
def create_title(data):
    name = data.get('name')
    title_id = data.get('id')

    title = Titles(name)
    if title_id:
        title.id = title_id

    db.session.add(title)
    db.session.commit()
