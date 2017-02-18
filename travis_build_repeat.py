from travispy import TravisPy
from settings import TRAVIS_KEY, TRAVIS_REPOS


def run():
    for r in TRAVIS_REPOS:
        t = TravisPy.github_auth(TRAVIS_KEY)
        repo = t.repo(r)
        build = t.build(repo.last_build_id)
        if build.restart():
            print("[{0}] Build {1} restarted.".format(r, repo.last_build_id))
        else:
            print("[{0}]Unable to restart build.".format(r))

if __name__ == '__main__':
    run()
