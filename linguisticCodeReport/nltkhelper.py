from nltk import pos_tag
import linguisticCodeReport.listhelper as lh

__NLTK_PART_OF_SPEECH__ = {'verb': {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}, 'noun': {'NN', 'NNS', 'NNP', 'NNPS'}}


def get_available_parts():
    return __NLTK_PART_OF_SPEECH__.keys()


def is_speech_part(word, speach_part):
    if not word:
        return False
    pos_info = pos_tag([word])
    nltk_verbs = __NLTK_PART_OF_SPEECH__.get(speach_part)
    return nltk_verbs.__contains__(pos_info[0][1])


def get_speech_part_from_text(text, speech_part):
    return [word for word in text.split('_') if is_speech_part(word, speech_part)]


def get_speech_parts_from_texts(texts, speech_parts):
    sp = []
    for text in texts:
        for speech_part in speech_parts:
            sp.append(get_speech_part_from_text(text, speech_part))
    return lh.flat(sp)


if __name__ == '__main__':
    print(__NLTK_PART_OF_SPEECH__.keys())
    for ke in get_available_parts():
        print(ke)
