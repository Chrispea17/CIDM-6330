
class Converter_Roman_Numeral:
    def __init__(self, num):
        self.num = str(num)
        self.numerals = ['', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
        self.placevaluelist = [{'I': 1, 'V': 5, 'X': 10}, {
            'X': 10, 'L': 50, 'C': 100}, {'C': 100, 'D': 500, 'M': 1000}, {'M': 1000}]
        self.placevaluelist2 = [['I', 'V', 'X'], [
            'X', 'L', 'C'], ['C', 'D', 'M'], ['M']]
        self.numbers = [0, 1, 5, 10, 50, 100, 500, 1000]
        self.tolist = [x for x in self.num]

    # def tolist(self): moved to attribute
    #     return [x for x in self.num]

    def intersect(self):
        set_numerals = set(self.numerals)
        return set_numerals.intersection(self.num)

    def retrieve_placevalue(self):
        place_value_list_equivalent = [
            self.placevaluelist2[j] for j in range(len(self.tolist)-1, -1, -1)]
        return place_value_list_equivalent

    def converter(self):
        list_equivalent = self.retrieve_placevalue()
        components_list = []
        if self.intersect() == set():
            for x in range(len(self.tolist)):
                p = int(self.tolist[x])
                t = list_equivalent[x]
                if p in [1, 2, 3, 5, 6, 7, 8]:
                    if p >= 5:
                        components_list.append(t[1] + t[0]*(int(p) % 5))
                    else:
                        components_list.append(t[0]*(int(p) % 5))
                elif p == 4:
                    components_list.append(t[0] + t[1])
                elif p == 9:
                    components_list.append(t[0] + t[2])
            numeral = "".join(components_list)
        else:
            for x in range(len(self.tolist)):
                components_list.append(
                    self.numbers[self.numerals.index(self.tolist[x])])
                if x > 0 and components_list[x] > components_list[x-1]:
                    components_list[x-1] = -components_list[x-1]
            numeral = sum(components_list)
        return numeral


# # system test (if this works we are in a good place for the first part)
# def test_convert_to_roman_numerals():
#     number = Number("129")
#     Number.convert(number)

# AAssertions

def test_number_to_list():
    test_number = Converter_Roman_Numeral(4)
    assert test_number.tolist == ["4"]


def test_numeral_to_list():  # combined this built item with placevalue find instead of
    test_numeral = Converter_Roman_Numeral("XV")
    assert test_numeral.tolist == ["X", "V"]


def test_roman_group_placevalue():
    test_placevalue = Converter_Roman_Numeral(2)
    assert test_placevalue.retrieve_placevalue(
    ) == [['I', 'V', 'X']]


def test_zero_one_thru_three_and_six_thru_eight():
    test_one_eight = Converter_Roman_Numeral("83")
    assert test_one_eight.converter() == "LXXXIII"


def test_nine_and_four():
    test_nine_four = Converter_Roman_Numeral("994")
    assert test_nine_four.converter() == "CMXCIV"


def test_romans():
    test_roman = Converter_Roman_Numeral('V')
    assert test_roman.converter() == 5


def test_with_zeros():
    test_roman = Converter_Roman_Numeral('3005')
    assert test_roman.converter() == "MMMV"


# Next steps, stop erroneous input
# def test_stop_erroneous_input():
#     test_stop = Converter_Roman_Numeral('CD')
#     assert test_stop.erroneous == "Not properly formatted"


convert_tool = Converter_Roman_Numeral('CD').converter()
print(convert_tool)

# Tests:
test_number_to_list()
test_numeral_to_list()
test_roman_group_placevalue()
test_zero_one_thru_three_and_six_thru_eight()
test_nine_and_four()
test_romans()
test_with_zeros()
