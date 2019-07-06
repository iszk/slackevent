# slackevent
slack event を見る人

## 動くまで

https://api.slack.com/apps から `Create New App` する
`Basin Information` から `Verification Token` をメモっておく
`Incoming Webhooks` を On にして `Add New Webhook to Workspace` から追加して、webhook url をメモっておく

`.chalice/config-dist.json` を参考に `config.json` を編集する
メモしておいた verification_code と webhook url を入れる

デプロイする
```
$ chalice deploy
```
URLが表示されるので、これをメモしておく

`Event Subscriptions` を On にして `Add Workspace Event` から `emoji_changed` を追加する

`Request URL` にデプロイしたURLを入れる


