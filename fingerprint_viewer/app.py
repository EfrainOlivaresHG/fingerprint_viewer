from flask import Flask
from flask import render_template
import retina_viewer as rv
import json
app = Flask(__name__)

conf = {
    "map_path_file": "word2vec/urls_62k_new_good_ones_0.wdc",
    "map_path_loc_file": "word2vec/urls_62k_new_good_ones_0.ldc",
    "model": ""
}
@app.route('/')
def hello():
    return render_template('line_basic.html')

@app.route('/bubble')
def bubble():
    return render_template('bubble_basic.html')

@app.route('/getretina', methods=['GET', 'POST'])
def get_retina():
    print "WE ARE IN" 
    import os
    word_dict = rv.load_word_location_dict_from_file(conf["map_path_file"])
    word_vectors = rv.load_location_words_dict_from_file(conf["map_path_loc_file"])
    retina = rv.Retina(['aws'], word_dict, word_vectors, None)
    tups = retina.fingerprint(['aws', 'azure'],0)
    data = []
    for tup in tups:
        data.append({ "x": tup[0], "y": tup[1] })
    jdatas = json.dumps(data)
    print jdatas
    return jdatas

if __name__ == '__main__':
  app.run('0.0.0.0', 8080)
