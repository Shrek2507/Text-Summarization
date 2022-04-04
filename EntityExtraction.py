import spacy
import traceback
from nltk.corpus import words

class ExtractEntities(object):
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.words_list = list(words.words())

    def generate_entities(self, summarized_news):
        """

        :type summarized_news: str
        """
        try:
            # Create a summarized article doc...
            summarized_news_doc = self.nlp(summarized_news)

            # Extract specific labels for reference tagging....
            specific_reference_tags = ['PERSON', 'ORG', 'PRODUCT', 'GPE', 'LOC', 'MONEY']

            # Creating a dictionary of tags...
            tags_dict = {}

            tags_dict['ORG'] = 'Organisation'
            tags_dict['PERSON'] = 'Person'
            tags_dict['GPE'] = 'Location'
            tags_dict['MONEY'] = 'Monetary Value'
            tags_dict['PRODUCT'] = 'Product'
            tags_dict['LOC'] = 'Location'

            # create entity details...
            entity_details = list(summarized_news_doc.ents)
            filtered_entities = []
            entity_labels = []

            # Iterating through the entities...
            for entity in entity_details:
                if entity.label_ in specific_reference_tags:
                    # get the tag value...
                    tag_value = tags_dict[str(entity.label_)]
                    # append the entities and their tags to the list...
                    filtered_entities.append(str(entity))
                    entity_labels.append(tag_value)

            filtered_entities = ','.join(filtered_entities)
            entity_labels = ','.join(entity_labels)

            filtered_entities = filtered_entities+';'+entity_labels

            return filtered_entities

        except Exception as e:
            print(traceback.format_exc())

