# make csv file as test data for input validation.
# prepare sample.csv which can pass the validation,
# and test_case.csv that indicates which property needs to change.

def readFile(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data_list = []
        for line in f:
            data_list.append(line.strip().split(','))
    f.close()
    return data_list

def writeFile(sample, test_case):

    test_no = int(test_case[0])
    test_item_name = test_case[1]
    test_value = test_case[2]
    output_file_name = str(test_no) + '_' + test_item_name + '.csv'
    
    with open(output_file_name, 'w', encoding='shift_jis') as f:
        sample_edited = list(sample)
        sample_edited[test_no - 1] = test_value
        f.write(','.join(sample_edited))
    f.close()
    return output_file_name

if __name__ == '__main__':
    sample = tuple(readFile('sample.csv')[0])
    test_cases = readFile('test_case.csv')
    for test_case in test_cases:
        print(writeFile(sample, test_case))
