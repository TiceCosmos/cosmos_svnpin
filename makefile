# SHELL=/bin/bash
.PHONY: all clean
all: schema/cosmos_pinyin.dict.yaml target/essay.txt
schema/cosmos_pinyin.dict.yaml: src/head.txt target/merge.txt
	@cat src/head.txt target/merge.txt > $@
target/merge.txt: src/merge.py src/gb2312.txt target/pinyin_word.txt target/pinyin_phrase.txt target/stroke.txt
	@./src/merge.py src/gb2312.txt target/pinyin_word.txt target/pinyin_phrase.txt target/stroke.txt > $@
target/pinyin_word.txt: makefile target src/luna_pinyin.dict.yaml
	@grep -P "^.\t" src/luna_pinyin.dict.yaml > $@
target/pinyin_phrase.txt: makefile target src/luna_pinyin.dict.yaml
	@grep -P "\t" src/luna_pinyin.dict.yaml | grep -v -P "^.\t" | opencc -c t2s > $@
target/stroke.txt: makefile target src/stroke.dict.yaml
	@cat src/stroke.dict.yaml | grep -P "^.\t" | sed 's/h/H/g;s/s/S/g;s/p/P/g;s/n/N/g;s/z/Z/g' | sort > $@
target/essay.txt: makefile target src/essay.txt
	@grep -P "\t" src/essay.txt | grep -v -P "^.\t" | opencc -c t2s > $@
target:
	@mkdir $@
clean:
	rm target/*
