from model import seq2seq
import tensorflow as tf
import re,json
from data_process import *

if __name__ == "__main__":
    PATH = "models"
    sess = tf.Session()
    with open('vocab.json', 'r') as fp:
        vocab = json.load(fp)
    reverse_vocab = dict()
    for key, value in vocab.items():
        reverse_vocab[value] = key
    vocab_size = len(vocab)
    model = seq2seq(sess, encoder_vocab_size=vocab_size, decoder_vocab_size=vocab_size, max_step=50)
    saver = tf.train.Saver()
    saver.restore(sess, tf.train.latest_checkpoint(PATH))

    while True:
        test = input("User >> ")
        if test == "exit":
            break
        speak = sentence_to_char_index([test], vocab, False)
        result = model.inference([speak])
        for sentence in result:
            response = ''
            for index in sentence:
                if index == 0:
                    break
                response += reverse_vocab[index]
            print("Bot >> ", response, "\n")
