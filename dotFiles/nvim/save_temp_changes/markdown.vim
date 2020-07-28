# this goes in plugged/markdown/syntax/markdown.vim or something


+" latex syntax highlighting
+syntax region Statement oneline matchgroup=Delimiter start="\$" end="\$"
+syntax region Statement matchgroup=Delimiter start="\\begin{.*}" end="\\end{.*}" contains=Statement
+syntax region Statement matchgroup=Delimiter start="{" end="}" contains=Statement
+
+" my custom thingys
+syn keyword basicLanguageKeywords begin end
+syn keyword augmdEnvironmentKeywords thm rmk prop ex cor lem clm defn pf quote
+hi! link basicLanguageKeywords Constant
+hi! link augmdEnvironmentKeywords Type
