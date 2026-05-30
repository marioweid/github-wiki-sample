from git import Repo
import os
import argparse
import github


def commit_files(repo: Repo, remote_url: str, branch: str = 'master') -> None:
    master = repo.create_head(branch)  # gitlab(main) vs github(master)
    master.checkout()
    repo.git.push(remote_url, "--force")


def api_commit() -> None:
    token = "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"
    repo_name = "github-wiki-sample"
    # First create a Github instance:

    # using an access token
    g = github.Github(token)

    # Github Enterprise with custom hostname
    # g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

    repo = g.get_repo("marioweid/github-wiki-sample")
    print(repo)

    contents = repo.get_contents("README.md", ref="2b050")
    # https://github.com/marioweid/github-wiki-sample.wiki.git


    # git clone ssh://git@sam-dev.cs.hm.edu:6000/marioweid/gitlab-wiki-sample.wiki.git
    # cd gitlab-wiki-sample.wiki
    # git checkout -b master
    # git remote set-url origin github:marioweid/github-wiki-sample.wiki.git
    # git push origin master


    repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="main")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy content between git repos')
    parser.add_argument('--source', '-s', type=str, dest='src_repo',
                        help='source repository form which to copy all files')
    parser.add_argument('--destination', '-d', type=str, dest='dest_repo',
                        help='destination repo to copy contents to')
    args = parser.parse_args()

    source_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "source")
    # github_upstream = "git@github.com:marioweid/github-wiki-sample.wiki.git"

    # clone repos
    # gitlab_repo = Repo.clone_from(args.src_repo, source_dir)

    # commit_files(gitlab_repo, args.dest_repo)
    api_commit()
