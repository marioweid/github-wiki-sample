from git import Repo
import os
import argparse


def commit_files(repo: Repo, remote_url: str, branch: str = 'master') -> None:
    master = repo.create_head(branch)  # gitlab(main) vs github(master)
    master.checkout()
    repo.git.push(remote_url, "--force")


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
    gitlab_repo = Repo.clone_from(args.src_repo, source_dir)

    commit_files(gitlab_repo, args.dest_repo)
