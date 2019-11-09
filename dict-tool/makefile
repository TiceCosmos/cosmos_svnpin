# SHELL=/bin/bash
.PHONY: all clean
all: target/cosmos_pinyin.dict.yaml target/essay.txt
target/cosmos_pinyin.dict.yaml: src/head.txt target/merge.txt
	@cat src/head.txt target/merge.txt > $@
target/merge.txt: merge.py target/pinyin_word.txt target/pinyin_phrase.txt target/stroke.txt
	@./merge.py target/pinyin_word.txt target/pinyin_phrase.txt target/stroke.txt > $@
target/pinyin_word.txt: makefile target src/luna_pinyin.dict.yaml
	@grep -P "^.\t" src/luna_pinyin.dict.yaml > $@
target/pinyin_phrase.txt: makefile target src/luna_pinyin.dict.yaml
	@grep -P "\t" src/luna_pinyin.dict.yaml | grep -v -P "^.\t" | cconv -f UTF8-TW -t UTF8-CN > $@
target/stroke.txt: makefile target src/stroke.dict.yaml
	@cat src/stroke.dict.yaml | grep -P "^.\t" | sed 's/h/H/g;s/s/S/g;s/p/P/g;s/n/N/g;s/z/Z/g' > $@
target/essay.txt: makefile target src/essay.txt
	@grep -P "\t" src/essay.txt | grep -v -P "^.\t" | cconv -f UTF8-TW -t UTF8-CN > $@
target:
	@mkdir $@
clean:
	rm target/*
