<!-- BEGIN:AVATAR -->
![Avatar](avatar.jpg)
<!-- END:AVATAR -->

<!-- BEGIN:BADGES -->
[![Build Status](https://github.com/cliffano/ansible-role-studio-dev/workflows/CI/badge.svg)](https://github.com/cliffano/ansible-role-studio-dev/actions?query=workflow%3ACI)
[![Security Status](https://snyk.io/test/github/cliffano/ansible-role-studio-dev/badge.svg)](https://snyk.io/test/github/cliffano/ansible-role-studio-dev)
<!-- END:BADGES -->

# Ansible Role Studio Dev Tools

Studio Dev Tools is a Ansible role for provisioning dev tools for Studio projects .

## Usage

Use the role in your playbook:

```yaml
- hosts: all

  vars:
    ans_reverse: true
    ans_transformation: 'upper'

  roles:
    - cliffano.studio_dev
```

## Config

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| sdev_username | System username | `root` | `someuser` |
| sdev_home_dir | Home directory path | `/tmp` | `/home/someuser` |
| sdev_profile_file | Shell profile filename | `.zprofile` | `.bashrc` |
| sdev_poetry_dir | Poetry installation directory | `/tmp/poetry` | `/home/someuser/.poetry` |
| sdev_repoman_link_src | Source path for Repoman symlink | `/tmp/stage/repoman` | `/opt/stage/repoman` |
| sdev_ssh_config_link_src | Source path for SSH config symlink | `/tmp/stage/sshconfig` | `/opt/stage/sshconfig` |
| sdev_ssh_config_file | SSH config filename | `config` | `config` |
| sdev_ssh_configd_link_src | Source path for SSH config include directory symlink | `/tmp/stage/sshconfigd` | `/opt/stage/sshconfigd` |
| sdev_ssh_configd_file | SSH config include directory filename | `configd` | `configd` |
| sdev_ssh_private_key_link_src | Source path for SSH private key symlink | `/tmp/stage/id_ed25519` | `/opt/stage/id_rsa` |
| sdev_ssh_public_key_link_src | Source path for SSH public key symlink | `/tmp/stage/id_ed25519.pub` | `/opt/stage/id_rsa.pub` |
| sdev_sshkey_name | SSH key name | `id_ed25519` | `id_rsa` |
| sdev_ghostty_config_link_src | Source path for Ghostty terminal config symlink | `/tmp/stage/ghosttyconfig` | `/opt/stage/ghosttyconfig` |
| sdev_ghostty_config_file | Ghostty config filename | `config` | `config` |
| sdev_git_aliases_file | Oh My Zsh git aliases custom file | `aliases-git.zsh` | `aliases-git.zsh` |
| sdev_gitconfig_link_src | Source path for .gitconfig symlink | `/tmp/stage/.gitconfig` | `/opt/stage/.gitconfig` |
| sdev_gitconfig_file | Git config filename | `.gitconfig` | `.gitconfig` |
| sdev_gpgagent_conf_file | GPG agent configuration filename | `gpg-agent.conf` | `gpg-agent.conf` |
| sdev_tmux_config_link_src | Source path for tmux config symlink | `/tmp/stage/.tmux.conf` | `/opt/stage/.tmux.conf` |
| sdev_tmux_config_file | tmux config filename | `.tmux.conf` | `.tmux.conf` |
| sdev_tmux_aliases_file | Oh My Zsh tmux aliases custom file | `aliases-tmux.zsh` | `aliases-tmux.zsh` |
| sdev_tmux_layout_scripts_dir | Directory containing tmux layout scripts | `/tmp/tmux-layouts` | `/opt/tmux-layouts` |
| sdev_tmux_layout_scripts | List of tmux layout script names | `[studio]` | `[studio, dev]` |
| sdev_npm_packages | List of global npm packages to install | `[repoman]` | `[repoman, yo]` |
| sdev_workspaces | List of workspace names, creates `~/dev/workspace-<name>` directories | `[control]` | `[control, garage]` |
| sdev_vscode_workspaces | List of VSCode workspace names | `[control]` | `[control, garage]` |
| sdev_colima_networks | List of Colima network names | `[studio]` | `[studio, dev]` |
| sdev_docker_images | List of Docker image configs, each with `id`, `image`, `env_file`, `home_dir`, and `entrypoint` | `[{id: studio, image: cliffano/studio, ...}]` | `[{id: myapp, image: myorg/myapp, env_file: /tmp/.env, home_dir: root, entrypoint: /bin/bash}]` |
| sdev_homebrew_packages_extra | Extra Homebrew packages to install on top of the base list | `[1password-cli]` | `[1password-cli, awscli]` |
| sdev_homebrew_cask_apps_extra | Extra Homebrew cask apps to install on top of the base list | `[discord]` | `[discord, slack]` |

## Colophon

<!-- BEGIN:DEVELOPERS_GUIDE -->
[Developer's Guide](https://cliffano.github.io/developers-guide-ansible.html)
<!-- END:DEVELOPERS_GUIDE -->

<!-- BEGIN:BUILD_REPORTS -->
Build reports:

* [Lint report](https://cliffano.github.io/ansible-role-studio-dev/lint/ansible-lint.txt)
* [Test report](https://cliffano.github.io/ansible-role-studio-dev/test/molecule.txt)

<!-- END:BUILD_REPORTS -->
