# steinmetz

## Get started

1. `python3 -m venv venv`
   venvという仮想環境モジュールを指定して，2つ目でその名前を指定する(基本的にはvenvという名前にする)
2. Activate
3. `pip3 install -r requirements.txt`
    他の人が使っている仮想環境(各ライブラリのバージョン)と同じ状態を作り出す
4. When finish your jobs: `deactivate`

| Platform | Shell           | Command to activate virtual environment |
| -------- | --------------- | --------------------------------------- |
| POSIX    | bash/zsh        | $ source <venv>/bin/activate            |
|          | fish            | $ source <venv>/bin/activate.fish       |
|          | csh/tcsh        | $ source <venv>/bin/activate.csh        |
|          | PowerShell Core | $ <venv>/bin/Activate.ps1               |
| Windows  | cmd.exe         | C:\> <venv>\Scripts\activate.bat        |
|          | PowerShell      | PS C:\> <venv>\Scripts\Activate.ps1     |
