import json

from utils.vocab import Vocab, LabelVocab
from utils.word2vec import Word2vecUtils
from utils.evaluator import Evaluator

class Example():

    @classmethod
    def configuration(cls, root, train_path=None, word2vec_path=None):
        cls.evaluator = Evaluator()
        cls.word_vocab = Vocab(padding=True, unk=True, filepath=train_path)
        cls.word2vec = Word2vecUtils(word2vec_path)
        cls.label_vocab = LabelVocab(root)

    @classmethod
    def load_dataset(cls, data_path):
        datas = json.load(open(data_path, 'r',encoding='utf-8'))
        exs = []
        for di, data in enumerate(datas):
            for ui, utt in enumerate(data):
                ex = cls(utt, f'{di}-{ui}')
                if ex.ex["utt_id"] == 1:
                    ex.skip_len = 0
                else:
                    pre_ex = exs[-1]
                    ex.utt = pre_ex.utt + ex.utt
                    ex.input_idx = pre_ex.input_idx + ex.input_idx
                    ex.tags = pre_ex.tags + ex.tags
                    ex.tag_id = pre_ex.tag_id + ex.tag_id
                    ex.skip_len = len(pre_ex.utt)
                exs.append(ex)
        return exs

    def __init__(self, ex: dict,did):
        super(Example, self).__init__()
        self.ex = ex
        self.did = did
        self.utt = ex['asr_1best']

        self.slot = {}
        if 'semantic' in ex:
            for label in ex['semantic']:
                act_slot = f'{label[0]}-{label[1]}'
                if len(label) == 3:
                    self.slot[act_slot] = label[2]
        self.tags = ['O'] * len(self.utt)
        for slot in self.slot:
            value = self.slot[slot]
            bidx = self.utt.find(value)
            if bidx != -1:
                self.tags[bidx: bidx + len(value)] = [f'I-{slot}'] * len(value)
                self.tags[bidx] = f'B-{slot}'
        self.slotvalue = [f'{slot}-{value}' for slot, value in self.slot.items()]
        self.input_idx = [Example.word_vocab[c] for c in self.utt]
        l = Example.label_vocab
        self.tag_id = [l.convert_tag_to_idx(tag) for tag in self.tags]
