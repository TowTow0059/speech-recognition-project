# Step 1
import pickle
import PairFile

file = PairFile.PairFile(path='asd', keyword='zxc')

# config_dictionary = {file.path: file.keyword}

# print(callable(PairFile))

# Step 2
with open('config.sav', 'wb') as config_dictionary_file:
    # Step 3
    pickle.dump(file, config_dictionary_file, pickle.HIGHEST_PROTOCOL)

# Step 2
with open('config.sav', 'rb') as config_dictionary_file:
    # Step 3
    config_dictionary = pickle.load(config_dictionary_file)

    # After config_dictionary is read from file
    print(config_dictionary.path)
    # print(type(config_dictionary))
