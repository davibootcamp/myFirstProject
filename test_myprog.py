import myprog

def testi_if_it_works():
    assert myprog.neg_c('EEE') == 3
    return True

def testi_if_it_works_with_lower_case_letters():
    assert myprog.neg_c('eee') == 3
    return True
