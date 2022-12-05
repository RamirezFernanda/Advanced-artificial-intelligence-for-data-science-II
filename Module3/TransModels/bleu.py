from nltk.translate.bleu_score import sentence_bleu


def split_dataset(dataset):
    original_dataset = open(dataset, 'r')
    splited_dataset = original_dataset.read()
    splited_dataset = splited_dataset.split()
    return splited_dataset


def bleu_score():
    original_dataset = split_dataset('./DataSets/europarl-v7.es-en.en')
    google_traduction = split_dataset('./DataSets/google_traduction.txt')
    deepl_traduction = split_dataset('./DataSets/deepl_traduction.txt')

    print('BLEU score for GoogleAPI-> {}'.format(
        sentence_bleu(google_traduction, original_dataset)))
    print('BLEU score for DeeplAPI-> {}'.format(
        sentence_bleu(deepl_traduction, original_dataset)))


bleu_score()
