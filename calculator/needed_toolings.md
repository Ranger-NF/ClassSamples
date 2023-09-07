# Things Needed

- Python3 added to path:

  ```
      python3 --version
      sudo apt-get update
      sudo apt-get install python3.6

  ```

- Code editor like VsCode
  `snap install codium --classic`

  OR

  ```
      wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg \
  | gpg --dearmor \
  | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg

  echo 'deb [ signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg ] https://download.vscodium.com/debs vscodium main' \
  | sudo tee /etc/apt/sources.list.d/vscodium.list

  sudo apt update && sudo apt install codium
  ```

  OR

  `https://code.visualstudio.com/download`
