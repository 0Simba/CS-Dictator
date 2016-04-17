
import sublime, sublime_plugin, re


def standarize_variables_declaration (string) :
    only_one_space            = re.compile(r"\s{2,}", re.IGNORECASE)
    no_space_before_semilicon = re.compile(r"\s;",    re.IGNORECASE)

    string = re.sub(only_one_space,            " ", string)
    string = re.sub(no_space_before_semilicon, ";", string)

    return string



def maximum_letters_per_declarations_keys (declarations) :
    lengths = [];

    for i in range(len(declarations[0])) :
        lengths.append(len(declarations[0][i]))

    for i in range(len(declarations)) :
        for j in range(len(declarations[i])) :
            lengths[j] = max(lengths[j], len(declarations[i][j]))

    return lengths




def selection_to_standard_code (self) :
    view = self.view
    sel  = view.sel()


    region = sel[0]
    code   = view.substr(region)
    code   = standarize_variables_declaration(code);

    return code



def splited_declarations_code (code) :
    lines        = code.split("\n")
    splited_code = []

    for i in range(len(lines)) :
        splited_code.append([])
        words = lines[i].split(" ")

        for j in range(len(words)) :
            splited_code[i].append(words[j])


    return splited_code



def declarations_to_code_in_table (declarations) :
    words_declaration_lengths = maximum_letters_per_declarations_keys(declarations)
    code                      = ""

    for i in range(len(declarations)) :
        line = declarations[i]
        if (i != 0) :
            code += "\n"

        for j in range(len(line)) :
            word         = line[j]
            code         += word
            space_needed = words_declaration_lengths[j] - len(word)

            if (len(line) - 1 != j) :
                space_needed += 1
                

            for _ in range(space_needed) :
                code += ' '


    return code




class TestCommand (sublime_plugin.TextCommand):
    def run (self, edit):

        code                      = selection_to_standard_code(self)
        declarations              = splited_declarations_code(code)
        code_in_table             = declarations_to_code_in_table(declarations);


        self.view.insert(edit, 0, code_in_table)
        
