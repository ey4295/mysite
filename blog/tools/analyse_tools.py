"""
This is a collection of tools to conduct ner analysis
"""
import random

import ner
import nltk
from nltk import word_tokenize


########################################################################################################
# Named Entity Recognition tools
#
########################################################################################################
def get_tokens(sent):
    """
    tokenize sent to get tokens
    :param sent:
    :return: list of tokens
    """
    return word_tokenize(sent)


def get_pos(sent):
    """
    get part of speech tag
    :return: list of tags
    """
    tokens = get_tokens(sent)
    return [tag for (token, tag) in nltk.pos_tag(tokens)]


def get_entities(sent):
    """
    get Named Entities
    :param sent:
    :return:
    """
    tagger = ner.SocketNER(host='localhost', port=4295, output_format='slashTags')
    tags = set(['PERSON', 'LOCATION', 'ORGANIZATION', 'DATE'])
    entities={}
    # get verb
    pos_tags = nltk.pos_tag(word_tokenize(sent))
    tag = ''
    VBS = []
    for pos in pos_tags:
        if nltk.re.match('VB.*', pos[1]):
            if not tag == '':
                tag = tag + ' ' + pos[0]
            else:
                tag += pos[0]
        elif not tag == '':
            VBS.append(tag)
            tag = ''
    l = len(VBS)
    new_VBS = []
    count = random.randint(1, 3)
    if count > l:
        count = l
    indices = random.sample(range(count), count)
    for index in indices:
        new_VBS.append(VBS[index])
    entities['VB']='|'.join(new_VBS)

    # get entities
    crf_entities = tagger.get_entities(sent)
    for (key, val) in crf_entities.items():
        if key in tags:
            # trick for special form stanford ner generate
            val = nltk.re.search('<{}>(.*?)<'.format(key), val[0]).group(1)
            entities[key]=val
    return entities

########################################################################################################
#  Sentiment Analysis tools
#
########################################################################################################
