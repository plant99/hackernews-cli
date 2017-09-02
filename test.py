import textwrap

def print_modified(sentence):
	sentence_wrapped = textwrap.wrap(sentence, 50, break_long_words=1)
	length_sr = len(sentence_wrapped)
	for i in range(length_sr):
		line_tbp = '' #to_be_printed
		line_tbp+= '|'
		line_tbp+= ' '*3
		line_tbp+= sentence_wrapped[i]
		line_tbp+= ' '*(55-len(sentence_wrapped[i]))
		line_tbp+= '|'
		print line_tbp

x = "alsdlajksdalksjdlkasjdklajsioasfiyaiufaiuyfiyiyiyoyadiupapiypf9eu[09u09uifdsdifjofiuhsdkfkjsfsdjhfkjsdfhhkjhdfkjshdfsdfkjshdfiuwehisdhfsndfnksydisdhfiusyer hsjdk fsuidfisdhfsduiyf"
print_modified(x)