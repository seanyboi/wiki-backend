
from flask import request
from flask_restplus import Resource
from passfort_demo.api.wiki.business import create_title
from passfort_demo.api.wiki.serializers import titles, titles_with_content, wiki_content
from passfort_demo.api.restplus import api
from passfort_demo.database.models import Titles, Content
from sqlalchemy import desc

ns = api.namespace('wiki/documents', description='Operations related to wiki documents')

# returns all document titles
@ns.route('/')
class TitlesCollection(Resource):

    @api.marshal_list_with(titles)
    def get(self):
        """Returns list of wiki document titles"""
        title = Titles.query.all()
        return title

    #@api.response(201, 'Document successfully created.')
    #@api.expect(titles)
    #def post(self):
        #"""Creates a new wiki document title."""
        #data = request.json
        #create_title(data)
        #return None, 201

# Returns versions of documents for a particular title
@ns.route('/<string:title>')
@api.response(404, 'Documents not found.')
class TitlesItem(Resource):
    """Returns list of documentation for a particular title"""
    @api.marshal_with(titles_with_content)
    def get(self, title):
        self.title = title
        """Returns a title with a the different content versions"""
        return Titles.query.filter(Titles.name == title).one()

# Returns the latest version of document given a title
@ns.route('/<string:title>/latest')
@api.response(404, 'Documents not found.')
class TitlesItem(Resource):
    """Returns the latest documentation for a particular title"""
    @api.marshal_with(wiki_content)
    def get(self, title):
        self.title = title
        titles_id = Titles.query.filter(Titles.name == title).one()
        id = titles_id.id
        """Returns a title with a the different content versions"""
        return Content.query.filter(Content.titles_id == id).order_by(desc(Content.pub_date)).first()


# Ran out of time. Could only get it matching a particular hour.
# Need to include date as well.
@ns.route('/<string:title>/<int:timestamp>/')
class TitleArchiveCollection(Resource):

    @api.marshal_with(wiki_content)
    def get(self, title, timestamp):
        """Returns wiki document from a specified hour."""
        self.title = title
        self.timestamp = timestamp
        titles_id = Titles.query.filter(Titles.name == title).one()
        id = titles_id.id

        content = Content.query.filter(Content.titles_id == id)
        content_query = []
        for x in content:
            if (x.pub_date.hour == timestamp):
                content_query.append(x)

        return content_query
