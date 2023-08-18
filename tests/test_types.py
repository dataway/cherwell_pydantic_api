import pytest

import pydantic
from cherwell_pydantic_api.types import *



def test_IDType():
    assert BusObID('1234567890aBcDeF1234567890AbCdEf') == '1234567890abcdef1234567890abcdef'
    with pytest.raises(ValueError):
        BusObID('1234567890aBcDeF1234567890AbCdEfG')
    with pytest.raises(ValueError):
        BusObID('')
    assert isinstance(BusObID('1234567890aBcDeF1234567890AbCdEf'), str)


def test_IdentifierType():
    assert FieldIdentifier('abc123') == 'abc123'
    assert FieldIdentifier('abc_123') == 'abc_123'
    assert FieldIdentifier('abc-123') == 'abc_123'
    assert FieldIdentifier('abc 123') == 'abc_123'
    assert FieldIdentifier('abc.123') == 'abc_123'
    assert FieldIdentifier('import') == 'I_import'
    assert FieldIdentifier('123') == 'I_123'
    assert FieldIdentifier('123abc') == 'I_123abc'
    assert FieldIdentifier('_abc') == 'I__abc'


def test_LCIdentifierType():
    assert BusObIdentifier('aBC123') == 'abc123'
    assert BusObIdentifier('aBC_123') == 'abc_123'
    assert BusObIdentifier('ABc-123') == 'abc_123'
    assert BusObIdentifier('aBC 123') == 'abc_123'
    assert BusObIdentifier('aBC.123') == 'abc_123'
    assert BusObIdentifier('Import') == 'I_import'
    assert BusObIdentifier('123') == 'I_123'
    assert BusObIdentifier('123aBC') == 'I_123abc'
    assert BusObIdentifier('_aBC') == 'I__abc'


def test_pydantic():
    class TestModel(pydantic.BaseModel):
        busobid: BusObID
        busobrecid: Optional[BusObRecID]
        fieldidentifier: FieldIdentifier
        busobidentifier: BusObIdentifier

    t1 = TestModel(busobid='1234567890aBcDeF1234567890AbCdEf', busobrecid=None,
                   fieldidentifier='abc123', busobidentifier='aBC123')
    assert t1.busobid == '1234567890abcdef1234567890abcdef'
    assert t1.busobrecid is None
    assert t1.fieldidentifier == 'abc123'
    assert t1.busobidentifier == 'abc123'

    with pytest.raises(pydantic.ValidationError) as exc_info:
        TestModel(busobid='1234567890aBcDeF1234567890AbCdEfG', busobrecid=None,
                   fieldidentifier='abc123', busobidentifier='aBC123')
    assert exc_info.value.errors() == [{
            'input': '1234567890aBcDeF1234567890AbCdEfG',
            'loc': ('busobid',),
            'type': 'cherwell_api_idtype',
            'msg': 'invalid IDType'
        }]
