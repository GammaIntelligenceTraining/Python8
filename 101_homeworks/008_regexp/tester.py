import re

# # Task 1: #COLOR
#
# test_string = 'AliceBlue #F0F8FF, Crimson #DC143C, DarkSeaGreen #8fbc8f, GreenYellow #ADFF2F, LightSlateGrey #789,' \
#               ' White = #000, #GHGHGH, #12346789'
#
# pattern = re.compile(r'#[0-9A-Fa-f]{3,6}')
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match)

# # Task 2: Numbers with + sign
#
# test_string = 'Check if there is no + sign after number 2*9-6*5, (3+5)-9*4), (17+12)-27*3, 2345-323232+23432342'
#
# pattern = re.compile(r'(\d+)[^+]')
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     # print(match)
#     print(match.group(1))

# # Task 3: Time
#
# test_string = 'Dinner at 09:00. Lunch is at 37:98. Breakfast is at 24:60. Something else at 23:59. 00:00, 24:24,' \
#               ' 210:124, 223:23, 23:248'
#
# pattern = re.compile(r'\b([0-1][0-9]|2[0-3]):([0-5][0-9])[^0-9]')
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match.group(1) + ':' + match.group(2))

# # Task 4: people.txt
#
# with open('people.txt', 'r', encoding='utf8') as file:
#     data = file.read()
#
#     name_pattern = re.compile(r'[A-Z][a-z]+ [A-Z][a-z]+')
#     address_pattern = re.compile(r'\d{3} [A-Z0-9][a-z]+ St\., [A-Z][A-Za-z-\' ]+ [A-Z]{2} \d+')
#     # address_pattern2 = re.compile(r'[A-Z][a-z-]+ [A-Z]{2} \d+')
#
#
#     name_matches = name_pattern.finditer(data)
#     address_matches = address_pattern.finditer(data)
#     # address_matches2 = address_pattern2.finditer(data)
#
#     names = []
#     addresses = []
#
#     for name in name_matches:
#         if name.group()[-2:] != 'St' and name.group() != 'Vice City' and name.group() != 'South Park':
#             # print(name.group())
#             names.append(name.group())
#             # print(name.group())
#
#     for address in address_matches:
#         # print(address.group())
#         addresses.append(address.group())
#     # for match in names:
#     #     print(match, addresses[names.index(match)-1])
#         # print(names.index(match))
#
#     print(len(names))
#     print(len(addresses))

# # Task 5: Forbidden characters
#
# good_string = 'HelloWorld01234'
# bad_string = 'Hello, my name is John!'
#
# pattern = re.compile(r'[^a-zA-Z0-9]')
# matches = pattern.findall(good_string)
# # matches = pattern.findall(bad_string)
#
# if len(matches) != 0:
#     print('String contains forbidden characters')
# else:
#     print("String doesn't contain forbidden characters")

# # Task 6: Estonian national ID
#
# test_string = 'Hello, my name is John and my ID is 38803160272. My sisters name is Mary her id is 47513210278. ' \
#               '68811320888, 46612001234'
#
# pattern = re.compile(r'[3456][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])\d{4}')
#
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match)
