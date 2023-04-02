from typing import List
import pytest
from my_module import NewTrainer


class TestNewTrainer:
    @pytest.fixture
    def trainer(self):
        return NewTrainer()

    def test_train(self, trainer):
        X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y = [10, 20, 30]
        trainer.train(X, y)
        # add assertion to test the expected behavior of train()

    def test_predict(self, trainer):
        X = [1, 2, 3]
        prediction = trainer.predict(X)
        # add assertion to test the expected behavior of predict()