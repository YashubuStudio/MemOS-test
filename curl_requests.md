# MemOS API with curl (cmd)

このドキュメントでは Windows の `cmd` 上で `curl` を使って MemOS サーバーを操作する方法を示します。
The following commands show how to interact with a MemOS server using `curl` on Windows `cmd`. The server is assumed to run on `http://localhost:8000` and uses Ollama's `gemma3` model running at `http://localhost:11434`.

Start the server:
サーバーを起動:

```
make serve
```

## Configure MemOS
MemOS の初期設定を行います。

```
curl -X POST "http://localhost:8000/configure" -H "Content-Type: application/json" -d "{\"user_id\":\"root\",\"chat_model\":{\"backend\":\"ollama\",\"config\":{\"model_name_or_path\":\"gemma3\",\"api_base\":\"http://localhost:11434\"}},\"mem_reader\":{\"backend\":\"simple_struct\",\"config\":{\"llm\":{\"backend\":\"ollama\",\"config\":{\"model_name_or_path\":\"gemma3\",\"api_base\":\"http://localhost:11434\"}},\"embedder\":{\"backend\":\"ollama\",\"config\":{\"model_name_or_path\":\"nomic-embed-text\"}},\"chunker\":{\"backend\":\"sentence\",\"config\":{}}}}}"} 
```

## User operations
ユーザー操作に関する例です。

Create a user:
ユーザーを作成します。
```
curl -X POST "http://localhost:8000/users" -H "Content-Type: application/json" -d "{\"user_id\":\"test_user\",\"user_name\":\"Test User\",\"role\":\"user\"}"
```

List users:
ユーザーの一覧を取得します。
```
curl http://localhost:8000/users
```

Get current user info:
現在ログインしているユーザーの情報を取得します。
```
curl http://localhost:8000/users/me
```

## MemCube operations
MemCube の登録や共有を行う例です。

Register a cube:
MemCube を登録します。
```
curl -X POST "http://localhost:8000/mem_cubes" -H "Content-Type: application/json" -d "{\"mem_cube_name_or_path\":\"/path/to/cube\",\"mem_cube_id\":\"cube123\",\"user_id\":\"root\"}"
```

Share a cube:
MemCube を他ユーザーと共有します。
```
curl -X POST "http://localhost:8000/mem_cubes/cube123/share" -H "Content-Type: application/json" -d "{\"target_user_id\":\"another_user\"}"
```

Remove a cube:
MemCube を削除します。
```
curl -X DELETE "http://localhost:8000/mem_cubes/cube123?user_id=root"
```

## Memory operations
メモリを追加・更新・検索する例です。

Add text memory:
テキストをメモリとして追加します。
```
curl -X POST "http://localhost:8000/memories" -H "Content-Type: application/json" -d "{\"memory_content\":\"hello world\",\"mem_cube_id\":\"cube123\",\"user_id\":\"root\"}"
```

Add chat messages:
チャットメッセージをまとめて追加します。
```
curl -X POST "http://localhost:8000/memories" -H "Content-Type: application/json" -d "{\"messages\":[{\"role\":\"user\",\"content\":\"hello\"}],\"mem_cube_id\":\"cube123\",\"user_id\":\"root\"}"
```

List memories:
メモリ一覧を取得します。
```
curl "http://localhost:8000/memories?mem_cube_id=cube123&user_id=root"
```

Get a memory:
指定したメモリを取得します。
```
curl "http://localhost:8000/memories/cube123/memory123?user_id=root"
```

Update a memory:
メモリ内容を更新します。
```
curl -X PUT "http://localhost:8000/memories/cube123/memory123?user_id=root" -H "Content-Type: application/json" -d "{\"content\":\"updated text\"}"
```

Delete a memory:
指定したメモリを削除します。
```
curl -X DELETE "http://localhost:8000/memories/cube123/memory123?user_id=root"
```

Delete all memories in a cube:
MemCube 内のメモリをすべて削除します。
```
curl -X DELETE "http://localhost:8000/memories/cube123?user_id=root"
```

Search memories:
メモリを検索します。
```
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" -d "{\"query\":\"hello\",\"user_id\":\"root\",\"install_cube_ids\":[\"cube123\"]}"
```

## Chat
保存したメモリを使ってチャットします。

```
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d "{\"query\":\"How are you?\",\"user_id\":\"root\"}"
```

