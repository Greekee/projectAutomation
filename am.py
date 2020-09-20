from github import Github
import git
import subprocess
import os
import sys

repo_dir = os.getcwd() + "/"
init_filename = "README.md"

f = open("token.pem", "r")
token = f.read()
f.close()
#print(token)
#print(type(token))

g = Github(token)

user = g.get_user()

def init():
    os.chdir("..")
    repo_dir = os.getcwd() + "/" + sys.argv[1]    
    
    if os.path.exists(repo_dir):
        print("Project Directory already exists")

    os.makedirs(repo_dir)
    os.chdir(sys.argv[1])
    r = git.Repo.init(repo_dir)

    filename = os.path.join(repo_dir, init_filename)
    open(filename, 'wb').close()
    r.index.add(init_filename)
    r.index.commit("initial commit")
    
    try:
        user.create_repo( sys.argv[1] )     # wirft error, wird aber nicht gefangen und bricht ab
    except ValueError:
        print("error")
    #else:
    #    print("Repositoryname is already existing in Github")
    #    os.chdir("..")
    #    os.rmdir(repo_dir)
    #    return

    buf = "https://github.com/Greekee/" + sys.argv[1] + ".git"
    subprocess.call(["git", "remote", "add", "origin", buf])
    subprocess.call(["git", "push", "-u", "origin", "master"])

if __name__ == "__main__":
    if( len(sys.argv) != 2 ):
        print("invlaid Arguments")
        exit()

    init()