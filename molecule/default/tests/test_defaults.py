import pytest

def test_profile(host):

    profile_file = host.file("/tmp/.zprofile")
    assert profile_file.exists
    assert profile_file.is_file
    assert profile_file.mode == 0o644

def test_bullet_train_theme(host):

    theme_file = host.file("/tmp/.oh-my-zsh/themes/bullet-train.zsh-theme")
    assert theme_file.exists
    assert theme_file.is_file
    assert theme_file.mode == 0o644

def test_term_export(host):

    profile_file = host.file("/tmp/.zprofile")
    assert "export TERM='xterm-256color'" in profile_file.content_string

def test_gitconfig(host):

    gitconfig_file = host.file("/tmp/.gitconfig")
    assert gitconfig_file.exists
    assert gitconfig_file.is_symlink

def test_git_aliases(host):

    git_aliases_file = host.file("/tmp/.oh-my-zsh/custom/aliases-git.zsh")
    assert git_aliases_file.exists
    assert git_aliases_file.is_file
    assert git_aliases_file.mode == 0o644
    assert "alias gaa=git add -A" in git_aliases_file.content_string
    assert "alias gta=git tag -a" in git_aliases_file.content_string


def test_gpg_agent_conf(host):

    gpg_agent_file = host.file("/tmp/.gnupg/gpg-agent.conf")
    assert gpg_agent_file.exists
    assert gpg_agent_file.is_file
    assert gpg_agent_file.mode == 0o644
    assert "pinentry-program /usr/local/bin/pinentry-mac" in gpg_agent_file.content_string
    assert "default-cache-ttl" in gpg_agent_file.content_string
    assert "max-cache-ttl 28800" in gpg_agent_file.content_string

def test_npm_packages(host):

    npm_list = host.run("npm list -g --depth=0")
    assert 'repoman' in npm_list.stdout