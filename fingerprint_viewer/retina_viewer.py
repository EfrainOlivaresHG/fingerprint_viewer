"""
Reconstruct a retina from computed map files.  These files are the post
minisom training files.  One file should contain a 1:1 word:location mapping,
The other file should contain the most common words word:[xy, xy, xy...]
"""


def load_word_location_dict_from_file(map_path_file):
    word_location_dict = {}
    with open(map_path_file, 'r') as source:
        for line in source:
            elems = line.split('\t')
            word = elems[0].strip()
            tup = eval(elems[1].strip())
            word_location_dict[word] = tup
    return word_location_dict


def load_location_words_dict_from_file(map_path_loc_file):
    location_words_dict = {}
    with open(map_path_loc_file, 'r') as source:
        for line in source:
            elems = line.split('\t')
            tup = eval(elems[0].strip())
            words = elems[1].strip().split(' ')
            location_words_dict[tup] = words
    return location_words_dict


class Retina:
    def __init__(self, _unique_words, _word_location_dict, _word_vectors, _model):
        self.unique_words = _unique_words
        self.word_loc = _word_location_dict
        self.word_vectors = _word_vectors
        self.model = _model

         
    def location(self, word):
        return self.word_loc[word]

    def fingerprint(self, item, density=20):
        if type(item) == type('word'):
            try:
                fingerprint = [self.location(item)]
            except:
                return []
            if density == 0:
                return fingerprint
            similar_words = self.model.most_similar(positive=[item], negative=[], topn=density)
            [fingerprint.append(self.location(tup[0])) for tup in similar_words]
            return fingerprint
        elif type(item) == type([]):
            tups = []
            for word in item:
                for tup in self.fingerprint(word, density):
                    tups.append(tup)

            return tups
            

    def fingerprint_x_y(self, word, density=20):
        xarr = []
        yarr = []
        for tup in self.fingerprint(word, density):
            xarr.append(tup[0])
            yarr.append(tup[1])

        return (xarr, yarr)
    
    def document_fingerprint_x_y(self, word_list, density=20):
        fingerprints = []
        for word in word_list:
            fingerprints.append(self.fingerprint(self, word, density))

