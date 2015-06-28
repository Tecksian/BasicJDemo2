__author__ = 'Austin'

from google.appengine.ext import ndb

class Concept(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.StringProperty()

class ConceptPage(ndb.Model):
    title = ndb.StringProperty()
    #using repeated=True makes it behave like a list....BUT
    #BEWARE -- you can only have one non-LocalStructuredProperty set to repeated=True!
    comments=ndb.StringProperty(repeated=True)
    #use LcalStructuredProperty for now -- will explain later
    concepts = ndb.LocalStructuredProperty(Concept, repeated=True)

    #create a method to add a concept
    def add_concept(self, arg_title='', arg_description=''):
        new_concept = Concept(name=arg_title, description=arg_description)
        self.concepts.append(new_concept)

    #a method to populate initial data so we don't have to comment/uncomment things all the time!
    def create_seed_data(self):
        self.title='Intro to Programming'
        self.concepts = [Concept(name='Topic 1', description='Description of topic 1'),
                         Concept(name='Topic 2', description='Description of topic 2'),
                         Concept(name='Topic 3', description='Description of topic 3'),
                         Concept(name='Topic 4', description='Description of topic 4')]
        self.put()

    #create a method to add a comment
    def add_comment(self,new_comment):
        self.comments.append(new_comment)
