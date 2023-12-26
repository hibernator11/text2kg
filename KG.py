import wikipedia
from SPARQLWrapper import SPARQLWrapper, JSON


class KG():
    def __init__(self):
        self.relations = []
        self.entities = {}

    def are_relations_equal(self, r1, r2):
        return all(r1[attr] == r2[attr] for attr in ["head", "type", "tail"])

    def exists_relation(self, r1):
        return any(self.are_relations_equal(r1, r2) for r2 in self.relations)
            
    def merge_relations(self, r1):
        r2 = [r for r in self.relations
              if self.are_relations_equal(r1, r)][0]
        
        if "meta" in r1:
            spans_to_add = [span for span in r1["meta"]["spans"]
                           if span not in r2["meta"]["spans"]]
            r2["meta"]["spans"] += spans_to_add       
            
    def get_wikipedia_data(self, candidate_entity):
        try:
            page = wikipedia.page(candidate_entity, auto_suggest=False)
            entity_data = {
                "title": page.title,
                "url": page.url,
                "summary": page.summary,
                "idWikidata": self.get_wikidata_entity(page.url)
            }
            return entity_data
        except:
            return None
        
    def get_wikidata_entity(self, wikipedia_url):
        
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setReturnFormat(JSON)
        
        try:
            
            query = """
            SELECT ?item
            WHERE {{   
                <{}> schema:about ?item
            }} LIMIT 1
            """.format(wikipedia_url)
            
            print(query)
            
            sparql.setQuery(query)
            results = sparql.queryAndConvert()['results']['bindings']
            
            idWikidata = ''
            for result in results:
                idWikidata = result['item']['value']
                break
            
            return idWikidata
        except:
            return None

    def add_entity(self, e):
        self.entities[e["title"]] = {k:v for k,v in e.items() if k != "title"}

    def add_relation(self, r):
        # check on wikipedia
        candidate_entities = [r["head"], r["tail"]]
        entities = [self.get_wikipedia_data(ent) for ent in candidate_entities]

        # if one entity does not exist, stop
        if any(ent is None for ent in entities):
            return

        # manage new entities
        for e in entities:
            self.add_entity(e)

        # rename relation entities with their wikipedia titles
        r["head"] = entities[0]["title"]
        r["tail"] = entities[1]["title"]

        # manage new relation
        if not self.exists_relation(r):
            self.relations.append(r)
        else:
            self.merge_relations(r)

    def print(self):
        print("Entities:" + str(len(self.entities)))
        for e in self.entities.items():
            print(f"  {e}")
        print("Relations:" + str(len(self.relations)))
        for r in self.relations:
            print(f"  {r}")
        print("total Entities:" + str(len(self.entities)))
        print("total Relations:" + str(len(self.relations)))

    # def save_model(self, text_file):
    #     with open('kb_'+ text_file+'.pickle', 'wb') as f:
    #         pickle.dump(self, f)
            
    # def load_model(self, text_file):
    #     self = pickle.load('kb_'+ text_file+'.pickle')          