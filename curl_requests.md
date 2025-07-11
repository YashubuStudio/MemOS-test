# MemOS API with curl (cmd)

The following commands show how to interact with a MemOS server using `curl` on Windows `cmd`. The server is assumed to run on `http://localhost:8000` and uses Ollama's `gemma3` model running at `http://localhost:11434`.

Start the server:

```
make serve
```

## Configure MemOS

```
curl -X POST "http://localhost:8000/configure" -H "Content-Type: application/json" -d "{\"user_id\":\"root\",\"chat_model\":{\"backend\":\"ollama\",\"config\":{\"model_name_or_path\":\"gemma3\",\"api_base\":\"http://localhost:11434\"}},\"mem_reader\":{\"backend\":\"simple_struct\",\"config\":{\"llm\":{\"backend\":\"ollama\",\"config\":{\"model_name_or_path\":\"gemma3\",\"api_base\":\"http://localhost:11434\"}},\"embedder\":{\"backend\":\"ollama\",\"config\":{\"model_name_or_path\":\"nomic-embed-text\"}},\"chunker\":{\"backend\":\"sentence\",\"config\":{}}}}" 
```

## User operations

Create a user:
```
curl -X POST "http://localhost:8000/users" -H "Content-Type: application/json" -d "{\"user_id\":\"test_user\",\"user_name\":\"Test User\",\"role\":\"user\"}"
```

List users:
```
curl http://localhost:8000/users
```

Get current user info:
```
curl http://localhost:8000/users/me
```

## MemCube operations

Register a cube:
```
curl -X POST "http://localhost:8000/mem_cubes" -H "Content-Type: application/json" -d "{\"mem_cube_name_or_path\":\"/path/to/cube\",\"mem_cube_id\":\"cube123\",\"user_id\":\"root\"}"
```

Share a cube:
```
curl -X POST "http://localhost:8000/mem_cubes/cube123/share" -H "Content-Type: application/json" -d "{\"target_user_id\":\"another_user\"}"
```

Remove a cube:
```
curl -X DELETE "http://localhost:8000/mem_cubes/cube123?user_id=root"
```

## Memory operations

Add text memory:
```
curl -X POST "http://localhost:8000/memories" -H "Content-Type: application/json" -d "{\"memory_content\":\"hello world\",\"mem_cube_id\":\"cube123\",\"user_id\":\"root\"}"
```

Add chat messages:
```
curl -X POST "http://localhost:8000/memories" -H "Content-Type: application/json" -d "{\"messages\":[{\"role\":\"user\",\"content\":\"hello\"}],\"mem_cube_id\":\"cube123\",\"user_id\":\"root\"}"
```

List memories:
```
curl "http://localhost:8000/memories?mem_cube_id=cube123&user_id=root"
```

Get a memory:
```
curl "http://localhost:8000/memories/cube123/memory123?user_id=root"
```

Update a memory:
```
curl -X PUT "http://localhost:8000/memories/cube123/memory123?user_id=root" -H "Content-Type: application/json" -d "{\"content\":\"updated text\"}"
```

Delete a memory:
```
curl -X DELETE "http://localhost:8000/memories/cube123/memory123?user_id=root"
```

Delete all memories in a cube:
```
curl -X DELETE "http://localhost:8000/memories/cube123?user_id=root"
```

Search memories:
```
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" -d "{\"query\":\"hello\",\"user_id\":\"root\",\"install_cube_ids\":[\"cube123\"]}"
```

## Chat

```
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d "{\"query\":\"How are you?\",\"user_id\":\"root\"}"
```

