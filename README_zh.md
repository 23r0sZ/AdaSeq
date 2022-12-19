# AdaSeq: An All-in-One Library for Developing State-of-the-Art Sequence Understanding Models

[![license](https://img.shields.io/github/license/modelscope/adaseq.svg)](./LICENSE)
[![modelscope](https://img.shields.io/badge/modelscope-1.1.0-624aff.svg)](https://modelscope.cn/)
![version](https://img.shields.io/github/tag/modelscope/adaseq.svg)
[![issues](https://img.shields.io/github/issues/modelscope/adaseq.svg)](https://github.com/modelscope/AdaSeq/issues)
[![stars](https://img.shields.io/github/stars/modelscope/adaseq.svg)](https://github.com/modelscope/AdaSeq/stargazers)
[![contribution](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](./CONTRIBUTING.md)

<div align="center">

[English](./README.md) | 简体中文

</div>

## 简介
***AdaSeq*** (**A**libaba **D**amo **A**cademy **Seq**uence Understanding Toolkit) 是一个基于[ModelScope](https://modelscope.cn/home)的序列理解开源工具箱，旨在提高开发者和研究者们的开发和创新效率，助力前沿论文工作落地。

![](./docs/imgs/task_examples_zh.png)

<details open>
<summary>🌟 <b>特性：</b></summary>

- **算法丰富**：

  AdaSeq提供了序列理解任务相关的大量前沿模型、训练方法和上下游工具。

- **性能强劲**：

  我们旨在开发性能最好的模型，在序列理解任务上胜出过其他开源框架。

- **简单易用**：

  只需一行命令，即可进行训练。

- **扩展性强**：

  用户可以自由注册模块组件，并通过组合不同的模块组件，便捷地构建自定义的检测模型。

</details>

⚠️**注意：** 这个项目仍在高速开发阶段，部分接口可能会发生改变。

## 📢 最新进展
- 2022-12: [[EMNLP 2022] 实现 MoRE 算法](./examples/MoRe)
- 2022-11: [[EMNLP 2022] 实现 NPCRF 算法](./examples/NPCRF)
- 2022-11: [[EMNLP 2022] BABERT 模型释出，实验复现](./examples/babert)

## ⚡ 快速体验
可以在ModelScope上快速体验我们的模型：

[[英文NER]](https://modelscope.cn/models/damo/nlp_raner_named-entity-recognition_english-large-news/summary)
[[中文NER]](https://modelscope.cn/models/damo/nlp_raner_named-entity-recognition_chinese-base-news/summary)
[[中文分词]](https://modelscope.cn/models/damo/nlp_structbert_word-segmentation_chinese-base/summary)

全部我们已发布的模型卡片：[Modelcards](./docs/modelcards.md)

## 🛠️ 模型库
<details open>
<summary><b>支持的模型：</b></summary>

- [Transformer-based CRF](./examples/bert_crf)
- [Partial CRF](./examples/partial_bert_crf)
- [Retrieval Augmented NER](./examples/RaNER)
- [Global-Pointer](./examples/global_pointer)
- [Multi-label Entity Typing](./examples/entity_typing)
- ...
</details>

## 💾 数据集
我们整理了很多序列理解相关任务的数据集：[Datasets](./docs/datasets.md)

## 📦 安装AdaSeq
AdaSeq项目基于 `Python version >= 3.7` 和 `PyTorch version >= 1.8`.
```
git clone https://github.com/modelscope/adaseq.git
cd adaseq
pip install -r requirements.txt -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html
```

## 📖 教程文档
- [快速开始](./docs/tutorials/quick_start_zh.md)
- 基础教程
  - [了解配置文件](./docs/tutorials/learning_about_configs_zh.md)
  - [自定义数据集](./docs/tutorials/customizing_dataset_zh.md)
  - [TODO] 常用架构和模块化设计
  - [TODO] 有用的Hooks
  - [超参数优化](./docs/tutorials/hyperparameter_optimization_zh.md)
  - [使用多GPU训练](./docs/tutorials/training_with_multiple_gpus_zh.md)
- 最佳实践
  - [在自定义数据上训练模型](./docs/tutorials/training_a_model_zh.md)
  - [复现论文实验结果](./docs/tutorials/reproducing_papers_zh.md)
  - [TODO] 上传模型到ModelScope
  - [TODO] 实现自定义模型
  - [TODO] 使用AdaLA进行推理

## 📝 贡献指南
我们感谢所有为了改进AdaSeq而做的贡献，也欢迎社区用户积极参与到本项目中来。请参考 [CONTRIBUTING.md](./CONTRIBUTING.md) 来了解参与项目贡献的相关指引。

## 📄 开源许可证
本项目采用 Apache 2.0 License 开源许可证.
