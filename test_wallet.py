import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    return Wallet(0)

@pytest.fixture
def wallet():
    return Wallet(20)


def test_default_initial_amount(empty_wallet):

    assert wallet.balance == 0

def test_setting_initial_amount(wallet):

    assert wallet.balance == 20

def test_wallet_add_cash(wallet):

    wallet.add_cash(90)
    assert wallet.balance == 110

def test_wallet_spend_cash(wallet):

    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):

     with pytest.raises(InsufficientAmount):
            wallet.spend_cash(100)