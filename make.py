#!/usr/bin/env python3

import codecs
import datetime
import logging
import os
import shutil
import yaml


version = datetime.datetime.now().strftime("%Y.%m.%d")

thuocl_dict_list = [file.removesuffix(".txt") for file in os.listdir(os.path.join("THUOCL", "data"))]
thuocl_dict_list.sort()


def 复制文件(target_dir: str, origin_dir: str, filename: str) -> None:
    shutil.copy(os.path.join(origin_dir, filename), os.path.join(target_dir, filename))


def 统一复制(folder: str) -> None:
    if not os.path.exists(folder):
        os.mkdir(folder)

    复制文件(folder, "rime-essay-simp", "essay-zh-hans.txt")

    复制文件(folder, "target", "cosmos_pinyin.dict.yaml")
    复制文件(folder, "target", "pinyin_simp_stroke.dict.yaml")

    for filename in thuocl_dict_list:
        复制文件(folder, "target", filename + ".dict.yaml")


def 生成_核心词库() -> None:
    def 获取过滤后字典(file_path: str) -> list:
        dict_list = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("---") or line.startswith("..."):
                    break
            for line in file:
                if line.startswith("---") or line.startswith("..."):
                    break
            for line in file:
                if len(line) == 1 or line.startswith("#"):
                    continue
                else:
                    dict_list.append(line.strip().split("\t"))

        return dict_list

    def 获取拼音字典() -> list:
        pinyin_dict = []

        for line_list in 获取过滤后字典(os.path.join("rime-pinyin-simp", "pinyin_simp.dict.yaml")):
            if len(line_list) == 3:
                pinyin_dict.append((line_list[0], line_list[1], line_list[2]))
            else:
                logging.warning("get_pinyin_dict: {}".format(line_list))

        return pinyin_dict

    def 获取笔画字典() -> dict:
        stroke_dict = {}

        for line_list in 获取过滤后字典(os.path.join("rime-stroke", "stroke.dict.yaml")):
            if len(line_list) == 2:
                stroke_dict[line_list[0]] = line_list[1].swapcase()
            else:
                logging.warning("get_stroke_dict: {}".format(line_list))

        return stroke_dict

    hybrid_dict = 获取拼音字典()
    stroke_dict = 获取笔画字典()

    for i, (words, codes, count) in enumerate(hybrid_dict):
        code_list = codes.split(" ")

        for j, code in enumerate(code_list):
            stroke = stroke_dict.get(words[j])

            if stroke == None:
                logging.warning("{}: not find the stroke of {}".format((words, words[j])))
                break

            code_list[j] = stroke + code
        else:
            hybrid_dict[i] = (words, " ".join(code_list), count)

    with open(os.path.join("target", "pinyin_simp_stroke.dict.yaml"), "w", encoding="utf-8") as file:
        file.writelines(
            [
                "# Rime dictionary\n",
                "# encoding: utf-8\n",
                "# 简体中文，拼音 + 笔画\n",
                "\n---\n",
                "name: pinyin_simp_stroke\n",
                "version: {}\n".format(version),
                "sort: by_weight\n",
                "columns:\n",
                "  - text\n",
                "  - code\n",
                "  - weight\n",
                "...\n\n",
            ]
        )
        for line in hybrid_dict:
            file.write("\t".join(line))
            file.write("\n")


def 生成_统计语料() -> None:
    thuocl_path = os.path.join("THUOCL", "data")
    for filename in thuocl_dict_list:
        contents = [
            "# Rime dictionary\n",
            "# encoding: utf-8\n",
            "\n---\n",
            "name: {}\n".format(filename),
            "version: {}\n".format(version),
            "sort: by_weight\n",
            "columns:\n",
            "  - text\n",
            "  - weight\n",
            "...\n\n",
        ]

        filepath = os.path.join(thuocl_path, filename + ".txt")
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            if content[0] == codecs.BOM_UTF8.decode("utf-8"):
                content = content[1:]
            contents += content

        filepath = os.path.join("target", filename + ".dict.yaml")
        with open(filepath, "w", encoding="utf-8") as file:
            file.writelines(contents)


def 生成_集成词库() -> None:
    from yaml.loader import FullLoader

    comments = ""
    contents = ""

    with open("cosmos_pinyin.dict.yaml", "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("---") or line.startswith("..."):
                break
            comments += line
        for line in file:
            if line.startswith("---") or line.startswith("..."):
                break
            contents += line

    contents = yaml.load(contents, FullLoader)
    contents["version"] = version
    contents["import_tables"] = []
    contents["import_tables"].append("pinyin_simp_stroke")
    for dict in thuocl_dict_list:
        contents["import_tables"].append(dict)

    with open(os.path.join("target", "cosmos_pinyin.dict.yaml"), "w", encoding="utf-8") as file:
        file.write(comments)
        file.write("---\n")
        contents = yaml.dump(contents, file, sort_keys=False)
        file.write("...\n")


def 生成_配置(source: str) -> None:
    target = os.path.join("target", source)
    统一复制(target)
    for filename in os.listdir(source):
        复制文件(target, source, filename)


def generate() -> None:
    生成_核心词库()
    生成_统计语料()
    生成_集成词库()

    生成_配置("中州韵")
    生成_配置("同文")


if __name__ == "__main__":
    generate()
