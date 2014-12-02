import os


def _touch(fname):
    try:
        os.utime(fname, None)
    except:
        open(fname, 'a').close()
    return fname


def _build(path, pwd=None):
    current = path.pop(0)
    if pwd:
        here = pwd + os.sep + current
    else:
        here = current
    if not path:
        return _touch(here)
    else:
        if not os.path.exists(here):
            os.makedirs(here)
        _build(path, here)


def generate_view(dir, name):
    view = "app" + os.sep + "views" + os.sep + name + ".html"
    split = name.split(os.sep)
    namespace = split[-1]
    split[-1] = "_" + namespace + ".scss"
    style = "lib" + os.sep + "styles" + os.sep + "site" + os.sep + os.sep.join(split)
    _build(view.split(os.sep), dir)
    _build(style.split(os.sep), dir)

    # view html file
    with open(dir + os.sep + view, 'w') as f:
        f.write("<div class='page %s'>\n\n</div>" % namespace)

    # styles file
    with open(dir + os.sep + style, 'w') as f:
        f.write(".page.%s{\n\n}" % namespace)

    #import styles styles
    with open(dir + os.sep + 'lib' + os.sep + 'styles' + os.sep + 'styles.scss', 'a') as styles:
        styles.write('@import "site/%s";\n' % name)


if __name__ == "__main__":
    generate_view('../../assets', 'homepage')
    generate_view('../../assets', 'settings/permissions')
    generate_view('../../assets', 'user/settings/new')



