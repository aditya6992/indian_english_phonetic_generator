# indian_english_phonetic_generator
This project uses letter to sound rules to generate indian english phonemes from a word, which can be used for speech recognition and speech synthesis. It is implemented in python 2.7

It is based on the following paper:
[Pronounciation rules for Indian English Text-to-Speech system](speech.tifr.res.in/workshop/03wslp/proceedings/p21.doc)

The script uses the phonetic set which is used in CMU Sphinx and CMU's phonetic dictionary.

The accuracy is around 75% for english words in general, and around 85 to 90% for new indian words and nouns that anyone might want to add to their dictionary for speech recognition/synthesis. The data set that I tested was very limited and the letter to sound rules that are implemented are imperfect (they are based on 'most likely' approach) as opposed to LSTM (Long Sort Term Memory) networks used by g2p-seq2seq type programs which give near perfect results, however these require an existing dictionary of a considerable size to train, but there aren't many phonetic dictionaries available for indian english. Regardless, this might be of some help if anyone wants to build a dictionary from scratch. Please note that these rules are specific for english in indian accent.

To run this in interactive mode:
```python g2p_indian.py```

