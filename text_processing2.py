#######################
# Test Processing II  #
#######################
def digits_to_words(input_string: str) -> str:
    mapping = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']
    numbers = []
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            numbers.append(mapping[int(input_string[i])])
    digit_string = ' '.join(numbers)
    return digit_string


"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    if '_' not in underscore_str:
        return underscore_str
    else:
        words = underscore_str.lower().split('_')
        camelcase_str = ''.join([word.capitalize() for word in words])
        if len(camelcase_str) > 0:
            edit = list(camelcase_str)
            edit[0] = edit[0].lower()
            camelcase_str = ''.join(edit)
        return camelcase_str
