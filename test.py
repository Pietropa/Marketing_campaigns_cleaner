import pytest
from cleaning import run


def test_cleaning_works1():
    run(df)
    assert(df_final['Total_Conversion'].dtype == 'int64')

def test_cleaning_works2():
    run(df)
    assert(df_final['age_n'].dtype == 'int64')