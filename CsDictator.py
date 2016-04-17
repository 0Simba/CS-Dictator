
import sublime, sublime_plugin, re


def standarize_variables_declaration (string) :
    only_one_space            = re.compile(r"\s{2,}", re.IGNORECASE)
    no_space_before_semilicon = re.compile(r"\s;",    re.IGNORECASE)

    string = re.sub(only_one_space,            " ", string)
    string = re.sub(no_space_before_semilicon, ";", string)

    return string



def maximum_letter_per_declarations_keys (declarations) :
    a = 1



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






class CsDictatorCommand (sublime_plugin.TextCommand):
    def run (self, edit):

        code                      = selection_to_standard_code(self)
        declarations              = splited_declarations_code(code)
        words_declaration_lengths = maximum_letter_per_declarations_keys(declarations)


        self.view.insert(edit, 0, string)












        # parsedString = [""];

        # for region in sel:
        #     parsedString = 


        # for i in range(len(parsedString)):
        #     parsedString[i] = "..." + parsedString[i]


        # string = "\n".join(parsedString)
