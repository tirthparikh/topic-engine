import nltk


class Engine:
    """Engine Object analyzes Relevant topic from the given list of strings"""

    def __init__(self, list_of_docs):
        self.documents = list_of_docs
        self.term_frequencies = {}
        self.unique_term_list = set()
        self.total_terms = 0

    def find_list_of_terms(self):
        """This method will calculate the total list of uniquely identified terms"""
        # Tokenizing into different sentences
        sentences = []
        for doc in self.documents:
            sentences.extend(nltk.tokenize.sent_tokenize(doc.strip()))

        # Tokenizing each sentence into words
        tokens = []
        for s in sentences:
            tokens.extend(nltk.tokenize.word_tokenize(s))

        # POS_TAG the tokens
        # This function judges the tokes as Nouns, Verb, Adjectives etc
        pos_tagged_tokens = nltk.pos_tag(tokens)

        return pos_tagged_tokens

    ##

    def top_n_terms(self, n):
        pos_tagged_tokens = self.find_list_of_terms()
        all_entity_chunks = []
        previous_pos = None
        current_entity_chunk = []

        for token, pos in pos_tagged_tokens:
            if pos == previous_pos and (pos.startswith('NNP') or pos.startswith('JJ')):
                # Included the Noun and Adjective
                current_entity_chunk.append(token)
            elif pos.startswith('NNP') or pos.startswith('JJ'):
                if current_entity_chunk:
                    all_entity_chunks.append((' '.join(current_entity_chunk), pos))
                current_entity_chunk = [token]
            previous_pos = pos

        entities = {}
        for c in all_entity_chunks:
            entities[c] = entities.get(c, 0) + 1

        self.term_frequencies = entities

        entities = sorted(entities.items(), key=lambda x: x[1])

        result = []
        for q in entities:
            result.append(q[0])

        result = [r[0] for r in result]
        return result[-n:]

