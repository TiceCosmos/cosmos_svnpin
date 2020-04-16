# SHELL=/bin/bash
.PHONY: all clean
all: dict/essay.txt dict/cosmos_pinyin1.dict.yaml dict/cosmos_pinyin2.dict.yaml
dict/essay.txt: makefile target src/essay.txt
	@grep -P "\t" src/essay.txt | opencc -c t2s > $@
dict/cosmos_pinyin1.dict.yaml: src/head.txt target/merge1.txt
	@cat src/head.txt target/merge1.txt > $@
dict/cosmos_pinyin2.dict.yaml: src/head.txt target/merge2.txt
	@cat src/head.txt target/merge2.txt > $@
target/merge1.txt: src/merge1.py target/pinyin_word.txt target/pinyin_phrase.txt target/stroke.txt
	@./src/merge1.py target/pinyin_word.txt target/pinyin_phrase.txt target/stroke.txt > $@
target/merge2.txt: src/merge2.py src/gb2312.txt target/pinyin_word.txt target/pinyin_phrase.txt target/stroke.txt
	@./src/merge2.py src/gb2312.txt target/pinyin_word.txt target/pinyin_phrase.txt target/stroke.txt > $@
target/pinyin_word.txt: makefile target src/luna_pinyin.dict.yaml
	@grep -P "^.\t" src/luna_pinyin.dict.yaml > $@
target/pinyin_phrase.txt: makefile target src/luna_pinyin.dict.yaml
	@grep -P "\t" src/luna_pinyin.dict.yaml | grep -v -P "^.\t" | opencc -c t2s > $@
target/stroke.txt: makefile target src/单字_笔顺码_29685个.txt
	@cat src/单字_笔顺码_29685个.txt | awk '{print $$2,$$4}' | sed 's/1/H/g;s/2/S/g;s/3/P/g;s/4/N/g;s/5/Z/g;s/ /\t/g' > $@
target:
	@mkdir $@
clean:
	rm target/*
