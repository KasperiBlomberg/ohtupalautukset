from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And

class QueryBuilder:
    def __init__(self, query=All()):
        self.build_query = query

    def plays_in(self, team):
        return QueryBuilder(And(self.build_query, PlaysIn(team)))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.build_query, HasAtLeast(value, attr)))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.build_query, HasFewerThan(value, attr)))

    def build(self):
        return self.build_query
    
    