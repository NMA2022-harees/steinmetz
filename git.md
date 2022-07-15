# Gitチートシート

ドキュメント: https://git-scm.com/doc
それぞれのサブコマンドの後ろに`-help`をつけると詳しい使い方や使えるオプションなどが確認できる。

- `git clone <src_link> [<destination_path>]`
  - srcからdestinationにリポジトリをダウンロードする
- `git switch <branch>`
  - branchを移動する
- `git switch -c <new_branch>`
  - branchを新規作成する
- `git add <file>`
  - commitするファイルに追加する
  - VSCodeの画面でやったほうが楽
- `git commit`
  - commitする（セーブする）
  - VSCodeの画面でやったほうが楽
- `git push`
  - localのcommitをremoteに同期（アップロード）する
  - 忘れがち
- `git pull`
  - remoteの変更をlocalに同期（ダウンロード）する
- `git reset --soft HEAD^`
  - 変更はそのままに直前のcommitだけ取り消す
  - VSCodeのHistory画面からやるほうがわかりやすいかも？
- `git reset --hard HEAD^`
  - 変更を破棄し、直前のcommitと同じ状態に戻る
  - VSCodeのHistory画面からやるほうがわかりやすいかも？
- その他
  - e-mailとユーザー名を設定する必要がある
  - ヒストリーの確認は`ctrl+shift+P(cmd+shift+P)`で起動するコマンドパレットの`Git: View History (git log)`から
  - branchをmainに取り込むときは`GitHub`で`PullRequest(PR)`を作成する
  - conflictしたときは適切に取り込んだ後、`add`して`commit`すれば良い（これはコマンドラインでやらないといいない）