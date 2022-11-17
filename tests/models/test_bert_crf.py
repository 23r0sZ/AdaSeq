import os
import unittest

from modelscope.trainers import build_trainer
from tests.models.base import TestModel, compare_fn

from adaseq.metainfo import Trainers


class TestBertCRF(TestModel):

    def test_bert_crf(self):
        cfg_file = os.path.join('tests', 'resources', 'configs', 'train_bert_crf.yaml')
        trainer = build_trainer(Trainers.ner_trainer, default_args={'cfg_file': cfg_file, 'seed': 42})

        with self.regress_tool.monitor_ms_train(
                trainer,
                'ut_bert_crf',
                level='strict',
                compare_fn=compare_fn,
                # Ignore the calculation gap of cpu & gpu
                atol=1e-3):
            trainer.train()


if __name__ == '__main__':
    unittest.main()
