from flask_restplus import fields
from passfort_demo.api.restplus import api

# this json is what we wish to be posted to content endpoints
wiki_content = api.model('Wiki content', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a wiki content'),
    'body': fields.String(required=True, description='Article content'),
    'pub_date': fields.DateTime,
    'title_id': fields.Integer(attribute='titles.id'),
    'titles': fields.String(attribute='titles.name'),
})

# this json is what we wish to be posted to titles endpoints
titles = api.model('Wiki Document Titles', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a wiki document title'),
    'name': fields.String(required=True, description='Title of document'),
})

# inheritance must be the same as the database models relationships reference
titles_with_content = api.inherit('Document title with content', titles, {
    'content': fields.List(fields.Nested(wiki_content))
})
