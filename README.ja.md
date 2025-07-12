# MemOS 1.0: 星河 (Stellar)

MemOSは、大規模言語モデル(LLM)に長期記憶を与えるためのオペレーティングシステムです。情報の保存・取得・管理を容易にし、よりコンテキストを考慮した会話や推論を可能にします。

- **Webサイト**: <https://memos.openmem.net/>
- **ドキュメント**: <https://memos.openmem.net/docs/home>
- **APIリファレンス**: <https://memos.openmem.net/docs/api/info>
- **ソースコード**: <https://github.com/MemTensor/MemOS>

## 📈 パフォーマンスベンチマーク

MemOSは複数の推論タスクにおいてベースラインを大きく上回る性能を示しています。

| モデル | 平均スコア | マルチホップ | オープンドメイン | シングルホップ | 時系列推論 |
| ------ | ---------- | ------------ | ---------------- | -------------- | ---------- |
| **OpenAI** | 0.5275 | 0.6028 | 0.3299 | 0.6183 | 0.2825 |
| **MemOS** | **0.7331** | **0.6430** | **0.5521** | **0.7844** | **0.7321** |
| **改善率** | **+38.98%** | **+6.67%** | **+67.35%** | **+26.86%** | **+159.15%** |

## ✨ 主な特徴

- **🧠 Memory-Augmented Generation (MAG)**: メモリ操作用の統一APIを提供し、LLMと連携してチャットや推論時にコンテキストメモリを検索します。
- **📦 Modular Memory Architecture (MemCube)**: 複数のメモリタイプを簡単に統合・管理できる柔軟なアーキテクチャ。
- **💾 多彩なメモリタイプ**: テキストメモリ、アクティベーションメモリなど。

### MemCubeとは？

複数のメモリ(テキスト、アクティベーション、パラメトリックなど)をまとめて保存・管理するコンテナです。各ユーザーのMemCubeはローカルディレクトリやHugging Faceのリポジトリとして配置でき、ロードや共有が容易に行えます。

## 📦 インストール

> **注意**: MemOSはLinux、Windows、macOSで動作しますが、macOSでは依存関係の解決が難しい場合があります。

### pipでインストール

```bash
pip install MemoryOS
```

新しい環境で始める場合は、後述の[Ollamaサポート](#ollama-サポート)に従ってOllamaもインストールしてください。これにより、ローカルOllamaサーバーを利用したサンプルが実行できます。

### 開発者向けインストール

```bash
git clone https://github.com/MemTensor/MemOS.git
cd MemOS
make install
```

### オプションの依存関係

#### Ollamaサポート

Ollama CLIをインストールします。

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

インストール後、Ollamaサーバーを起動し、モデルを取得します (サンプルでは`gemma3:latest`を使用)。

```bash
ollama serve &                 # ローカルOllamaサーバーを起動
ollama pull gemma3:latest      # 推論用モデルをダウンロード
```

サーバーが `http://localhost:11434` で起動していれば、次のサンプルを試せます。

```bash
python examples/basic_modules/llm.py
```

#### Transformersサポート

`transformers` ライブラリを使う場合は [PyTorch](https://pytorch.org/get-started/locally/) をインストールしてください (GPU利用にはCUDA版推奨)。

#### Hugging Face Hub

公開リポジトリからモデルやデータセットを取得するだけであれば `huggingface-cli login` は必須ではありません。プライベートリポジトリを利用する場合や高速にダウンロードしたい場合は、アクセストークンを取得して `huggingface-cli login` を実行してください。

## 💬 コミュニティとサポート

- **GitHub Issues**: <https://github.com/MemTensor/MemOS/issues>
- **Pull Requests**: <https://github.com/MemTensor/MemOS/pulls>
- **GitHub Discussions**: <https://github.com/MemTensor/MemOS/discussions>
- **Discord**: <https://discord.gg/Txbx3gebZR>
- **WeChat**: QRコードから参加できます

<img src="docs/assets/qr_code.png" alt="QR Code" width="600">

## 📜 引用

MemOSを研究で利用する場合、以下の論文を引用していただけると幸いです。

```bibtex
@article{li2025memos_long,
  title={MemOS: A Memory OS for AI System},
  author={Li, Zhiyu and others},
  journal={arXiv preprint arXiv:2507.03724},
  year={2025},
  url={https://arxiv.org/abs/2507.03724}
}
```

## 🙌 コントリビュート

貢献を歓迎します。詳細は[貢献ガイドライン](https://memos.openmem.net/docs/contribution/overview)をご覧ください。

## 📄 ライセンス

MemOSは[Apache 2.0 License](./LICENSE)で公開されています。

## 📰 最新情報

- **2025-07-07** – MemOS 1.0 (Stellar) プレビューリリース
- **2025-07-04** – MemOS論文公開: <https://arxiv.org/abs/2507.03724>
- **2025-05-28** – Short Paper公開: <https://arxiv.org/abs/2505.22101>
- **2024-07-04** – WAIC 2024でMemory3モデル公開
- **2024-07-01** – Memory3論文公開: <https://arxiv.org/abs/2407.01178>
