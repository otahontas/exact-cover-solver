import pytest
from exact_cover_solver.data_creators import DataCreator


def test_not_possible_to_call_constrain_creating_without_real_implementation():
    class FakeDataCreator(DataCreator):
        def create_constrains(self):
            super(FakeDataCreator, self).create_constrains()

    with pytest.raises(NotImplementedError):
        creator = FakeDataCreator()
        creator.create_constrains()
