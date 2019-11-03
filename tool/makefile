# SHELL=/bin/bash
.PHONY: clean
target/cosmos_pinyin.dict.yaml: src/head.dict target/merge.dict
	@cat src/head.dict target/merge.dict > $@
target/merge.dict: merge.py target/pinyin.dict target/stroke.dict target/frequency.dict
	@./merge.py > $@
target/pinyin.dict: makefile target
	@grep -P "^.\t" src/luna_pinyin.dict.yaml > $@
target/stroke.dict: makefile target
	@cat src/stroke.dict.yaml | grep -P '^.\t' | sed 's/h/1/g;s/s/2/g;s/p/3/g;s/n/4/g;s/z/5/g' > $@
target/frequency.dict: makefile target
	@cp src/frequency.dict $@
target:
	@mkdir $@
clean:
	rm target/*
