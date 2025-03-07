import pytest

def test_git_aliases(host):

    content_file = host.file("/tmp/.oh-my-zsh/custom/aliases-git.zsh")
    assert content_file.exists
    assert content_file.is_file
    assert content_file.mode == 0o644
    assert "alias gaa=git add -A" in content_file.content_string
