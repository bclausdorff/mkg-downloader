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