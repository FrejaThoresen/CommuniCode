from communicode import git


def get_projects():
    return git.getprojects()

def create_project(name):
    return git.createproject(name=name)

def get_branches():
    return git.getbranches(1)
