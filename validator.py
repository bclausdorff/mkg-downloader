import os.path

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle


def is_valid_dir(parser, arg):
    if not os.path.exists(arg):
        parser.error("The directory %s does not exist!" % arg)
        return

    if not os.path.isdir(arg):
        parser.error("The path %s is no directory!" % arg)
        return

    return arg + '/'

def is_valid_license(parser, arg):
    licenses = {'CC-0': 'CC0 1.0', 'CC-BY': 'CC BY 3.0 DE', 'Copyright': 'Rechte vorbehalten - freier Zugang'}

    l = licenses.get(arg, None)

    if l is None:
        parser.error("Invalid license: {} \n Available licenses: {} ".format(arg, licenses.keys()))

    return l