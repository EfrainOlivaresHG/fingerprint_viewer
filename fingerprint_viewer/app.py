from flask import Flask
from flask import render_template
import retina_viewer as rv
import json
app = Flask(__name__)

conf = {
    "map_path_file": "word2vec/urls_62k_new_good_ones_0.wdc",
    "map_path_loc_file": "word2vec/urls_62k_new_good_ones_0.ldc",
    "model": "",
    "text_corpus": "data/random_1000_urls.tsv"
}

word_dict = rv.load_word_location_dict_from_file(conf["map_path_file"])
word_vectors = rv.load_location_words_dict_from_file(conf["map_path_loc_file"])
retina = rv.Retina(['aws'], word_dict, word_vectors, None)

@app.route('/')
def bubble():
    with open(conf["text_corpus"],'r') as source:
        url_list = [line.split('\t')[0].strip() for line in source]
    return render_template('bubble_basic.html', url_list=url_list)

@app.route('/fprint')
def fprint():
    with open(conf["text_corpus"], 'r') as source:
        url_list = [line.split('\t')[0].strip() for line in source]
    return render_template('view_single_fingerprint.html',
        tab_title="TAB",
        page_title="Single Fingerprint View",
        graph_size="64",
        graph_x_px="600",
        graph_y_px="680",
        url_list=url_list)



@app.route('/getretina/<urlname>', methods=['GET', 'POST'])
def get_retina(urlname):
    print "Looking for {}".format(urlname) 
    text = ['aws']
    with open(conf["text_corpus"], 'r') as source:
        for line in source:
            cols = line.split('\t')
            binary = cols[2].strip()
            url = cols[0].strip()
            text = [word for word in cols[1].strip().split()]
            if url == urlname:
                print "FOUND IT!"
                break

    tups = retina.fingerprint(text,0)
    data = []
    for tup in tups:
        data.append({ "x": tup[0], "y": tup[1] })
    jdatas = json.dumps(data)
    return jdatas

if __name__ == '__main__':
  app.run('0.0.0.0', 8080)
