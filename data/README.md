# データカタログ

- `questions/math.json`: 数学のオリジナル問題
- `questions/science.json`: 理科のオリジナル問題
- `questions/social.json`: 社会のオリジナル問題
- `past-exams/ledger.json`: 過去問の設問台帳。年度・科目・大問・配点・出題分野・正解照合状態・出典を記録し、設問本文・図版は原則保存しない
- `analysis/math-r7-r8.json`: 数学の年度別設問分析
- `../docs/analysis/science-r7-r8.md`: 理科の令和7・8年度過去問分析
- `../docs/analysis/social-r7-r8.md`: 社会の令和7・8年度過去問分析

過去問台帳は、問題PDFと公式正解表を確認できた範囲で登録する。公式正解未確認の設問は空欄とし、推測で補わない。問題データは `data/schemas/question.schema.json` に従う。未検証データを公開用問題として混在させない。
